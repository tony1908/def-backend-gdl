from django.conf.urls import url
from .views import PersonasApi, PersonaApi
# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	url(r'^$', PersonasApi.as_view(), name='personas_all'),
	url(r'^(?P<pk>[0-9]+)/$', PersonaApi.as_view(), name="persona_endpoint"),
	# url(r'^api-token-auth/', obtain_jwt_token),
]