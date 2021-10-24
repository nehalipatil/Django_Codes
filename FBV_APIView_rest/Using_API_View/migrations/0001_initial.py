# Generated by Django 3.2.7 on 2021-10-12 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'CategoryAV',
            },
        ),
        migrations.CreateModel(
            name='VendorAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=10, unique=True)),
                ('category_av', models.ManyToManyField(related_name='vendor', to='Using_API_View.CategoryAV')),
            ],
            options={
                'db_table': 'VendorAV',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=10, unique=True)),
                ('category_av', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='Using_API_View.categoryav')),
            ],
            options={
                'db_table': 'SubCategoryAV',
            },
        ),
        migrations.CreateModel(
            name='DeliveryAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Delivery_Address', models.TextField()),
                ('category_av', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='Using_API_View.categoryav')),
            ],
            options={
                'db_table': 'DeliveryAV',
            },
        ),
    ]