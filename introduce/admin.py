from django.contrib import admin
from .models import Introduce

# Register your models here.


@admin.register(Introduce)
class IntroduceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','hobby','like_it']
    list_display_links = ['name']
