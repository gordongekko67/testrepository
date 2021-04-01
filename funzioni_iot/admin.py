from django.contrib import admin

# Register your models here.
from .models import Titoli2, Question, Giornalista, Cliente

admin.site.register(Question)
admin.site.register(Giornalista)
admin.site.register(Cliente)


@admin.register(Titoli2)
class TitoliAdmin(admin.ModelAdmin):
    list_display = ('codtit2', 'codslugtit2', 'codisintit2', 'codbodytit2', 'codmintit2', 'codmaxtit2')


"""
@admin.register(Giornalista)
class GiornalistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codcli', 'descli')
"""