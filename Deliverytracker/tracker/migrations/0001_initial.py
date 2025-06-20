# Generated by Django 5.2.2 on 2025-06-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('customer_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('T', 'In Transit'), ('D', 'Delivered')], default='P', max_length=1)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
