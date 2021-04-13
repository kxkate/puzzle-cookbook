from django.core.management.base import BaseCommand, CommandError
from cookbook.models import Ingredient
import csv
import json
import pandas
from collections import OrderedDict


class Command(BaseCommand):
    help = 'Downloads ingredient data from top-1k-ingredients database'

    def handle(self, *args, **options):
        # df = pandas.read_csv('static/cookbook/top-1-ingredients.csv', names=("ingredient_name", "id", "Song", "Album"))

