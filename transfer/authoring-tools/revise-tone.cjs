const fs = require('node:fs');
const root = 'apps/web/src/app/';
let global = fs.readFileSync(root + 'globals.css', 'utf8');
const tokens = {
background:'#242520',foreground:'#f3f1e8',card:'#2c2e27','card-foreground':'#f3f1e8',muted:'#34362f','muted-foreground':'#b5b9aa','muted-foreground-strong':'#c9cbbf',border:'#4b4e43',input:'#858978',overlay:'rgba(15, 17, 13, 0.75)',skeleton:'#3b3e34',primary:'#ff9674','primary-strong':'#ff9674','primary-hover':'#ffad93','primary-foreground':'#32231a','primary-text':'#ff9674','primary-subtle':'#41332b','primary-on-subtle':'#ffb39a',secondary:'#cadc85',accent:'#cadc85','accent-hover':'#d7e6a5','accent-foreground':'#303923','accent-subtle':'#35415b','on-accent-subtle':'#e0e8fa',ring:'#ff9674','ring-offset':'#242520',success:'#cadc85','success-subtle':'#333d29','on-success-subtle':'#d8eaa1',warning:'#efc884','warning-subtle':'#443a28','on-warning-subtle':'#f4d49e',destructive:'#f08482','destructive-hover':'#f59b99','destructive-foreground':'#251a1a','destructive-subtle':'#472e2d','on-destructive-subtle':'#ffc6bd',info:'#b8c8eb','info-subtle':'#35415b','on-info-subtle':'#e0e8fa'
};
for (const [key,value] of Object.entries(tokens)) global=global.replace(new RegExp('(--color-'+key+':)[^;]+;'), '$1 '+value+';');
global=global.replace('@import "./studio.css";', '@import "./studio.css";\n@import "./course-site.css";');
global=global.replace('html {\n', 'html {\n  color-scheme: dark;\n');
fs.writeFileSync(root+'globals.css',global);
let studio=fs.readFileSync(root+'studio.css','utf8');
const map={
'#4264dc':'var(--color-secondary)','#294bc9':'var(--color-accent-subtle)','#fff':'var(--color-foreground)',
'#d1daed':'var(--color-border)','#e3e9f5':'var(--color-border)','#3659a0':'transparent',
'#d9e3ff':'var(--color-on-accent-subtle)','#e2e9ff':'var(--color-on-accent-subtle)','#edf2ff':'var(--color-muted)',
'#c5d3ff':'var(--color-secondary)','#f9faff':'var(--color-background)','#7391e5':'var(--color-primary)',
'#e9eef8':'var(--color-muted)','#53617a':'var(--color-muted-foreground)','#243e7320':'transparent',
'#cdd6e7':'var(--color-input)','#6a778d':'var(--color-muted-foreground)','#d6dfff':'var(--color-border)',
'#e9edf5':'var(--color-border)','#6b7c98':'var(--color-muted-foreground)','#edf1ff':'var(--color-accent-subtle)',
'#3d5cca':'var(--color-on-accent-subtle)','#fff1db':'var(--color-secondary)','#946416':'var(--color-accent-foreground)',
'#e9f3ef':'var(--color-primary-subtle)','#38715c':'var(--color-primary-text)','#98a5b8':'var(--color-muted-foreground)',
'#f3f6fe':'var(--color-background)','#d9e2f5':'var(--color-border)','#d4def2':'var(--color-border)',
'#172640':'#191e19','#e1eaff':'#e5edda','#7c8ba3':'var(--color-muted-foreground)',
'#fff6e5':'var(--color-primary-subtle)','#72531b':'var(--color-primary-on-subtle)','#eef2fb':'var(--color-card)',
'#d5e0fa':'var(--color-accent-subtle)','#2646ba':'var(--color-on-accent-subtle)','#b77722':'var(--color-primary)',
'#f4f6fb':'var(--color-background)','#e8b85c':'var(--color-primary)','#fff8ed':'var(--color-primary-subtle)',
'#eef2ff':'var(--color-card)','#cfdaef':'var(--color-border)','#aabbeb':'var(--color-primary)',
'#2848a5':'transparent','#eaf0ff':'var(--color-muted)','#bacbec':'var(--color-border)',
'#f8efd9':'var(--color-primary-subtle)','#80601f':'var(--color-primary-on-subtle)','#e0d1aa':'var(--color-border)',
'#b8c8eb':'var(--color-input)','#f4f7ff':'var(--color-card)','#f7f9ff':'var(--color-background)',
'#f0f4ff':'var(--color-card)','#d8e1f6':'var(--color-border)','#dce5fa':'var(--color-border)'
};
studio=studio.replace(/#[a-f0-9]{3,8}\b/gi,hex=>map[hex.toLowerCase()]??hex);
fs.writeFileSync(root+'studio.css',studio);
console.log('Applied the exact dark Maker’s Notebook palette.');
