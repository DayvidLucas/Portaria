# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *

class NotasAdmin(admin.ModelAdmin):
    #form = NotasForm
    list_display= ['motorista','empresa','produto','nota','observacao']
    search_fields = ['placa','motorista','empresa','nota','produto']
    

admin.site.register(Notas, NotasAdmin)