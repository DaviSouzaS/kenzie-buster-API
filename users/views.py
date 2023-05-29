from rest_framework.views import APIView, Response, status
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission
from .models import User


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserViewId(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, 404)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, 404)

        serializer = UserSerializer(user, request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)