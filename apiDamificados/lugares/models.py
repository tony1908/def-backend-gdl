# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from personas.models import Personas

STATUS = (("1","Actual"),("0","Ya no"))

class Lugares(models.Model) :
	calle = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	colonia = models.CharField(max_length=100)

class PersonasHasLugares(models.Model):
	fecha = models.DateField()
	status = models.CharField(choices=STATUS, max_length=20)
	lugares_id = models.ForeignKey(Lugares)
	personas_id = models.ForeignKey(Personas)