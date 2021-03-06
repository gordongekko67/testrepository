from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post,Articoli,Clienti,Titoli

admin.site.site_url = "/base"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Articoli)
class ArticoliAdmin(admin.ModelAdmin):
    list_display = ('codart', 'codslug', 'codauthor', 'codpublish', 'codstatus')


@admin.register(Clienti)
class ClientiAdmin(admin.ModelAdmin):
    list_display = ('codcli', 'codslugcli', 'codauthorcli', 'codpublishcli', 'codstatuscli')


@admin.register(Titoli)
class TitoliAdmin(admin.ModelAdmin):
    list_display = ('codtit', 'codslugtit', 'codisintit', 'codbodytit', 'codmintit', 'codmaxtit')





