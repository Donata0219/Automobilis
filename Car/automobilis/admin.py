from django.contrib import admin

# Register your models here.
from django.contrib import admin
from automobilis.models import Automobilis
class Automobiliu_lentele(admin.TabularInline):
    model = Automobilis
    readonly_fields = ['duration', 'genre', 'release_date']
    can_delete = False

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = [ ]

    list_filter = []
    search_fields = []
admin.site.register(Automobilis, AutomobilisAdmin )