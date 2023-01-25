# Generated by Django 4.1.5 on 2023-01-25 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_name_alter_customer_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='product.category'),
        ),
    ]
