# -*- coding: utf-8 -*-
from django.db import models

class Visitante(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100)
    
    empresa = models.CharField(
        verbose_name="Empresa",
        max_length=100)

    autorizado = models.CharField(
        verbose_name="Autorizado por",
        max_length=100)

    setor = models.CharField(
        verbose_name="Setor Visitado",
        max_length=100)

    placa = models.CharField(
        verbose_name="Placa",
        max_length=100)

    entrada = models.DateTimeField(verbose_name=u"Hora de entrada")

    saida = models.DateTimeField(
        verbose_name = u"Hora de saida",
        blank=True, null=True)

    observacao = models.TextField(
        verbose_name=u"Observação",
        blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name=u"Visitante"
        verbose_name_plural=u"Visitantes"






