# Generated by Django 2.2.3 on 2019-11-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20191111_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.CharField(help_text='上传图片路径及文件名', max_length=50, verbose_name='Image'),
        ),
    ]
