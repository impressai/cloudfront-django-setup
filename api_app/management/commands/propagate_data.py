import os
import json

from django.conf import settings
from django.core.management import BaseCommand, CommandError
from api_app.serializers import HttpDogModelSerializer

class Command(BaseCommand):
    help = "Propagate Data"

    def handle(self, *args, **options):
        try:
            filename = 'scripts/status-codes.json'
            file = os.path.join(settings.BASE_DIR, filename)
            with open(file, 'r') as f:
                json_text = f.read()
                dict_status_codes = json.loads(json_text)
            http_dog_serializer = HttpDogModelSerializer(data=dict_status_codes, many=True)
            http_dog_serializer.is_valid(raise_exception=True)
            http_dog_serializer.save()
            self.stdout.write("Data Propagated")
        except Exception as ex:
            raise CommandError('Error {}'.format(str(ex)))
