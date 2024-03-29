# Generated by Django 2.2.3 on 2019-12-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_activeporduct_active_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeporduct',
            name='height_des',
            field=models.TextField(blank=True, help_text='高度描述', null=True, verbose_name='HeightDes'),
        ),
        migrations.AddField(
            model_name='activeporduct',
            name='material_des',
            field=models.TextField(blank=True, help_text='材质描述', null=True, verbose_name='MaterialDes'),
        ),
        migrations.AddField(
            model_name='activeporduct',
            name='thickness_des',
            field=models.TextField(blank=True, help_text='厚度描述', null=True, verbose_name='ThicknessDes'),
        ),
    ]
