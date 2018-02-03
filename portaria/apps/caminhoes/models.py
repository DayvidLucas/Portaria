# -*- coding: utf-8 -*-
from django.db import models

class Caminhoes(models.Model):
    numero = models.CharField(
        max_length=4,
        verbose_name=u"Nº")
    
    placa = models.CharField(
        max_length=7,
        verbose_name=u'placa')
    
    mod = models.CharField(
        max_length=7,
        verbose_name=u'Mod')
    
    motorista = models.CharField(
        max_length=50,
        verbose_name=u'Motorista')

    placa = models.CharField(
        max_length=7,
        verbose_name=u'placa')
    
    entrada = models.DateTimeField(verbose_name=u"Hora de entrada")

    saida = models.DateTimeField(
        verbose_name = u"Hora de saida",
        blank=True, null=True)

    observacao = models.TextField(
        verbose_name=u"Observação",
        blank=True, null=True)

    def __str__(self):
        return self.motorista

    class Meta:
        verbose_name=u"Caminhão"
        verbose_name_plural=u"Caminhões"
