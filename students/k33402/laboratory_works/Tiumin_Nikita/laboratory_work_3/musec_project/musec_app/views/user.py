
from rest_framework.decorators import api_view, authentication_classes
from musec_app.auth.authentication import AppTokenAuthentication
from musec_app.responses import api_response
from musec_app.serializers import UserSerializer


@api_view(['GET'])
@authentication_classes([AppTokenAuthentication])
def me(request):
    return api_response.payload(UserSerializer(request.user, context={'profile': True}).data)
