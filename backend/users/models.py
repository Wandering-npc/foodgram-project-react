from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from validators import validate_username


class User(AbstractUser):

    email = models.EmailField(
        max_length=254,
        verbose_name='Эл. почта',
        unique=True,
        blank=False,
        null=False
    )
    username = models.CharField(
        validators=(validate_username,),
        max_length=150,
        verbose_name='Имя пользователя',
        null=False,
        unique=True,
        blank=False,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=25,
        null=False,
        blank=False
    )
    last_name = models.TextField(
        verbose_name='Фамилия',
        null=False,
        blank=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_is_not_me'
            )
        ]


class Follow(CreatedModel):
    """Модель подписки."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name='unique_follow'
            )
        ]


  
