# Generated by Django 4.1.2 on 2022-10-27 06:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_course_created_at_course_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]