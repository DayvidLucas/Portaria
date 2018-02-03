# -*- coding: utf-8 -*-
from django.db import models

class Notas(models.Model):
    
    placa = models.CharField(
        max_length=7,
        verbose_name=u"Placa")
    
    motorista = models.CharField(
        max_length=50,
        verbose_name=u"Motorista")
    
    empresa = models.CharField(
        max_length=50,
        verbose_name=u"Empresa")

    produto = models.CharField(
        max_length=50,
        verbose_name=u"Produto")

    nota = models.CharField(
        max_length=15,
        verbose_name=u"Nota Fiscal")

    entrega = models.DateTimeField(verbose_name=u"Hora da entrega")

    entrada = models.DateTimeField(verbose_name=u"Hora de Entrada")

    saida = models.DateTimeField(
        verbose_name = u"Hora de saida",
        blank=True, null=True)

    observacao = models.TextField(
        verbose_name=u"Observação",
        blank=True, null=True)

    def __str__(self):
        return self.motorista

    
    class Meta:
        verbose_name=u"Nota"
        verbose_name_plural=u"Notas"
    