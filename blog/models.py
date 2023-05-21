from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь создавший пост', null=True, blank=True)
    title=models.CharField(verbose_name='Заголовок', max_length=255,default='', null=True, blank=True)
    text=models.TextField(verbose_name='Описание')
    date_post=models.DateTimeField(default=timezone.now, verbose_name='Дата создания поста')

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

    def __str__(self) -> str:
        return self.title

class AboutUs(models.Model):
    whatsapp_url=models.URLField(max_length=250, verbose_name='чат в Whatsapp')
    telegram_url=models.URLField(max_length=250, verbose_name='чат в Telegram')
    text_aboutus=models.TextField(verbose_name='Описание о нас')
    
    class Meta:
        verbose_name='AboutUs'
        verbose_name_plural='AboutUs'

    def __str__(self) -> str:
        return self.text_aboutus
# Create your models here.
