from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    # Отключение ненужных полей родительской модели
    first_name = None
    last_name = None
    email = None
    is_active = None
    last_login = None
    date_joined = None
    groups = None
    user_permissions = None

    LEVELS = (
        ("Ребенок", "Ребенок"),
        ("Студент", "Студент"),
        ("Человек", "Человек"),
        ("Говорящий", "Говорящий"),
        ("Преподаватель", "Преподаватель"),
    )

    CONTACT_TYPES = (
        ("Telegram", "Telegram"),
        ("WhatsApp", "WhatsApp"),
        ("email", "email"),
        ("Telegram", "Telegram"),
        ("Telegram", "Telegram"),
    )

    name = models.CharField(
        "Имя",
        blank=False,
        null=False,
        max_length=150,
    )
    contact_type = models.CharField(
        "Уровень владения языком", choices=LEVELS, default="Человек", max_length=64
    )
    email = models.EmailField(
        "Адрес электронной почты",
        unique=True,
        blank=False,
        null=False,
        max_length=254,
    )
    level = models.CharField(
        "Уровень владения языком", choices=LEVELS, default="Человек", max_length=64
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
