# Generated by Django 5.1.3 on 2024-11-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review_on_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
