from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Název žánru",
                            help_text='Zadejte žánr seriálu(např. sci-fi, komedie)')

    class Meta:
        ordering = ["name"]
        permissions = (("can_add_genres", "Create a new genre"), ("can_delete_genres", "Delete a genre"),
                       ("can_update_genres", "Update a genre"),)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Jméno režiséra", help_text="Zadejte jméno režiséra.")

    class Meta:
        ordering = ["name"]
        permissions = (("can_add_directors", "Create a new directors"), ("can_delete_directors", "Delete a directors"),
                       ("can_update_directors", "Update a directors"),)

    def __str__(self):
        return self.name


class Serial(models.Model):
    name = models.CharField(max_length=150, verbose_name="Název seriálu", help_text='Zadejte název seriálu.')
    genre = models.ManyToManyField(Genre, help_text="Vyberte žánr seriálu.")
    director = models.ManyToManyField(Director, help_text="Vyberte režiséra seriálu.")
    date = models.DateField(default="1.1.2021", verbose_name="Datum vydání", help_text="Zadejte datum vydání seriálu.")
    series = models.IntegerField(blank=True, null=True, verbose_name="Počet sérií", help_text="Zadejte počet kapitol.")
    rate = models.FloatField(default=5.0, validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], null=True,
                             help_text="Zadejte hodnocení od 1.0 - 10.0", verbose_name="Hodnocení")

    class Meta:
        ordering = ["date", "name"]
        permissions = (("can_add_serials", "Create a new serial"), ("can_delete_serials", "Delete a serial"),
                       ("can_update_serials", "Update a serials"),)

    def __str__(self):
        return f"{self.name}, Rok vydání: {str(self.date.year)}, Hodnocení: {str(self.rate)}"

    def get_absolute_url(self):
        return reverse('serial-detail', args=[str(self.id)])
