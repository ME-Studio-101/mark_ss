// Костыль для починки ебнутого респонсива, завязанного на абсолютных значениях всего
// Динамически меняет initial-scale базового html документа
function setInitialScale() {
    var viewport = document.querySelector('meta[name="viewport"]');
    if (!viewport) {
      viewport = document.createElement('meta');
      viewport.name = 'viewport';
      document.head.appendChild(viewport);
    }

    var screenWidth = screen.width;
    var initialScale;

    if (screenWidth < 576) {
      initialScale = screenWidth / 575;
    } else if (screenWidth >= 576 && screenWidth <= 767) {
      initialScale = screenWidth / 768;
    } else if (screenWidth >= 768 && screenWidth <= 991) {
      initialScale = 1.0;
    } else if (screenWidth >= 992 && screenWidth <= 1440) {
      initialScale = screenWidth / 1440;
    } else {
      initialScale = 1.0;
    }

    viewport.setAttribute('content', 'width=device-width, initial-scale=' + initialScale);
  }

  window.addEventListener('load', setInitialScale); // Установить при загрузке
  window.addEventListener('resize', setInitialScale); // Обновить при изменении размера окна