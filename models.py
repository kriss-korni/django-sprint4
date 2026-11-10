
"""Модели блога: категории, местоположения и публикации."""

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class PublishedModel(models.Model):
    """Абстрактная модель общих полей публикации."""

    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )

    class Meta:
        """Настройки абстрактной модели."""

        abstract = True


class Category(PublishedModel):
    """Категория публикаций."""

    title = models.CharField(
        'Заголовок',
        max_length=256,
    )
    description = models.TextField(
        'Описание',
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=(
            'Идентификатор страницы для URL; разрешены '
            'символы латиницы, цифры, дефис и подчёркивание.'
        ),
    )

    class Meta:
        """Настройки отображения категории."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Возвращает заголовок категории."""
        return self.title


class Location(PublishedModel):
    """Местоположение, связанное с публикациями."""

    name = models.CharField(
        'Название места',
        max_length=256,
    )

    class Meta:
        """Настройки отображения местоположения."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        """Возвращает название местоположения."""
        return self.name


class Post(PublishedModel):
    """Публикация в блоге."""

    title = models.CharField(
        'Заголовок',
        max_length=256,
    )
    text = models.TextField(
        'Текст',
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='posts',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
        related_name='posts',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='posts',
    )

    image = models.ImageField(
        'Изображение',
        upload_to='posts_images/',
        blank=True,

    )

    class Meta:
        """Настройки отображения публикации."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        """Возвращает заголовок публикации."""
        return self.title
class Comment(models.Model):
    """Модель для комментариев к публикациям."""
    text = models.TextField('Текст комментария')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )

    class Meta:
        """Настройки отображения комментариев."""
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created_at',)  

    def __str__(self):
        return self.text[:20]
