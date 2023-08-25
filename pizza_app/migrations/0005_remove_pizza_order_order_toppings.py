# Generated by Django 4.2.4 on 2023-08-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0004_remove_order_toppings_pizza_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='topping_orders', to='pizza_app.pizza'),
        ),
    ]