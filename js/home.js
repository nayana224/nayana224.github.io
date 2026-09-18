const root=document.documentElement;
root.dataset.theme=localStorage.getItem('theme')||'light';
document.getElementById('theme-toggle')?.addEventListener('click',()=>{
  root.dataset.theme=root.dataset.theme==='light'?'dark':'light';
  localStorage.setItem('theme',root.dataset.theme);
});

async function loadLatest(){
  try{
    const response=await fetch('data/briefings.json',{cache:'no-store'});
    const data=await response.json();
    const items=[...(data.items||[])].sort((a,b)=>b.date.localeCompare(a.date));
    const item=items[0];
    if(!item)return;
    const text=item.ko||item.en;
    document.getElementById('latest-date').textContent=item.date.replaceAll('-','.');
    document.getElementById('latest-title').textContent=text.title;
    document.getElementById('latest-summary').textContent=text.summary;
  }catch(e){console.error(e);}
}
loadLatest();
