# Generated by Django 5.0.7 on 2024-07-24 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['done', '-creation_date']},
        ),
    ]
