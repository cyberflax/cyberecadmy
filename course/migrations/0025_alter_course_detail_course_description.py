# Generated by Django 3.2.7 on 2022-02-01 06:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_crs_review_crs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_detail',
            name='course_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
