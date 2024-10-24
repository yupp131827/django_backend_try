# Generated by Django 4.2.16 on 2024-10-21 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesTypeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('code', models.CharField(max_length=8, unique=True, verbose_name='コード')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'db_table': 'articles_type_master',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='名前')),
                ('code', models.CharField(max_length=8, unique=True, verbose_name='コード')),
                ('img', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='画像')),
                ('text', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='本文')),
                ('is_public', models.BooleanField(default=False, verbose_name='公開フラグ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_app.articlestypemaster', verbose_name='記事タイプ')),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
