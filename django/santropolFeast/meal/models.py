from django.db import models
from django.utils.translation import ugettext_lazy as _

ALLERGY_CHOICES = (
    ('Tomato', _('Tomato')),
    (('Milk'), _('Milk')),
    (('Peanut'), _('Peanut'))
)


class Meal(models.Model):
    REGULAR = 'R'
    LARGE = 'L'

    SIZE = (
        (REGULAR, _('Regular')),
        (LARGE, _('Large')),
    )

    class Meta:
        verbose_name_plural = _('meals')

    # Meal information
    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )
    description = models.TextField(verbose_name=_('description'))
    size = models.CharField(
        max_length=1,
        choices=SIZE,
        default=REGULAR
    )
    ingredients = models.ManyToManyField(
        'meal.Ingredient',
        related_name='meals'
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    class Meta:
        verbose_name_plural = _('ingredients')

    # Ingredient information
    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )

    def __str__(self):
        return self.name


class Allergy(models.Model):

    class Meta:
        verbose_name_plural = _('allergies')

    # Allergy information
    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )
    description = models.TextField(verbose_name=_('description'))
    ingredients = models.ManyToManyField(
        'meal.Ingredient',
        related_name='allergies'
    )

    def __str__(self):
        return self.name


class Menu(models.Model):

    class Meta:
        verbose_name_plural = _('menus')

    # Menu information
    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )

    date = models.DateField(verbose_name=_('date'))

    ingredients = models.ManyToManyField(
        'meal.Ingredient',
        related_name='menus'
    )

    def __str__(self):
        return self.name
