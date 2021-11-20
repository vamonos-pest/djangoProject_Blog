from django.db import models

class Post(models.Model):
    title = models.CharField('Тема', max_length=255)
    post = models.TextField('Описание')
