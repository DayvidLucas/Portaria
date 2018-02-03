# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *

class OnibusAdmin(admin.ModelAdmin):
   # form = OnibusForm eoq
    list_display= ['nome','empresa','trajeto','entrada']
    search_fields = ['nome','empresa','trajeto']

admin.site.register(Onibus, OnibusAdmin)