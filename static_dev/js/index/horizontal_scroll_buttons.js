function getResponsiveVars(prefix) {
    const width = window.innerWidth;
    const isSmallScreen = width <= 575;
    const isMediumScreen = width > 575 && width <= 991;
    const scrollAmount = isSmallScreen ? width - width * 0.04348 : (isMediumScreen ? 400 : 600);

    const scrollLeftVar = `${prefix}scroll_left${isSmallScreen ? '_sm' : ''}`;
    const scrollRightVar = `${prefix}scroll_right${isSmallScreen ? '_sm' : ''}`;

    console.log(`getResponsiveVars called with prefix: ${prefix}`, { scrollAmount, scrollAmount, scrollLeftVar, scrollRightVar });

    return {
        scrollAmount: scrollAmount,
        scroll: `${prefix}scroll${isSmallScreen ? '_sm' : ''}`,
        scrollLeftVar: scrollLeftVar,
        scrollRightVar: scrollRightVar
    };
}

function setupScrollHandlers(prefix) {
    console.log(`setupScrollHandlers called with prefix: ${prefix}`);
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
        scrollRightElement.parentElement.classList.toggle('inactive', scrollLeft + clientWidth + 1 >= scrollWidth);
        console.log('Scroll buttons updated:', { scrollLeft, scrollWidth, clientWidth });
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
    console.log('Initializing horizontal scroll buttons');
    ['lf_', 'um_'].forEach(setupScrollHandlers);
}