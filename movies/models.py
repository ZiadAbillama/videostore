from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

CURRENT_YEAR = datetime.date.today().year

class Movie(models.Model):
    # They explicitly want a MovieID field; make it the primary key so no extra id is created.
    MovieID = models.CharField(max_length=20, primary_key=True)

    MovieTitle   = models.CharField(max_length=200)
    Actor1Name   = models.CharField(max_length=120, blank=True)
    Actor2Name   = models.CharField(max_length=120, blank=True)
    DirectorName = models.CharField(max_length=120, blank=True)

    GENRE_CHOICES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Horror', 'Horror'),
        ('Other', 'Other'),
    ]
    MovieGenre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='Other')

    ReleaseYear = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(CURRENT_YEAR)]
    )

    def _str_(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"