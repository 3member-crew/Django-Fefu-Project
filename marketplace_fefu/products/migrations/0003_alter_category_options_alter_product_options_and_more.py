# Generated by Django 4.2.7 on 2023-11-11 15:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_vendor_delete_user'),
        ('products', '0002_category_remove_product_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['ordering'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-add_date']},
        ),
        migrations.AddField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='change_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='product', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='users.vendor'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=55),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
