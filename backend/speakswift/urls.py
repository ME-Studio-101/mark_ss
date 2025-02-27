from django.urls import path
from . import views


urlpatterns = [
    # Стартовая страница
    path("", views.index, name='index'),
    path('index-mobile/', views.index_mobile, name='index-mobile'),
    path('index-mobile-additional/', views.index_mobile_additional, name='index-mobile-additional'),
    path('index-tablet/', views.index_tablet, name='index-tablet'),
    path('index-tablet-additional/', views.index_tablet_additional, name='index-tablet-additional'),
    path('index-desktop/', views.index_desktop, name='index-desktop'),
    path('index-desktop-additional/', views.index_desktop_additional, name='index-desktop-additional'),

    # Курс 1 - Занятия для детей
    path('course1/', views.course1, name='course1'),
    # path('course1/course1form/', views.course1form, name='course1form'),

    # Курс 2 - Курс интенсив
    path('course2/', views.course2, name='course2'),
    # path('course2/course2form/', views.course2form, name='course2form'),
    
    # Курс 3 - Индивидуальные занятия
    path('course3/', views.course3, name='course3'),
    # path('course3/course3form/', views.course3form, name='course3form'),
    
    # Курс 4 - Курсы английского
    path('course4/', views.course4, name='course4'),
    # path('course4/course4form/', views.course4form, name='course4form'),
    
    # О нас
    path('about/', views.about, name='about'),

    # Тест на уровень английского языка
    path("test1/", views.test1, name='test1'),
    path("test-results/", views.test_results, name='test_results'),

    # Отправка формы
    path('form_handler/', views.form_handler, name='form_handler'),
]