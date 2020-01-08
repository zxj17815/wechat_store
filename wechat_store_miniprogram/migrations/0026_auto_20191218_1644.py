# Generated by Django 2.2.3 on 2019-12-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0025_auto_20191211_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='wechatoreder',
            name='receive_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='ReceiveTime'),
        ),
        migrations.AlterField(
            model_name='apptoken',
            name='expires_in',
            field=models.DateTimeField(default='2019-12-18 16:44:10', verbose_name='expires_in'),
        ),
        migrations.AlterField(
            model_name='wechatoreder',
            name='state',
            field=models.IntegerField(choices=[(0, '待付款'), (1, '待发货'), (2, '待确认'), (3, '退货中'), (4, '退款中'), (5, '已完成'), (6, '确认收货')], default=0, help_text='int，订单状态', verbose_name='State'),
        ),
    ]
