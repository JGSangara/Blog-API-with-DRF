# Generated by Django 4.1.4 on 2023-01-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
