from django.core.management.base import BaseCommand           
from hammar.main import dailyRun

class Command(BaseCommand):
    def handle(self, *args, **options):         
	dailyRun()

