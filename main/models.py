from django.db import models

class Post(models.Model):
    title = models.CharField('Тема', max_length=255)
    post = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'