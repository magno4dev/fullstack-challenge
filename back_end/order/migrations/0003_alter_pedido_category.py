# Generated by Django 4.0.4 on 2022-05-17 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_pedido_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='order.category'),
        ),
    ]
