# Generated by Django 5.0.1 on 2024-01-05 11:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0002_alter_category_options_blog"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="Category",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="blog",
            old_name="update_At",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="creates_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="update_at",
            new_name="updated_at",
        ),
    ]