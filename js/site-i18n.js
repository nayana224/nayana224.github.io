const siteI18n = {
  ko: {
    'nav.about':'소개',
    'nav.work':'작업',
    'nav.writing':'글',
    'nav.notes':'노트',
    'nav.archive':'기록',
    'hero.tag':'ROS 2 · 로봇 매니퓰레이션 · 로봇 학습',
    'hero.eyebrow':'로보틱스 엔지니어 · 연구자 · 가끔 글을 씁니다.',
    'hero.description':'로봇을 만들고, 학습이 로보틱스를 어떻게 바꾸는지 공부하며, 오래 남길 만한 생각을 기록합니다. 이곳은 <strong>프로젝트</strong>, <strong>연구 노트</strong>, 그리고 작은 <strong>AI &amp; 로보틱스 브리핑</strong>을 모아두는 개인 공간입니다.',
    'hero.work':'주요 작업 보기',
    'hero.notes':'기술 노트',
    'meta.focus':'현재 관심',
    'meta.across':'다루는 영역',
    'meta.archive':'기록',
    'about.tag':'소개',
    'about.title':'내가 집중하는 <span>문제</span>',
    'skills.tag':'기술',
    'skills.title':'사용하는 <span>도구와 기술</span>',
    'projects.tag':'주요 작업',
    'projects.title':'만들고 <span>검증한 것들</span>',
    'background.tag':'기록',
    'background.title':'수상 · <span>활동</span>',
    'notes.tag':'노트 & 글',
    'notes.title':'만들고 공부하며 <span>남긴 기록</span>',
    'notes.lead':'직접 만든 것, 읽은 논문, 그리고 두 번은 이해해야 했던 문제들을 정리합니다.',
    'briefing.tag':'최근 글',
    'briefing.title':'최근 <span>브리핑 & 노트</span>',
    'briefing.lead':'AI와 로보틱스에서 무엇이 바뀌었는지, 무엇을 읽을 만한지, 그리고 내 연구와 어떻게 이어지는지를 짧게 정리합니다.',
    'briefing.viewall':'모든 글 보기 →'
  },
  en: {
    'nav.about':'About',
    'nav.work':'Work',
    'nav.writing':'Writing',
    'nav.notes':'Notes',
    'nav.archive':'Archive',
    'hero.tag':'ROS 2 · Robotic Manipulation · Robot Learning',
    'hero.eyebrow':'Robotics engineer, researcher, and occasional writer.',
    'hero.description':'I build robots, study how learning changes robotics, and write down the ideas worth keeping. This site is my personal space for <strong>projects</strong>, <strong>research notes</strong>, and a small <strong>AI &amp; robotics briefing</strong>.',
    'hero.work':'Selected Work',
    'hero.notes':'Technical Notes',
    'meta.focus':'Current focus',
    'meta.across':'Working across',
    'meta.archive':'Archive',
    'about.tag':'Profile',
    'about.title':'Engineering <span>Focus</span>',
    'skills.tag':'Capabilities',
    'skills.title':'Technical <span>Stack</span>',
    'projects.tag':'Selected Work',
    'projects.title':'Project <span>Experience</span>',
    'background.tag':'Background',
    'background.title':'Awards &amp; <span>Activities</span>',
    'notes.tag':'Notes & Writing',
    'notes.title':'Notes from <span>building &amp; studying</span>',
    'notes.lead':'Notes on things I built, papers I read, and problems I had to understand twice.',
    'briefing.tag':'Latest Writing',
    'briefing.title':'Recent <span>briefings &amp; notes</span>',
    'briefing.lead':'Short posts on AI and robotics: what changed, what is worth reading, and what connects back to my work.',
    'briefing.viewall':'View all writing →'
  }
};

let siteLang = localStorage.getItem('site-lang') || 'ko';

function applySiteLanguage() {
  document.documentElement.lang = siteLang;
  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const value = siteI18n[siteLang]?.[el.dataset.i18n];
    if (value) el.textContent = value;
  });
  document.querySelectorAll('[data-i18n-html]').forEach((el) => {
    const value = siteI18n[siteLang]?.[el.dataset.i18nHtml];
    if (value) el.innerHTML = value;
  });
  document.querySelectorAll('.site-language-button').forEach((button) => {
    button.classList.toggle('active', button.dataset.lang === siteLang);
  });
}

document.querySelectorAll('.site-language-button').forEach((button) => {
  button.addEventListener('click', () => {
    siteLang = button.dataset.lang;
    localStorage.setItem('site-lang', siteLang);
    localStorage.setItem('briefing-lang', siteLang);
    applySiteLanguage();
  });
});

applySiteLanguage();
