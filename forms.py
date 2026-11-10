from django import apps
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования публикаций."""

    class Meta:
        model = Post
        # Указываем, какие поля из модели Post показывать пользователю в форме
        fields = ('title', 'text', 'pub_date', 'location', 'category', 'image')
        # Меняем вид поля даты на удобный календарь
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
from .models import Comment

class CommentForm(forms.ModelForm):
    """Форма для добавления комментариев."""

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),  # Делаем поле компактным, на 3 строчки
        }
