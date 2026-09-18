const homeCopy = {
  ko: {
    'nav.portfolio':'포트폴리오',
    'nav.news':'뉴스',
    'hero.eyebrow':'Robotics · AI · Research · Writing',
    'hero.intro':'로봇을 만들고, AI와 로봇 학습을 공부하며, 프로젝트와 연구 기록을 남깁니다. 이곳은 <strong>포트폴리오</strong>, <strong>AI 뉴스 브리핑</strong>, <strong>개인 블로그</strong>로 이어지는 개인 홈입니다.',
    'status.label':'현재 관심',
    'directory.kicker':'바로가기',
    'directory.title':'한눈에 보는 내 공간',
    'cards.portfolio.label':'포트폴리오',
    'cards.portfolio.title':'프로젝트 & 경험',
    'cards.portfolio.desc':'로보틱스 프로젝트, 기술 스택, 수상 및 활동 기록.',
    'cards.news.label':'AI & Research News',
    'cards.news.title':'데일리 브리핑',
    'cards.news.desc':'AI·로보틱스 최신 변화와 내 연구 관점의 짧은 해설.',
    'cards.velog.title':'개인 블로그 & 노트',
    'cards.velog.desc':'공부하면서 정리한 개념, 구현, 디버깅, 논문 학습 기록.',
    'cards.github.title':'코드 & 저장소',
    'cards.github.desc':'프로젝트 코드, 실습 저장소, 공개 작업 기록.',
    'now.kicker':'요즘',
    'now.title':'요즘 보고 있는 것',
    'footer.text':'로보틱스, AI, 그리고 기록할 가치가 있는 것들.'
  },
  en: {
    'nav.portfolio':'Portfolio',
    'nav.news':'News',
    'hero.eyebrow':'Robotics · AI · Research · Writing',
    'hero.intro':'I build robots, study AI and robot learning, and keep notes on projects and research. This is my personal home connecting my <strong>portfolio</strong>, <strong>AI briefing</strong>, and <strong>personal blog</strong>.',
    'status.label':'Current focus',
    'directory.kicker':'Start here',
    'directory.title':'Everything in one place',
    'cards.portfolio.label':'Portfolio',
    'cards.portfolio.title':'Projects & Experience',
    'cards.portfolio.desc':'Robotics projects, technical stack, awards, and activities.',
    'cards.news.label':'AI & Research News',
    'cards.news.title':'Daily Briefing',
    'cards.news.desc':'Short notes on AI and robotics updates through my research lens.',
    'cards.velog.title':'Personal Blog & Notes',
    'cards.velog.desc':'Concepts, implementation notes, debugging, and paper study logs.',
    'cards.github.title':'Code & Repositories',
    'cards.github.desc':'Project code, practice repositories, and public engineering work.',
    'now.kicker':'Now',
    'now.title':'What I am following now',
    'footer.text':'Robotics, AI, and things worth writing down.'
  }
};

let lang=localStorage.getItem('site-lang')||'ko';
function applyLanguage(){
  document.documentElement.lang=lang;
  document.querySelectorAll('[data-i18n]').forEach(el=>{
    const value=homeCopy[lang]?.[el.dataset.i18n];
    if(value) el.textContent=value;
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el=>{
    const value=homeCopy[lang]?.[el.dataset.i18nHtml];
    if(value) el.innerHTML=value;
  });
  document.querySelectorAll('.home-language-button').forEach(btn=>btn.classList.toggle('active',btn.dataset.lang===lang));
}
document.querySelectorAll('.home-language-button').forEach(btn=>btn.addEventListener('click',()=>{
  lang=btn.dataset.lang;
  localStorage.setItem('site-lang',lang);
  localStorage.setItem('briefing-lang',lang);
  applyLanguage();
}));

const root=document.documentElement;
root.dataset.theme=localStorage.getItem('theme')||'light';
document.getElementById('theme-toggle').addEventListener('click',()=>{
  root.dataset.theme=root.dataset.theme==='light'?'dark':'light';
  localStorage.setItem('theme',root.dataset.theme);
});
applyLanguage();
