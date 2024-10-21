from django.contrib import admin
from test_app.models.articles import Articles
from test_app.models.articlesTypeMaster import ArticlesTypeMaster

# Register your models here.

class ArticlesModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'is_public', 'type', 'created_at', 'updated_at')

class ArticlesTypeMasterModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

admin.site.register(Articles, ArticlesModelAdmin)

admin.site.register(ArticlesTypeMaster, ArticlesTypeMasterModelAdmin)