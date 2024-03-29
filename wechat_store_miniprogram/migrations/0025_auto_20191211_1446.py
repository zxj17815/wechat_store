# Generated by Django 2.2.3 on 2019-12-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0024_auto_20191210_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderexpress',
            name='type',
            field=models.IntegerField(choices=[(0, '手工下单'), (1, '物流助手下单')], default=0, help_text='int，下单类型', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='apptoken',
            name='expires_in',
            field=models.DateTimeField(default='2019-12-11 14:46:20', verbose_name='expires_in'),
        ),
        migrations.AlterField(
            model_name='wechatoreder',
            name='state',
            field=models.IntegerField(choices=[(0, '待付款'), (1, '待发货'), (2, '待确认'), (3, '退货中'), (4, '退款中'), (5, '已完成')], default=0, help_text='int，订单状态', verbose_name='State'),
        ),
    ]
