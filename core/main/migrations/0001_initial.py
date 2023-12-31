# Generated by Django 4.2.5 on 2023-09-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Notebook name')),
                ('price', models.PositiveIntegerField(verbose_name='Notebook Price')),
                ('img', models.ImageField(upload_to='images', verbose_name='Notebook image')),
            ],
        ),
    ]
