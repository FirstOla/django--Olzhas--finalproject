# Generated by Django 4.2.1 on 2023-05-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp_url', models.URLField(max_length=250, verbose_name='чат в Whatsapp')),
                ('telegram_url', models.URLField(max_length=250, verbose_name='чат в Telegram')),
                ('text_aboutus', models.TextField(verbose_name='Описание о нас')),
            ],
            options={
                'verbose_name': 'AboutUs',
                'verbose_name_plural': 'AboutUs',
            },
        ),
    ]
