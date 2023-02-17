from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','nomi','company','date','url','malumot','tur','rasm1']

admin.site.register(Portfolio,AdminPortfolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Type,AdminType)


class AdminMurojat(admin.ModelAdmin):
    list_display = ['id','nomi','mail','title','text','date']
admin.site.register(Murojat,AdminMurojat)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','ismi','lavozimi','malumot','twitter','facebook','instagram','inn','rasm']

admin.site.register(Team,AdminTeam)