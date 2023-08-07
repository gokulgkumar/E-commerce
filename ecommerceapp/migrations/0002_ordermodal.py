# Generated by Django 4.2.3 on 2023-08-03 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=250)),
                ('Product_name', models.CharField(max_length=250)),
                ('Quantity', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=250)),
                ('Phone_Number', models.CharField(max_length=250)),
                ('Order_date', models.DateField(auto_now_add=True)),
                ('Cart_Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.customermodal')),
                ('Cart_Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.productmodal')),
            ],
        ),
    ]
