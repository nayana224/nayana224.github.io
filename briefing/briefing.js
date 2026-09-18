const state = { items: [], active: 'All', lang: localStorage.getItem('briefing-lang') || 'ko', data: null };

const byId = (id) => document.getElementById(id);

const ui = {
  ko: {
    'nav.portfolio': '포트폴리오',
    'hero.kicker': 'AI & Research Briefing',
    'hero.title': 'AI, 로보틱스, 로봇 학습에서<br>놓치지 말아야 할 변화.',
    'hero.description': '무엇이 바뀌었는지, 왜 중요한지, 그리고 내 연구와 어떻게 연결되는지를 짧고 밀도 있게 정리합니다.',
    'radar.label': '현재 주목 분야',
    'feed.preview': '최근 검증 피드 · 1차 출처 우선',
    'feed.empty': '이 카테고리에는 아직 브리핑이 없습니다.',
    'footer.back': '포트폴리오로 돌아가기 →',
    'why': '왜 중요한가',
    'research': '내 연구와의 연결',
    'published': '게시',
    'status': '상태',
    'sourceType': '출처 유형',
    'sources': '출처',
    'verified': '검증됨',
    'preview': '프리뷰 샘플',
    'primary': '1차 출처',
    'secondary': '2차 출처',
    'none': '출처 없음'
  },
  en: {
    'nav.portfolio': 'Portfolio',
    'hero.kicker': 'AI & Research Briefing',
    'hero.title': 'Things worth tracking in<br>AI, robotics, and robot learning.',
    'hero.description': 'Short, high-signal notes on what changed, why it matters, and how it connects to my research.',
    'radar.label': 'Currently watching',
    'feed.preview': 'Recent verified feed · primary sources preferred',
    'feed.empty': 'No briefings in this category yet.',
    'footer.back': 'Back to portfolio →',
    'why': 'Why it matters',
    'research': 'Research connection',
    'published': 'Published',
    'status': 'Status',
    'sourceType': 'Source type',
    'sources': 'Sources',
    'verified': 'Verified',
    'preview': 'Preview sample',
    'primary': 'Primary source',
    'secondary': 'Secondary source',
    'none': 'No source'
  }
};

function formatPublished(value) {
  if (!value) return '';
  const locale = state.lang === 'ko' ? 'ko-KR' : 'en';

  if (!value.includes('T')) {
    return new Intl.DateTimeFormat(locale, {
      year: 'numeric',
      month: 'short',
      day: '2-digit'
    }).format(new Date(value + 'T00:00:00'));
  }

  return new Intl.DateTimeFormat(locale, {
    year: 'numeric',
    month: 'short',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'Asia/Seoul',
    timeZoneName: 'short'
  }).format(new Date(value));
}

function verificationLabel(value) {
  if (value === 'verified') return ui[state.lang].verified;
  return ui[state.lang].preview;
}

function sourceTypeLabel(value) {
  if (value === 'primary') return ui[state.lang].primary;
  if (value === 'secondary') return ui[state.lang].secondary;
  return ui[state.lang].none;
}

function formatDate(date) {
  const locale = state.lang === 'ko' ? 'ko-KR' : 'en';
  return new Intl.DateTimeFormat(locale, { month: 'short', day: '2-digit' })
    .format(new Date(date + 'T00:00:00'));
}

function applyLanguage() {
  document.documentElement.lang = state.lang;
  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const value = ui[state.lang][el.dataset.i18n];
    if (value) el.textContent = value;
  });
  document.querySelectorAll('[data-i18n-html]').forEach((el) => {
    const value = ui[state.lang][el.dataset.i18nHtml];
    if (value) el.innerHTML = value;
  });
  document.querySelectorAll('.language-button').forEach((button) => {
    button.classList.toggle('active', button.dataset.lang === state.lang);
  });
}

function categoryLabel(category) {
  const map = {
    All: {ko:'전체',en:'All'},
    AI: {ko:'AI',en:'AI'},
    Robotics: {ko:'로보틱스',en:'Robotics'},
    Vision: {ko:'비전',en:'Vision'},
    Papers: {ko:'논문',en:'Papers'},
    Simulation: {ko:'시뮬레이션',en:'Simulation'}
  };
  return map[category]?.[state.lang] || category;
}

