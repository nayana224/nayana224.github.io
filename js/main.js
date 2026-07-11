/** Portfolio interactions: theme, navigation, scroll effects, glow, and project modals. */

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initSmoothScroll();
    initScrollEffects();
    initMouseGlow();
    initProjectModal();
});

function initTheme() {
    const root = document.documentElement;
    const toggle = document.getElementById('theme-toggle');
    if (!toggle) return;

    const storedTheme = localStorage.getItem('portfolio-theme');
    const systemPrefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
    const initialTheme = storedTheme || (systemPrefersLight ? 'light' : 'dark');

    const applyTheme = (theme) => {
        root.dataset.theme = theme;
        const nextTheme = theme === 'dark' ? 'light' : 'dark';
        toggle.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
        toggle.setAttribute('title', `Switch to ${nextTheme} theme`);
    };

    applyTheme(initialTheme);

    toggle.addEventListener('click', () => {
        const nextTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
        applyTheme(nextTheme);
        localStorage.setItem('portfolio-theme', nextTheme);
    });
}

function initSmoothScroll() {
    const internalLinks = document.querySelectorAll('a[href^="#"]');

    internalLinks.forEach((link) => {
        link.addEventListener('click', (event) => {
            const targetId = link.getAttribute('href');
            if (!targetId || targetId === '#') return;

            const targetSection = document.querySelector(targetId);
            if (!targetSection) return;

            event.preventDefault();
            const header = document.getElementById('header-nav');
            const headerHeight = header ? header.offsetHeight : 0;
            const targetPosition = targetSection.getBoundingClientRect().top + window.scrollY - headerHeight;

            window.scrollTo({ top: targetPosition, behavior: 'smooth' });
        });
    });
}

function initScrollEffects() {
    const header = document.getElementById('header-nav');
    const scrollBar = document.getElementById('scroll-bar');
    const sections = document.querySelectorAll('section[id]');

    const updateScrollState = () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;

        if (scrollBar && docHeight > 0) {
            scrollBar.style.width = `${(scrollTop / docHeight) * 100}%`;
        }

        if (header) header.classList.toggle('scrolled', scrollTop > 50);

        let currentSectionId = '';
        sections.forEach((section) => {
            const sectionTop = section.offsetTop - 140;
            if (scrollTop >= sectionTop && scrollTop < sectionTop + section.offsetHeight) {
                currentSectionId = section.id;
            }
        });

        document.querySelectorAll('.nav-links a[href^="#"]').forEach((link) => {
            link.classList.toggle('active', link.getAttribute('href') === `#${currentSectionId}`);
        });
    };

    window.addEventListener('scroll', updateScrollState, { passive: true });
    updateScrollState();
}

function initMouseGlow() {
    const glowBg = document.getElementById('glow-bg');
    if (!glowBg || window.matchMedia('(pointer: coarse)').matches) return;

    window.addEventListener('mousemove', (event) => {
        glowBg.style.setProperty('--mouse-x', `${event.clientX}px`);
        glowBg.style.setProperty('--mouse-y', `${event.clientY}px`);
    }, { passive: true });
}

function initProjectModal() {
    const modal = document.getElementById('project-modal');
    const modalBody = document.getElementById('modal-body-content');
    const closeButton = document.getElementById('modal-close');
    const detailButtons = document.querySelectorAll('.project-more-btn');

    if (!modal || !modalBody || !closeButton) return;

    const openModal = (projectId) => {
        const template = document.getElementById(`template-${projectId}`);
        if (!template) return;

        modalBody.innerHTML = template.innerHTML;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
        closeButton.focus();
    };

    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        window.setTimeout(() => { modalBody.innerHTML = ''; }, 400);
    };

    detailButtons.forEach((button) => {
        button.addEventListener('click', () => openModal(button.dataset.project));
    });

    closeButton.addEventListener('click', closeModal);
    modal.addEventListener('click', (event) => {
        if (event.target === modal) closeModal();
    });
    window.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && modal.classList.contains('active')) closeModal();
    });
}
