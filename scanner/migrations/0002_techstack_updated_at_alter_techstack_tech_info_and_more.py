# Generated by Django 4.1.7 on 2023-03-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='techstack',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='techstack',
            name='tech_info',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='techstack',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
