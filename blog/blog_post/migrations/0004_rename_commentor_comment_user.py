# Generated by Django 4.1 on 2024-07-11 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0003_blog_post_likes_delete_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentor',
            new_name='user',
        ),
    ]
