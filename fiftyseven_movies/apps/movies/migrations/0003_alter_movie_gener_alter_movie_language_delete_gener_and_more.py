# Generated by Django 4.1.5 on 2023-01-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='gener',
            field=models.CharField(max_length=80, verbose_name='Gener name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=80, verbose_name='Language name'),
        ),
        migrations.DeleteModel(
            name='Gener',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
