import numpy as np, soundfile as sf
sr=44100; dur=60.0; N=int(sr*dur); out=np.zeros(N)
rng=np.random.default_rng(1)
def pluck(f,length=0.9,amp=0.3):
    n=int(sr*length); p=int(sr/f); buf=rng.uniform(-1,1,p); y=np.zeros(n)
    for i in range(n):
        y[i]=buf[i%p]; buf[i%p]=0.5*(buf[i%p]+buf[(i+1)%p])*0.996
    return y*amp
def add(sig,t):
    i=int(t*sr)
    if i>=N: return
    j=min(N,i+len(sig)); out[i:j]+=sig[:j-i]
note=lambda m:440*2**((m-69)/12)
bpm=118; beat=60/bpm
chords=[[60,64,67,72],[55,62,67,71],[57,60,64,69],[53,60,65,69]]  # C G Am F
cache={}
def P(m,l=0.9,a=0.25):
    k=(m,l)
    if k not in cache: cache[k]=pluck(note(m),l,1)
    return cache[k]*a
t=0;bar=0
pattern=[0,2,1,3,2,1,3,2]  # ukulele-ish arpeggio in eighths
while t<dur:
    ch=chords[bar%4]
    add(P(ch[0]-12,1.8,0.35),t)
    for k,idx in enumerate(pattern):
        add(P(ch[idx],0.7,0.18 if k%2 else 0.24),t+k*beat/2)
    # kick on 1 and 3, clap/shaker on 2 and 4
    for b in range(4):
        tb=t+b*beat
        if b%2==0:
            n=int(sr*0.25); tt=np.arange(n)/sr
            add(np.sin(2*np.pi*(50+80*np.exp(-tt*25))*tt)*np.exp(-tt*12)*0.5,tb)
        else:
            n=int(sr*0.15); add(rng.uniform(-1,1,n)*np.exp(-np.arange(n)/sr*30)*0.12,tb)
        n=int(sr*0.05); add(rng.uniform(-1,1,n)*np.exp(-np.arange(n)/sr*90)*0.05,tb+beat/2)
    t+=4*beat; bar+=1
out=np.tanh(out*1.2)
fi=int(sr*0.5); fo=int(sr*3)
out[:fi]*=np.linspace(0,1,fi); out[-fo:]*=np.linspace(1,0,fo)
out/=np.abs(out).max(); sf.write('music.wav',(out*0.9).astype(np.float32),sr)
