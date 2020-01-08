# Generated by Django 2.2.3 on 2019-11-11 00:39

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivePorduct',
            fields=[
                ('id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='string，产品名称', max_length=150, verbose_name='Name')),
                ('series', models.TextField(help_text='text，系列', verbose_name='Series')),
                ('height', models.IntegerField(choices=[(0, 'NO Show'), (1, 'Tab'), (2, 'Low'), (3, 'Quarter'), (4, 'Crew'), (5, 'Boot'), (6, 'Over the Calf')], help_text='int，高度', verbose_name='Height')),
                ('thickness', models.IntegerField(choices=[(0, 'thin'), (1, 'mid'), (2, 'thick')], help_text='int，厚度', verbose_name='Thickness')),
                ('material', models.TextField(help_text='text，材质', verbose_name='Material')),
                ('price', models.FloatField(help_text='float，商品价格', verbose_name='Price')),
                ('describe', models.TextField(help_text='text，详情描述', verbose_name='Describe')),
                ('start_time', models.DateTimeField(help_text='datetime，活动开始时间', verbose_name='StartTime')),
                ('end_time', models.DateTimeField(help_text='datetime，活动结束时间', verbose_name='EndTime')),
                ('state', models.IntegerField(choices=[(0, 'close'), (1, 'open')], default=0, help_text='int，状态（0：关闭；1：启用）', verbose_name='State')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='CreateTime')),
                ('edit_time', models.DateTimeField(auto_now=True, null=True, verbose_name='EditTime')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('file_name', models.CharField(help_text='上传图片文件名', max_length=50, verbose_name='FileName')),
                ('image', models.URLField(help_text='上传图片', verbose_name='Image')),
                ('request_id', models.CharField(max_length=250, verbose_name='RequestId')),
                ('etag', models.CharField(max_length=250, verbose_name='Etag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='string，Color名称', max_length=100, verbose_name='Name')),
                ('active_porduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ActivePorduct', verbose_name='ActivePorduct')),
                ('images', models.ManyToManyField(help_text='[int]，外键-Image，商品图片', to='store.Image', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('size', models.IntegerField(choices=[(0, 'XS'), (1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL'), (5, 'XXXL')], help_text='int，Size大小', verbose_name='Size')),
                ('quantity', models.IntegerField(help_text='int，库存量', verbose_name='Quantity')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ProductColor', verbose_name='ProductColor')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.IntegerField(choices=[(0, 'unknown'), (1, 'admin'), (2, 'weuser'), (3, 'other')], default=1, help_text='用户类型', verbose_name='UserType')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
