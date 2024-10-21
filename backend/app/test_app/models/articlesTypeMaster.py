from django.db import models

# Create your models here.
class ArticlesTypeMaster(models.Model):
    class Meta:
        db_table = 'articles_type_master'


    name = models.CharField(
        '名前',
        max_length=20,
        null=False,
        blank=False,
    )

    code = models.CharField(
        'コード',
        max_length=8,
        null=False,
        blank=False,
        unique=True,
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

