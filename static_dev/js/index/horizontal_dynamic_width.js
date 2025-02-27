function updateMinWidth() {
    const width = window.innerWidth;
    let ssContainerWidth;

    if (width <= 575) {
        ssContainerWidth = 575;
    } else if (width > 575 && width <= 991) {
        ssContainerWidth = 768;
    } else {
        ssContainerWidth = 1440;
    }

    const margin = (width - ssContainerWidth) / 2;
    document.documentElement.style.setProperty('--hs-cases-start-end-min-width', `${margin}px`);
}

window.addEventListener('load', updateMinWidth);

window.addEventListener('resize', updateMinWidth);