# Generated by Django 4.1.7 on 2023-02-26 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cartproduct_alter_cart_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartproduct',
            options={'ordering': ['cart']},
        ),
    ]
