# Generated by Django 4.2.3 on 2023-07-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_product_delete_apprash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promo_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
