from rest_framework import generics, status
from rest_framework.serializers import Serializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend


from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

# Clase para la correcta visualizacion del usuario y el update
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION")[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT["ALGORITHM"])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data["user_id"] != kwargs["pk"]:
            stringResponse = {"detail": "Unauthorized Request"}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)
