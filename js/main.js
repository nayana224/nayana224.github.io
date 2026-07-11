/** Portfolio interactions: theme, navigation, scroll effects, glow, skill icons, and project modals. */

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initSkillIcons();
    initSmoothScroll();
    initScrollEffects();
    initMouseGlow();
    initProjectModal();
});

function initSkillIcons() {
    const moveItItem = Array.from(document.querySelectorAll('.skill-item'))
        .find((item) => item.textContent.trim() === 'MoveIt 2');

    if (!moveItItem) return;

    const icon = moveItItem.querySelector('img') || document.createElement('img');
    icon.src = 'data:image/png;base64,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';
    icon.alt = 'MoveIt 2 logo';

    if (!icon.parentElement) {
        moveItItem.prepend(icon);
    }
}

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
