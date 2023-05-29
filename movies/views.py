from rest_framework.views import APIView, Response, status
from .serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .permissions import MoviePermission
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieOrderSerializer


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviePermission]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        # added_by = {"added_by": request.user.email}

        # return_data = {, **added_by}

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):

        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, request, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
    

class MovieViewId(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviePermission]
    
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, 404)
        
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, 404)

        movie.delete()

        return Response(status=204)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, 404)
        
        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, movie=movie)

        title = {"title": movie.title}

        buyed_by = {"buyed_by": request.user.email}

        return_data = {**serializer.data, **title, **buyed_by}

        return Response(return_data, status.HTTP_201_CREATED)
