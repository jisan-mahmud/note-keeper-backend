# Generated by Django 5.1.6 on 2025-03-09 07:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AddField(
            model_name='notes',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
