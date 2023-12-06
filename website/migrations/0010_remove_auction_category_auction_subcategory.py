# Generated by Django 4.2.7 on 2023-12-06 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_auction_category_auction_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='category',
        ),
        migrations.AddField(
            model_name='auction',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.subcategory'),
        ),
    ]
