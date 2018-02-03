# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *

class CaminhoesAdmin(admin.ModelAdmin):
   # form = CaminhoesForm
    list_display= ['motorista','placa','observacao']
    search_fields = ['motorista','placa']

admin.site.register(Caminhoes, CaminhoesAdmin)