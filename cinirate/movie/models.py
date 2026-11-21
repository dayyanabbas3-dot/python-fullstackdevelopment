from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)   
    poster = models.ImageField(
        upload_to='posters/',
        blank=True,
        verbose_name='Poster image',
    )
    poster_url = models.URLField(
        blank=True,
        verbose_name='Poster URL (optional)',
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews_set'
    )
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - ({self.rating})"
# Create your models here.
