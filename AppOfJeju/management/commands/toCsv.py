from django.core.management.base import BaseCommand
import csv
from AppOfJeju.models import CropMarketData

class Command(BaseCommand):
    help = 'Export CropMarketData to CSV'

    def handle(self, *args, **options):
        with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer=csv.writer(csvfile)
            # CSV 헤더 작성
            writer.writerow(['id', 'crop_type', 'supplier', 'crop_date', 'crop_supply', 'crop_price'])

            # CropMarketData 모델 인스턴스를 순회하며 데이터 작성
            for data in CropMarketData.objects.all():
                writer.writerow([data.id, data.crop_type, data.supplier, data.crop_date, data.crop_supply, data.crop_price])