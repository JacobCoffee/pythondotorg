# Generated by Django 4.2.11 on 2024-03-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minutes', '0003_alter_minutes_creator_alter_minutes_last_modified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
