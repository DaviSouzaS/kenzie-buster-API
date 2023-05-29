from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(default=False)
    order_movies = models.ManyToManyField(Movie, through="movies.MovieOrder", related_name="user_orders")
