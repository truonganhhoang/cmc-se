import sherpa_onnx, numpy as np, soundfile as sf, subprocess, json, os, re, sys, time
from narration import NARR, vi_say, en_say
M="/home/claude/tts/models/"; OUT="/home/claude/cmc-se/audio"; TMP="/tmp/ttsw"
os.makedirs(OUT,exist_ok=True); os.makedirs(TMP,exist_ok=True)

def vits(name,onnx,**kw):
    return sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=M+name+"/"+onnx,tokens=M+name+"/tokens.txt",data_dir=M+name+"/espeak-ng-data",**kw),num_threads=2)))
def kokoro():
    d=M+"kokoro-multi-lang-v1_0/"
    return sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(model=d+"model.onnx",voices=d+"voices.bin",tokens=d+"tokens.txt",data_dir=d+"espeak-ng-data",dict_dir=d+"dict",lexicon=d+"lexicon-us-en.txt"),num_threads=2)))

VOICES=[
 dict(id="vi-mai",lang="vi",name="Mai",desc="Nữ · miền Bắc",engine="vais",sid=0,speed=0.92,post=""),
 dict(id="vi-minh",lang="vi",name="Minh",desc="Giọng trầm",engine="vais",sid=0,speed=0.95,post="asetrate=22050*0.86,aresample=22050,rubberband=pitch=0.85:tempo=1.163:formant=preserved,"),
 dict(id="en-heart",lang="en",name="Heart",desc="Female · US",engine="kokoro",sid=3,speed=0.98,post=""),
 dict(id="en-michael",lang="en",name="Michael",desc="Male · US",engine="kokoro",sid=16,speed=0.98,post=""),
 dict(id="en-emma",lang="en",name="Emma",desc="Female · UK",engine="kokoro",sid=21,speed=0.98,post=""),
]
only=[a for a in sys.argv[1:] if not a.startswith("--slides=")]
SEL=[int(x)-1 for a in sys.argv[1:] if a.startswith("--slides=") for x in a[9:].split(",")]
eng={}
def get(e):
    if e not in eng:
        eng[e]=vits("vits-piper-vi_VN-vais1000-medium","vi_VN-vais1000-medium.onnx",noise_scale=0.55,noise_scale_w=0.7) if e=="vais" else kokoro()
    return eng[e]

manifest={"voices":[],"slides":{}}
mf=OUT+"/manifest.json"
if os.path.exists(mf): manifest=json.load(open(mf))
POST_CHAIN="highpass=f=70,equalizer=f=180:t=q:w=1:g=1.5,equalizer=f=3200:t=q:w=1.2:g=2,equalizer=f=7500:t=q:w=1.5:g=-2,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2,loudnorm=I=-16:TP=-1.5:LRA=9"
for v in VOICES:
    if only and v["id"] not in only: continue
    tts=get(v["engine"]); slides=[]
    t0=time.time()
    old=manifest["slides"].get(v["id"],[])
    for si,(vi,en) in enumerate(NARR):
        if SEL and si not in SEL and si<len(old):
            slides.append(old[si]); continue
        sents = vi if v["lang"]=="vi" else en
        parts=[]; segs=[]; t=0.25; sr=None
        lead=np.zeros(int(0.25*24000),dtype=np.float32)
        for k,s in enumerate(sents):
            say = vi_say(s) if v["lang"]=="vi" else en_say(s)
            a=tts.generate(say,sid=v["sid"],speed=v["speed"]); x=np.array(a.samples,dtype=np.float32); sr=a.sample_rate
            # trim edges
            nz=np.where(np.abs(x)>0.01)[0]
            if len(nz): x=x[max(0,nz[0]-int(.03*sr)):nz[-1]+int(.06*sr)]
            parts.append((s,x))
        # assemble at native sr
        gap=lambda sec: np.zeros(int(sec*sr),dtype=np.float32)
        buf=[gap(0.25)]; t=0.25
        for k,(s,x) in enumerate(parts):
            segs.append({"t":round(t,2),"text":s}); buf.append(x); t+=len(x)/sr
            if k<len(parts)-1: buf.append(gap(0.42)); t+=0.42
        buf.append(gap(0.5))
        wav=f"{TMP}/{v['id']}_{si+1:02d}.wav"; sf.write(wav,np.concatenate(buf),sr)
        mp3=f"{OUT}/{v['id']}/{si+1:02d}.mp3"; os.makedirs(os.path.dirname(mp3),exist_ok=True)
        chain=v["post"]+POST_CHAIN
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",wav,"-af",chain,"-ar","24000","-ac","1","-c:a","libmp3lame","-b:a","56k",mp3],check=True)
        dur=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",mp3],capture_output=True,text=True).stdout)
        slides.append({"file":f"audio/{v['id']}/{si+1:02d}.mp3","dur":round(dur,2),"segs":segs})
    manifest["slides"][v["id"]]=slides
    manifest["voices"]=[x for x in manifest["voices"] if x["id"]!=v["id"]]+[{k:v[k] for k in ("id","lang","name","desc")}]
    print(v["id"],"done",round(time.time()-t0,1),"s; total",round(sum(s["dur"] for s in slides),1),"s",flush=True)
order=[x["id"] for x in VOICES]
manifest["voices"].sort(key=lambda x: order.index(x["id"]))
json.dump(manifest,open(mf,"w"),ensure_ascii=False,indent=1)
