from django.contrib import admin

# Register your models here.
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','created_at','updated_at','is_pudlished')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_pudlished',)
    list_filter = ('is_pudlished','category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category,CategoryAdmin)
