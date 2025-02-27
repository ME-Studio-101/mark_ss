function initHorizontalScrollSpy() {
    const scrollContainers = document.querySelectorAll('.spy_horizontal_scrollable');

    function handleScroll(event) {
        const parent = event.target;
        const parentX = parent.getBoundingClientRect().x;
        const items = parent.querySelectorAll('.horizontal_scrollable_item');
        
        if (items.length === 0) return;

        const positions = [];
        const spyId = parent.getAttribute('data-target');
        
        if (!spyId) return;

        const spyLinks = document.querySelectorAll(`${spyId} .spy_link`);

        items.forEach((item, index) => {
            const itemX = item.getBoundingClientRect().x;
            positions[index] = itemX;

            if (spyLinks[index]) {
                spyLinks[index].classList.remove('active');
            }
        });

        const closestIndex = positions.reduce((prev, curr, index) => 
            Math.abs(curr - parentX) < Math.abs(positions[prev] - parentX) ? index : prev, 0);

        if (spyLinks[closestIndex]) {
            spyLinks[closestIndex].classList.add('active');
        }
    }

    scrollContainers.forEach((container) => {
        const events = ['scroll', 'touchmove', 'touchend'];
        
        events.forEach(eventType => {
            container.addEventListener(eventType, handleScroll, { passive: true });
        });

        handleScroll({ target: container, type: 'initial' });
    });
}

window.initHorizontalScrollSpy = initHorizontalScrollSpy;

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHorizontalScrollSpy);
} else {
    initHorizontalScrollSpy();
}
initHorizontalScrollSpy();