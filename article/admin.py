from django.contrib import admin

from .models import Article,Comment
# Register your models here.
#özellştirmeler yapcaz burda
admin.site.register(Comment)#şimdi migrate alcaz


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author","created_date"]

    list_display_links = ["title", "created_date"]#oluşturma tarhine de basınca içeriği görebilecek duruma gelmek için link ekledik
    
    search_fields = ["title"]#titlebilgisine göre arama özelliği eklemiş olduk
    
    list_filter = ["created_date"] # oluşturulma tarihi süzgecine göre 
    class Meta:
        model = Article