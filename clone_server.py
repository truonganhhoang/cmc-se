"""
Máy chủ nhân bản giọng nói cho trang "Kỹ thuật phần mềm CMC" (mã tham khảo).

Trang web gọi:  POST {CONFIG.cloneApi}   (multipart/form-data)
    text       – lời dẫn của một chương
    lang       – "vi" hoặc "en"
    reference  – file ghi âm mẫu 20–30 giây của người dùng
Trả về:  audio/wav

Mô hình:
  - Tiếng Anh: Coqui XTTS-v2 (tts_models/multilingual/multi-dataset/xtts_v2)
  - Tiếng Việt: viXTTS (bản XTTS-v2 tinh chỉnh cho tiếng Việt, mã nguồn mở) – đặt checkpoint vào VI_DIR
Cần GPU (khuyến nghị ≥ 8 GB VRAM). Mã này chưa được chạy thử trong môi trường soạn trang
(không tải được trọng số mô hình), đội kỹ thuật cần kiểm thử trước khi đưa vào sử dụng.

Cài đặt:  pip install coqui-tts fastapi uvicorn python-multipart soundfile
Chạy:     VI_DIR=/models/viXTTS uvicorn clone_server:app --host 0.0.0.0 --port 8000
Rồi đặt CONFIG.cloneApi = "https://<máy-chủ-của-trường>/clone" trong index.html.

Lưu ý pháp lý và đạo đức: chỉ nhân bản giọng của chính người dùng, có xác nhận đồng ý (trang đã có ô xác nhận);
không lưu file mẫu sau khi xử lý; giới hạn tần suất gọi; chỉ cho phép CORS từ tên miền của Trường.
"""
import io, os, tempfile
import soundfile as sf
import torch
from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "https://cmcu.edu.vn").split(",")
VI_DIR = os.environ.get("VI_DIR", "")
MAX_CHARS = 600
device = "cuda" if torch.cuda.is_available() else "cpu"

app = FastAPI(title="CMC SE voice clone")
app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS, allow_methods=["POST"], allow_headers=["*"])

_en = None
_vi = None

def en_model():
    global _en
    if _en is None:
        from TTS.api import TTS
        _en = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    return _en

def vi_model():
    global _vi
    if _vi is None:
        from TTS.tts.configs.xtts_config import XttsConfig
        from TTS.tts.models.xtts import Xtts
        cfg = XttsConfig(); cfg.load_json(os.path.join(VI_DIR, "config.json"))
        m = Xtts.init_from_config(cfg)
        m.load_checkpoint(cfg, checkpoint_dir=VI_DIR, use_deepspeed=False)
        _vi = m.to(device).eval()
    return _vi

@app.post("/clone")
async def clone(text: str = Form(...), lang: str = Form(...), reference: UploadFile = File(...)):
    if lang not in ("vi", "en"):
        raise HTTPException(400, "lang must be vi or en")
    if not text.strip() or len(text) > MAX_CHARS:
        raise HTTPException(400, "text empty or too long")
    data = await reference.read()
    if len(data) > 10_000_000:
        raise HTTPException(400, "reference too large")
    with tempfile.TemporaryDirectory() as d:
        ref_raw = os.path.join(d, "ref_in")
        ref_wav = os.path.join(d, "ref.wav")
        open(ref_raw, "wb").write(data)
        # chuẩn hoá về wav mono 22.05 kHz (cần ffmpeg)
        if os.system(f'ffmpeg -loglevel error -y -i "{ref_raw}" -ac 1 -ar 22050 "{ref_wav}"') != 0:
            raise HTTPException(400, "cannot decode reference audio")
        if lang == "en":
            wav = en_model().tts(text=text, speaker_wav=ref_wav, language="en")
            sr = 24000
        else:
            m = vi_model()
            lat, emb = m.get_conditioning_latents(audio_path=[ref_wav])
            out = m.inference(text, "vi", lat, emb, temperature=0.7, enable_text_splitting=True)
            wav, sr = out["wav"], 24000
    buf = io.BytesIO(); sf.write(buf, wav, sr, format="WAV")
    return Response(buf.getvalue(), media_type="audio/wav")
