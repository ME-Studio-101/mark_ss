// Решение для обновления страницы с релоадом всего контента, ибо на телефоне этого нельзя просто так сделать
// Работает через присвение кнопкам или ссылкам класса refresh-link
function refreshWithCacheBusting() {
  var currentUrl = window.location.href;
  var newUrl = currentUrl.split('?')[0] + '?cache_bust=' + new Date().getTime();
  window.location.replace(newUrl);
}

function setupRefreshLinks() {
  var refreshLinks = document.querySelectorAll('.refresh-link');
  if (refreshLinks.length > 0) {
    refreshLinks.forEach(function (link) {
      link.addEventListener('click', function (event) {
        event.preventDefault(); // Предотвращаем переход по ссылке
        refreshWithCacheBusting();
      });
    });
  } else {
    console.error('No elements found with class "refresh-link"');
  }
}

document.addEventListener('DOMContentLoaded', setupRefreshLinks);