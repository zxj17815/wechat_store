# Generated by Django 2.2.3 on 2019-11-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0016_auto_20191125_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpackge',
            name='order',
        ),
        migrations.RemoveField(
            model_name='refundpackge',
            name='refund',
        ),
        migrations.AddField(
            model_name='refund',
            name='refund_packge',
            field=models.ManyToManyField(help_text='[int]，外键-RefundPackge', to='wechat_store_miniprogram.RefundPackge', verbose_name='RefundPackge'),
        ),
        migrations.AddField(
            model_name='wechatoreder',
            name='product_packge',
            field=models.ManyToManyField(help_text='[int]，外键-models.Model', to='wechat_store_miniprogram.OrderPackge', verbose_name='Product'),
        ),
    ]