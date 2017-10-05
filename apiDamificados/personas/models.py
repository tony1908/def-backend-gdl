# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

SEXOS = (("M","Mujer"),("H","Hombre"),("I","Indefinido"))
TIPOSPERSONAS = (("Voluntario","Voluntario"),("Danmificado","Danmificado"),("Otro","Otro"))
# Create your models here.

class Personas(models.Model) :
	nombre = models.CharField(max_length=100)
	edad = models.IntegerField(max_length=3)
	sexo = models.CharField(choices=SEXOS, max_length=5)
	tipo_de_persona = models.CharField(choices=TIPOSPERSONAS, max_length=50)
