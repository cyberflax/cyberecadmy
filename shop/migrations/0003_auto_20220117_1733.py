# Generated by Django 3.2.7 on 2022-01-17 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_shop_detail_product_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_detail',
            old_name='about_shop',
            new_name='about_product',
        ),
        migrations.RenameField(
            model_name='product_detail',
            old_name='shop_description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='product_detail',
            old_name='shop_img',
            new_name='product_img',
        ),
        migrations.RenameField(
            model_name='product_detail',
            old_name='shop_price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='product_detail',
            old_name='shop_sku',
            new_name='product_sku',
        ),
        migrations.RenameField(
            model_name='product_detail',
            old_name='shop_tag',
            new_name='product_tag',
        ),
        migrations.RenameField(
            model_name='product_detail',
            old_name='shop_title',
            new_name='product_title',
        ),
    ]
