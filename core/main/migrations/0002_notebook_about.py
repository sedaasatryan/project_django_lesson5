# Generated by Django 4.2.5 on 2023-09-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='about',
            field=models.TextField(default=1, verbose_name='Notebook description'),
            preserve_default=False,
        ),
    ]
