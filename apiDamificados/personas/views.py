# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Personas
from .serializers import PeopleGetName,PersonasCreationSerlializer,TodosSerializer2

from django.shortcuts import render

# Create your views here.

class PersonasApi(APIView):

	def get(self, request):
		people = Personas.objects.all()
		serializer = PeopleGetName(people, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		print(request.data)
		serializer = TodosSerializer2(data=request.data)
		print(serializer)
		print(serializer.is_valid())
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






