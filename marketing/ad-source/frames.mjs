import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+process.cwd()+'/ad.html'); await p.waitForLoadState('networkidle'); await p.evaluate(()=>document.fonts.ready);
for(let f=0;f<1800;f++){ await p.evaluate(t=>render(t),f/30); await p.screenshot({path:`frames/f${String(f).padStart(4,'0')}.jpg`,type:'jpeg',quality:93}); }
await b.close();
