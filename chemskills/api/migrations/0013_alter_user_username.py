# Generated by Django 4.2.3 on 2023-12-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_user_classrooms_alter_user_current_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=32, unique=True),
        ),
    ]
