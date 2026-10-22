# RentHub Gensan 60-second ad: source

`../RentHub_Gensan_Ad.mp4` is the finished ad (1920×1080, 30 fps, 60 s).

| File | Purpose |
|---|---|
| `script.json` | Voiceover lines, one per scene |
| `vo.py` | Synthesizes the voiceover with Kokoro TTS (`af_heart` voice, speed 1.22) and writes `timing.json` |
| `ad.html` | The animated scenes. `render(t)` draws the frame at `t` seconds, and each scene's `data-start` matches its voiceover line |
| `shots/` | Screenshots of the app used in the scenes, captured by `shots.mjs` |
| `frames.mjs` | Renders 1,800 frames from `ad.html` with Playwright |
| `music.py` | Synthesizes the upbeat background track |

The final mix ducks the music under the voice:

```
ffmpeg -framerate 30 -i frames/f%04d.jpg -i vo.wav -i music.wav -filter_complex "[1:a]adelay=400|400,aresample=44100,volume=1.6,asplit=2[v1][v2];[2:a]volume=0.32[m];[m][v1]sidechaincompress=threshold=0.05:ratio=2.5:attack=30:release=500[duck];[duck][v2]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.95,apad[a]" -map 0:v -map "[a]" -t 60 -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k RentHub_Gensan_Ad.mp4
```
