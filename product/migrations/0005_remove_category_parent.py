# Generated by Django 4.1.5 on 2023-02-06 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_subcategory_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
