# Generated by Django 2.1.7 on 2019-02-15 13:28

from django.db import migrations


def create_first_version(apps, schema_editor):
    Version = apps.get_model("ncdr", "Version")
    Version.objects.create()


def remove_versions(apps, schema_editor):
    Version = apps.get_model("ncdr", "Version")
    Version.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("ncdr", "0004_add_version")]

    operations = [
        migrations.RunPython(create_first_version, reverse_code=remove_versions)
    ]