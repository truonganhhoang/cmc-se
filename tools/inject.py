import json, re, sys
sys.path.insert(0,"/home/claude/tts")
from i18n import EN, ROLES_EN, UI_EN
man=json.load(open("/home/claude/cmc-se/audio/manifest.json",encoding="utf-8"))
en={k:v for k,v in EN.items() if not any(x in k for x in ("Năm 4","~8 sản phẩm","2031","v1 · Năm 1 · Build","v2 · Năm 2 · Team","v3 · Năm 3 · Industry"))}; en["· Kỹ thuật phần mềm"]="· Software Engineering"
data={"manifest":man,"en":en,"rolesEn":ROLES_EN,"ui":UI_EN}
blob=json.dumps(data,ensure_ascii=False,separators=(",",":")).replace("</","<\\/")
p="/home/claude/cmc-se/index.html"; s=open(p,encoding="utf-8").read()
s=re.sub(r"<!--VD-START-->.*?<!--VD-END-->",lambda m:'<!--VD-START--><script type="application/json" id="voiceData">'+blob+'</script><!--VD-END-->',s,flags=re.S)
open(p,"w",encoding="utf-8").write(s); print("injected",len(blob))
