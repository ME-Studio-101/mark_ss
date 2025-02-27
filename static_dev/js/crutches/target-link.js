
document.querySelectorAll('.h-active_link').forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Отключение перехода по ссылке
    });

    link.addEventListener('mouseover', function(event) {
        event.stopPropagation(); // Отключение наведения
    });
});