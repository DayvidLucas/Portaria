# -*- coding: utf-8 -*-
from django.db import models

class Funcionarios(models.Model):
    
    nome = models.CharField(
        max_length=7,
        verbose_name=u"Nome")
    
    horario = models.DateTimeField(verbose_name=u"Horário")
    
    entrada = models.DateTimeField(verbose_name=u"Hora de Entrada")

    saida_almoco = models.DateTimeField(verbose_name=u"Saida do Almoço")

    volta_almoco = models.DateTimeField(verbose_name=u"Volta do Almoço")


    saida = models.DateTimeField(verbose_name=u"Horário de saida")


    def __str__(self):
        return self.nome

    
    class Meta:
        verbose_name=u"Funcionario"
        verbose_name_plural=u"Funcionarios"