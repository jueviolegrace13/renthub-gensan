import json, sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
T='/tmp/claude-0/-home-user-renthub-gensan/0d5eab0f-13e1-536e-81d6-8db6a9bcc1d5/scratchpad/tts/'
k=Kokoro(T+'kokoro.onnx',T+'voices.bin')
voice=sys.argv[1] if len(sys.argv)>1 else 'af_heart'
speed=float(sys.argv[2]) if len(sys.argv)>2 else 1.1
lines=json.load(open('script.json'))
out=[];meta=[];t=0.0
for i,l in enumerate(lines):
    s,sr=k.create(l,voice=voice,speed=speed,lang='en-us')
    # trim edge silence
    nz=np.where(np.abs(s)>0.01)[0]; s=s[max(0,nz[0]-800):nz[-1]+1600]
    gap=np.zeros(int(sr*0.3),dtype=np.float32)
    meta.append({'start':round(t,3),'dur':round(len(s)/sr,3)})
    out+= [s,gap]; t+= (len(s)+len(gap))/sr
a=np.concatenate(out); sf.write('vo.wav',a,sr)
json.dump(meta,open('timing.json','w'),indent=1)
print(voice,speed,'total',round(t,2)); print(meta)
