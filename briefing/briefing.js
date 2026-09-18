const state = { items: [], active: 'All' };

const byId = (id) => document.getElementById(id);

function formatDate(date) {
  return new Intl.DateTimeFormat('en', { month: 'short', day: '2-digit' })
    .format(new Date(date + 'T00:00:00'));
}

function renderFilters(filters) {
  const root = byId('filter-list');
  root.innerHTML = '';
  filters.forEach((filter) => {
    const button = document.createElement('button');
    button.className = 'filter-button' + (state.active === filter ? ' active' : '');
    button.type = 'button';
    button.textContent = filter;
    button.addEventListener('click', () => {
      state.active = filter;
      renderFilters(filters);
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
    const article = document.createElement('article');
    article.className = 'briefing-entry';

    const sources = item.sources?.length
      ? '<div class="entry-links">' + item.sources.map((s) =>
          '<a href="' + s.url + '" target="_blank" rel="noreferrer">' + s.label + ' ↗</a>'
        ).join('') + '</div>'
      : '';

    article.innerHTML =
      '<div class="entry-index"><strong>' + String(index + 1).padStart(2, '0') + '</strong>' +
      '<span>' + formatDate(item.date) + '</span></div>' +
      '<div>' +
        '<div class="entry-meta"><span class="category">' + item.category + '</span>' +
        item.tags.map((tag) => '<span>' + tag + '</span>').join('') + '</div>' +
        '<h2>' + item.title + '</h2>' +
        '<p class="entry-summary">' + item.summary + '</p>' +
        '<div class="entry-sections">' +
          '<div class="entry-block"><h3>Why it matters</h3><p>' + item.why_it_matters + '</p></div>' +
          '<div class="entry-block"><h3>Research connection</h3><p>' + item.research_connection + '</p></div>' +
        '</div>' +
        sources +
      '</div>';

    root.appendChild(article);
  });
}

function initTheme() {
  const root = document.documentElement;
  const saved = localStorage.getItem('theme');
  if (saved) root.dataset.theme = saved;

  byId('theme-toggle').addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
    localStorage.setItem('theme', root.dataset.theme);
  });
}

async function init() {
  initTheme();
  try {
    const response = await fetch('../data/briefings.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('Failed to load briefing data');
    const data = await response.json();
    state.items = data.items || [];
    renderFilters(data.filters || ['All']);
    renderFeed();
  } catch (error) {
    byId('briefing-feed').innerHTML =
      '<div class="feed-empty">Briefing data could not be loaded.</div>';
    console.error(error);
  }
}

init();