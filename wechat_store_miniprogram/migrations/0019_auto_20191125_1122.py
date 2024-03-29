# Generated by Django 2.2.3 on 2019-11-25 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0018_auto_20191125_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refund',
            name='refund_packge',
        ),
        migrations.AddField(
            model_name='refundpackge',
            name='refund',
            field=models.ForeignKey(default='', help_text='int，外键-Refund', on_delete=django.db.models.deletion.CASCADE, related_name='refund_packge', to='wechat_store_miniprogram.Refund', verbose_name='Refund'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderpackge',
            name='order',
            field=models.ForeignKey(help_text='int，外键-WeChatOreder', on_delete=django.db.models.deletion.CASCADE, related_name='order_packge', to='wechat_store_miniprogram.WeChatOreder', verbose_name='WeChatOreder'),
        ),
    ]
