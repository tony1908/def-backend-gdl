from rest_framework import serializers
from .models import Personas


def validar_edad(source):
	if source <= 100:
		pass
	else:
		raise serializers.ValidationError("No hay nadie mayor a 100")
		pass

class PeopleGetName(serializers.Serializer):
	nombre = serializers.CharField(max_length=100)

class PersonasCreationSerlializer(serializers.Serializer) :
	nombre = serializers.CharField(max_length=100)
	edad = serializers.IntegerField(validators=[validar_edad])
	sexo = serializers.CharField(max_length=5)
	tipo_de_persona = serializers.CharField(max_length=50)

class PersonasModifieSerliazer(serializers.Serializer) :
	tipo_de_persona = serializers.CharField(max_length=50)

class TodosSerializer2(serializers.ModelSerializer):
	class Meta:
		model = Personas
		# fields = '__all__'
		fields = ('nombre','edad','sexo', 'tipo_de_persona')
