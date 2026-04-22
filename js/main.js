/**
 * 파일명: main.js
 * 기능: 웹사이트 전체의 주요 UI 상호작용 관리
 */

document.addEventListener('DOMContentLoaded', () => {
    initSmoothScroll();
});

/**
 * 네비게이션 메뉴 클릭 시 해당 섹션으로 부드럽게 스크롤하는 함수
 */
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            
            // 클릭한 링크의 href 값 (예: #section-projects) 가져오기
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}