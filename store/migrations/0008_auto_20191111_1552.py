# Generated by Django 2.2.3 on 2019-11-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20191111_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.URLField(help_text='上传图片路径及文件名', verbose_name='Image'),
        ),
    ]
