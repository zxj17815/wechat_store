# Generated by Django 2.2.3 on 2019-11-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0013_refund_out_refund_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='out_refund_no',
            field=models.CharField(blank=True, help_text='string，退款单号', max_length=50, null=True, verbose_name='OutRefundNo'),
        ),
    ]
