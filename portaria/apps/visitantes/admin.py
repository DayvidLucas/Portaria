# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *

class VisitantesAdmin(admin.ModelAdmin):
   # form = VisitantesForm
    list_display= ['nome','empresa','entrada']
    search_fields = ['nome','empresa','entrada']

admin.site.register(Visitante, VisitantesAdmin)
