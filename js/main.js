/**
 * 파일명: main.js
 * 기능: 로보틱스 포트폴리오 웹사이트의 UI 상호작용 및 인터랙션 제어
 */

document.addEventListener('DOMContentLoaded', () => {
    initSmoothScroll();
    initScrollEffects();
    initMouseGlow();
    initProjectModal();
});

/**
 * 1. 네비게이션 메뉴 클릭 시 해당 섹션으로 부드럽게 스크롤하는 함수
 */
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                // 네비게이션 헤더 높이를 감안하여 오프셋 스크롤
                const headerHeight = document.getElementById('header-nav').offsetHeight;
                const targetPosition = targetSection.getBoundingClientRect().top + window.scrollY - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * 2. 스크롤 진행률 표시바 및 헤더 글라스모피즘 효과 토글
 */
function initScrollEffects() {
    const header = document.getElementById('header-nav');
    const scrollBar = document.getElementById('scroll-bar');
    const sections = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        
        // 스크롤 바 너비 계산
        if (docHeight > 0) {
            const scrollPercentage = (scrollTop / docHeight) * 100;
            scrollBar.style.width = `${scrollPercentage}%`;
        }

        // 헤더 글라스모피즘 스타일 적용
        if (scrollTop > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // 스크롤 위치에 맞춰 활성화된 메뉴 하이라이트
        let currentSectionId = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (scrollTop >= sectionTop && scrollTop < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        const navLinks = document.querySelectorAll('.nav-links a');
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });
}

/**
 * 3. 마우스 포인터 뒤를 따라가는 은은한 네온 빛무리(Glow) 효과
 */
function initMouseGlow() {
    const glowBg = document.getElementById('glow-bg');
    
    if (!glowBg) return;

    window.addEventListener('mousemove', (e) => {
        // CSS Custom Properties 변수값 업데이트
        glowBg.style.setProperty('--mouse-x', `${e.clientX}px`);
        glowBg.style.setProperty('--mouse-y', `${e.clientY}px`);
    });
}

/**
 * 4. 프로젝트 카드 클릭 시 상세 정보를 담은 템플릿 모달 로딩 및 여닫기
 */
function initProjectModal() {
    const modal = document.getElementById('project-modal');
    const modalBody = document.getElementById('modal-body-content');
    const closeBtn = document.getElementById('modal-close');
    const moreButtons = document.querySelectorAll('.project-more-btn');

    if (!modal || !modalBody || !closeBtn) return;

    // 모달 열기 함수
    const openModal = (projectId) => {
        const template = document.getElementById(`template-${projectId}`);
        if (template) {
            // 해당 템플릿의 HTML 내용을 복사하여 모달 바디에 주입
            modalBody.innerHTML = template.innerHTML;
            modal.classList.add('active');
            // 뒷배경 스크롤 방지
            document.body.style.overflow = 'hidden';
        }
    };

    // 모달 닫기 함수
    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        // 트랜지션 완료 후 바디 내용 초기화
        setTimeout(() => {
            modalBody.innerHTML = '';
        }, 400);
    };

    // 프로젝트 카드의 '상세 분석 보기' 버튼 클릭 이벤트 연동
    moreButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const projectId = btn.getAttribute('data-project');
            if (projectId) {
                openModal(projectId);
            }
        });
    });

    // 닫기 버튼 클릭 시 모달 닫기
    closeBtn.addEventListener('click', closeModal);

    // 모달 배경(오버레이) 영역 클릭 시 모달 닫기
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // ESC 키 누를 시 모달 닫기
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}