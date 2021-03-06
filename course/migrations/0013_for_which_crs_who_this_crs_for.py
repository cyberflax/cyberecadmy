# Generated by Django 3.2.7 on 2022-01-28 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20220120_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='who_this_crs_for',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crs', models.CharField(max_length=1000)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='for_which_crs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='crs', to='course.course_detail')),
                ('title', models.ManyToManyField(to='course.who_this_crs_for')),
            ],
        ),
    ]
