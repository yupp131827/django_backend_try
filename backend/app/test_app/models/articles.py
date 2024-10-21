from django.db import models
from test_app.models.articlesTypeMaster import ArticlesTypeMaster


# Create your models here.
class Articles(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(
        '名前',
        max_length=20,
        null=True,
        blank=True,
        default='',
    )

    code = models.CharField(
        'コード',
        max_length=8,
        null=False,
        blank=False, 
        unique=True,
    )

    img = models.CharField(
        '画像',
        max_length=1000,
        null=True,
        blank=True,
        default='',
    )

    text = models.CharField(
        '本文',
        max_length=500,
        null=True,
        blank=True,
        default='',
    )

    is_public = models.BooleanField(
        '公開フラグ',
        default=False,
    )

    type = models.ForeignKey(
        ArticlesTypeMaster,
        verbose_name='記事タイプ',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        '作成日時',
        auto_now_add=True,
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        '更新日時',
        auto_now=True,
        null=False,
        blank=False,
    )

