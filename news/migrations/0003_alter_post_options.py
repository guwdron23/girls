# Generated by Django 4.1.4 on 2022-12-15 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_author_alter_post_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
