document.addEventListener('DOMContentLoaded', function() {
    function getResponsiveVars(prefix) {
        const width = window.innerWidth;
        const isSmallScreen = width <= 575;
        const isMediumScreen = width > 575 && width <= 991;
        const scrollAmount = isSmallScreen ? width : (isMediumScreen ? 768 : 1440);


        return {
            scrollAmount: scrollAmount,
            scroll: `${prefix}scroll${isSmallScreen ? '-sm' : ''}`,
            scrollLeftVar: `${prefix}scroll_left${isSmallScreen ? '-sm' : ''}`,
            scrollRightVar: `${prefix}scroll_right${isSmallScreen ? '-sm' : ''}`
        };
    }

    function setupScrollHandlers(prefix) {
        const { scroll, scrollLeftVar, scrollRightVar, scrollAmount } = getResponsiveVars(prefix);
        const scrollElement = document.getElementById(scroll);
        const scrollLeftElement = document.getElementById(scrollLeftVar);
        const scrollRightElement = document.getElementById(scrollRightVar);

        if (!scrollElement || !scrollLeftElement || !scrollRightElement) {
            console.warn(`Required elements not found for prefix: ${prefix}`);
            return;
        }

        const updateScrollButtons = () => {
            const { scrollLeft, scrollWidth, clientWidth } = scrollElement;
            scrollLeftElement.parentElement.classList.toggle('inactive', scrollLeft === 0);
            scrollRightElement.parentElement.classList.toggle('inactive', scrollLeft + clientWidth >= scrollWidth);
        };

        updateScrollButtons();
        scrollElement.addEventListener('scroll', updateScrollButtons);

        [scrollLeftElement, scrollRightElement].forEach((element, index) => {
            element.addEventListener('click', event => {
                event.preventDefault();
                scrollElement.scrollBy({
                    left: index === 0 ? -scrollAmount : scrollAmount,
                    behavior: 'smooth'
                });
            });
        });
    }

    function initHorizontalScrollButtons() {
        ['adv_',].forEach(setupScrollHandlers);
    }

    initHorizontalScrollButtons();
});