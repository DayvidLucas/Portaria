# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *

class FuncionariosAdmin(admin.ModelAdmin):
    #form = FuncionariosForms
    list_display= ['nome','saida_almoco','volta_almoco']
    search_fields = ['nome']
    

admin.site.register(Funcionarios, FuncionariosAdmin)