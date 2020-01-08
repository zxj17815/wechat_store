# Generated by Django 2.2.3 on 2019-11-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0019_auto_20191125_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='re_extra',
            field=models.TextField(default='', help_text='答复信息', verbose_name='ReExtra'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='refund',
            name='state',
            field=models.IntegerField(choices=[(0, '待通过'), (1, '待退货'), (2, '待确认'), (3, '已完成'), (4, '未通过')], default=0, help_text='int，状态', verbose_name='State'),
        ),
    ]