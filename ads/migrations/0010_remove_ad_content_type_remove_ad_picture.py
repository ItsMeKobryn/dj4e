# Generated by Django 4.2.7 on 2024-10-28 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0009_ad_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ad",
            name="content_type",
        ),
        migrations.RemoveField(
            model_name="ad",
            name="picture",
        ),
    ]
