# Generated by Django 2.2.3 on 2019-11-11 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20191111_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='file_url',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.CharField(default='', help_text='上传图片路径及文件名', max_length=50, verbose_name='Image'),
            preserve_default=False,
        ),
    ]
