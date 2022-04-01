# Generated by Django 3.2.7 on 2021-12-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Reklamin adi')),
                ('image', models.ImageField(upload_to='advertisement_image/', verbose_name='Image')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('is_top', models.BooleanField(default=False, verbose_name='Top Advertisement')),
                ('is_bottom', models.BooleanField(default=False, verbose_name='Bottom Adverstiment')),
                ('is_right', models.BooleanField(default=False, verbose_name='Right Advertisement')),
                ('is_left', models.BooleanField(default=False, verbose_name='Left Advertisement')),
                ('pages', models.CharField(blank=True, choices=[('Main Page', 'Əsas Səhife'), ('About Page', 'Haqqimizda'), ('All Brands Page', 'Butun Markalar'), ('Brand', 'Marka'), ('All Models Page', 'Butun Modeller'), ('Car Detail Page', 'Esas Kateqoriyalar'), ('Car Filter Page', 'Orta Kateqoriyalar'), ('Contact Page', 'Kontakt Sehifesi'), ('Inner Details Page', 'Ic Detallar'), ('Searched Products', 'Axtarilan Detallar'), ('Shops Page', 'Maqazinler'), ('Sub Parts Page', 'Ic Kateqoriyalar'), ('Wish List Page', 'Arzu Listi Sehifesi'), ('Change Password Page', 'Sifreni Deyisme Sehifesi'), ('Forget Password Page', 'Sifreni Unutdum Sehifesi'), ('Login Page', 'Hesaba Daxil Olmaq'), ('Reset Password Page', 'Sifreni Yenilemek'), ('Register Page', 'Registrasiyadan Kecmek'), ('Self Profile', 'Profil Sehifesi'), ('User Profile', 'Basqa Userin Profili'), ('Add Product', 'Product Elave Etmek'), ('Filtered Product', 'Filtrlenmis Detallar'), ('Products Page', 'Productlar Sehifesi'), ('Sale Product', 'Endirimde Olan Mehsullar'), ('Single Produt', 'Productun Sehifesi'), ('Update Product', 'Productun Duzelis Sehifesi')], max_length=50, null=True, verbose_name='Sehifeler')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Reklam Banneri',
                'verbose_name_plural': 'Reklam Bannerleri',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('phone_number', models.PositiveIntegerField(verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'Our Contact',
                'verbose_name_plural': 'Our Contacts',
            },
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Basligi')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_az', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_ru', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='marka_image', verbose_name='Image')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Marka',
                'verbose_name_plural': 'Markalar',
            },
        ),
        migrations.CreateModel(
            name='Modell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Basligi')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_az', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_ru', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='model_image', verbose_name='Image')),
                ('is_parent', models.BooleanField(default=False, verbose_name='esas model')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Modeller',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Arzu Listi',
                'verbose_name_plural': 'Arzu Listleri',
            },
        ),
    ]
