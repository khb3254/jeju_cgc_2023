from django.core.management.base import BaseCommand, CommandError
from AppOfJeju.models import PredictionData
import csv
from datetime import datetime

class Command(BaseCommand):
    help = 'Load a list of crops from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type = str, help = 'The CSV file path')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        with open(csv_file_path, newline='', encoding = 'utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                crop_date = datetime.strptime(row['timestamp'], '%Y-%m-%d').date()
                PredictionData.objects.create(
                    crop_type=row['item'],
                    supplier=row['corporation'],
                    origin=row['location'],
                    crop_date=crop_date,
                    crop_price=float(row['price']),
                    ai_model="RandomForest"
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded RandomForest output data'))