function renderFilters() {
  const root = byId('filter-list');
  root.innerHTML = '';
  ['All','AI','Robotics','Vision','Papers','Simulation'].forEach((filter) => {
    const button = document.createElement('button');
    button.className = 'filter-button' + (state.active === filter ? ' active' : '');
    button.type = 'button';
    button.textContent = categoryLabel(filter);
    button.addEventListener('click', () => {
      state.active = filter;
      renderFilters();
      renderFeed();
    });
    root.appendChild(button);
  });
}

function renderFeed() {
  const root = byId('briefing-feed');
  const empty = byId('feed-empty');
  const items = state.active === 'All'
    ? state.items
    : state.items.filter((item) => item.category === state.active);

  root.innerHTML = '';
  empty.hidden = items.length > 0;

  items.forEach((item, index) => {
    const text = item[state.lang] || item.en;
    const article = document.createElement('article');
    article.className = 'briefing-entry';

    const sources = item.sources?.length
      ? '<div class="entry-links"><span class="entry-links-label">' + ui[state.lang].sources + '</span>' + item.sources.map((s) =>
          '<a class="source-link" href="' + s.url + '" target="_blank" rel="noreferrer"><span>' + (s.label?.[state.lang] || s.label || 'Source') + ' ↗</span><small>' + s.url + '</small></a>'
        ).join('') + '</div>'
      : '';

    const provenance =
      '<div class="entry-provenance">' +
        '<div><span>' + ui[state.lang].published + '</span><strong>' + formatPublished(item.published_at) + '</strong></div>' +
        '<div><span>' + ui[state.lang].status + '</span><strong class="' + (item.verification === 'verified' ? 'is-verified' : 'is-preview') + '">' + verificationLabel(item.verification) + '</strong></div>' +
        '<div><span>' + ui[state.lang].sourceType + '</span><strong>' + sourceTypeLabel(item.source_type) + '</strong></div>' +
      '</div>';

    article.innerHTML =
      '<div class="entry-index"><strong>' + String(index + 1).padStart(2, '0') + '</strong>' +
      '<span>' + formatDate(item.date) + '</span></div>' +
      '<div>' +
        '<div class="entry-meta"><span class="category">' + categoryLabel(item.category) + '</span>' +
        item.tags.map((tag) => '<span>' + tag + '</span>').join('') + '</div>' +
        '<h2>' + text.title + '</h2>' +
        provenance +
        '<p class="entry-summary">' + text.summary + '</p>' +
        '<div class="entry-sections">' +
          '<div class="entry-block"><h3>' + ui[state.lang].why + '</h3><p>' + text.why_it_matters + '</p></div>' +
          '<div class="entry-block"><h3>' + ui[state.lang].research + '</h3><p>' + text.research_connection + '</p></div>' +
        '</div>' +
        sources +
      '</div>';

    root.appendChild(article);
  });
}

function initTheme() {
  const root = document.documentElement;
  const saved = localStorage.getItem('theme');
  root.dataset.theme = saved || 'light';

  byId('theme-toggle').addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
    localStorage.setItem('theme', root.dataset.theme);
  });
}

function initLanguage() {
  document.querySelectorAll('.language-button').forEach((button) => {
    button.addEventListener('click', () => {
      state.lang = button.dataset.lang;
      localStorage.setItem('briefing-lang', state.lang);
      applyLanguage();
      renderFilters();
      renderFeed();
    });
  });
}

async function init() {
  initTheme();
  initLanguage();
  applyLanguage();

  try {
    const response = await fetch('../data/briefings.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('Failed to load briefing data');
    state.data = await response.json();
    state.items = state.data.items || [];
    renderFilters();
    renderFeed();
  } catch (error) {
    byId('briefing-feed').innerHTML =
      '<div class="feed-empty">' +
      (state.lang === 'ko' ? '브리핑 데이터를 불러오지 못했습니다.' : 'Briefing data could not be loaded.') +
      '</div>';
    console.error(error);
  }
}

init();