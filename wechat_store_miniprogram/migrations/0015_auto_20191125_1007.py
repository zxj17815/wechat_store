# Generated by Django 2.2.3 on 2019-11-25 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechat_store_miniprogram', '0014_auto_20191122_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refund',
            name='refund_packge',
        ),
        migrations.RemoveField(
            model_name='wechatoreder',
            name='product_packge',
        ),
        migrations.AddField(
            model_name='orderpackge',
            name='order',
            field=models.ForeignKey(default='', help_text='int，外键-WeChatOreder', on_delete=django.db.models.deletion.CASCADE, related_name='product_packge', to='wechat_store_miniprogram.WeChatOreder', verbose_name='WeChatOreder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refundpackge',
            name='refund',
            field=models.ForeignKey(default='', help_text='int，外键-Refund', on_delete=django.db.models.deletion.CASCADE, related_name='refund_packge', to='wechat_store_miniprogram.Refund', verbose_name='Refund'),
            preserve_default=False,
        ),
    ]
