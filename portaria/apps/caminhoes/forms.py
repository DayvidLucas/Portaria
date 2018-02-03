# -*- coding: utf-8 -*-
from django import forms
import datetime
from .models import*

class CaminhoesForm(forms.ModelForm):
    entrada = forms.DateTimeField()
    saida = forms.DateTimeField()


    def clean_entrada(self):
        entrada = self.cleaned_data['entrada']
        saida = self.cleaned_data['saida']

        if entrada < datime.now:
            raise forms.ValidationError(
                "A data não pode ser menor que a data atual!"
            )
        elif entrada > saida:
            raise forms.ValidationError(
                "A data de entrada não pode ser depois da data de saida"
            )
        return entrada

    def clean_sainda(self):
        entrada = self.cleaned_data['entrada']
        saida = self.cleaned_data['saida']

        if saida > datime.now:
            raise forms.ValidationError(
                "A hora de hora/data de saida não pode ser maior que a atual!"
            )
        elif saida < entrada:
            raise forms.ValidationError(
                "A data de saida não pode ser menor que a de entrada"
            )
        return entrada

    class Meta:
        model = Caminhoes
        exclude = ('pk',)