# Generated by Django 4.1.5 on 2023-02-13 15:23

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='clothes_size',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shoe_size',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44')], max_length=20, null=True),
        ),
    ]
