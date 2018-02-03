# -*- coding: utf-8 -*-
from django.db import models

class Onibus(models.Model):
    
    TRAJETO_CHOICES = (
        ('MP', 'Mendes x Pirai'),
        ('PB', 'Pirai x B.Pirai'),
        ('BP', 'B.Pirai x Pirai'),
        ('MP', 'Mendes x Pirai'),
        ('PM', 'Pirai x Mendes'),
    )

    nome = models.CharField(
        verbose_name="Nome",
        max_length=50)
    
    empresa = models.CharField(
        verbose_name="Empresa",
        max_length=50)

    trajeto = models.CharField(
        verbose_name="Trajeto",
        max_length=2, choices=TRAJETO_CHOICES)

    passageiro = models.IntegerField(
        verbose_name="Passageiros (qnt)",
        max_length=4)

    placa = models.CharField(
        verbose_name="Placa",
        max_length=7)

    entrada = models.DateTimeField(verbose_name=u"Chegada")

    saida = models.DateTimeField(
        verbose_name = u"Hora de saida",
        blank=True, null=True)

    observacao = models.TextField(
        verbose_name=u"Observação",
        blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name=u"Onibus"
        verbose_name_plural=u"Onibus"
