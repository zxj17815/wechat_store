# Generated by Django 2.2.3 on 2019-11-14 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0006_refund_refundpackge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpackge',
            name='is_refund',
        ),
        migrations.RemoveField(
            model_name='orderpackge',
            name='refund_count',
        ),
    ]
