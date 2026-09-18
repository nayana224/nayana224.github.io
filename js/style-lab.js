const root=document.documentElement;
const buttons=[...document.querySelectorAll('.theme-chip')];
buttons.forEach(button=>{
  button.addEventListener('click',()=>{
    root.dataset.theme=button.dataset.themeValue;
    buttons.forEach(b=>b.classList.toggle('active',b===button));
  });
});
