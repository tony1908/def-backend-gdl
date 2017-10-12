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

	def create(self, validated_data):
		return Personas.objects.create(**validated_data)

class PersonasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personas
		fields = '__all__'
		# fields = ['nombre','edad','sexo','tipo_de_persona','id']

class PersonasModifieSerliazer(serializers.Serializer) :
	tipo_de_persona = serializers.CharField(max_length=50)

	# def create(self, validated_data):
	# 	return Personas.objects.create(**validated_data)

	# def update(self, instance, validated_data):
	# 	instance.tipo_de_persona = validated_data.get('tipo_de_persona', instance.tipo_de_persona)
	# 	return instance

# class PersonasSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Personas
# 		# fields = '__all__'
# 		fields = ('nombre','edad','sexo','tipo_de_persona')
