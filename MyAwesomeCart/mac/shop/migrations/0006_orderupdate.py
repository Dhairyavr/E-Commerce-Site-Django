# Generated by Django 3.0.4 on 2020-04-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=100)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
