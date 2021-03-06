# Generated by Django 3.2.7 on 2022-01-18 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0006_rename_course_duration_course_detail_course_duration_in_weeks'),
    ]

    operations = [
        migrations.CreateModel(
            name='crs_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
