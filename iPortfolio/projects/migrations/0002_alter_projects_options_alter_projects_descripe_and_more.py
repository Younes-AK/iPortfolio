# Generated by Django 5.0.6 on 2024-07-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'project'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='descripe',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]