import os
from django.core.management.base import BaseCommand
from schoolapp.models import School, Pincode

class Command(BaseCommand):
    help = 'Adds dummy data to the School and Pincode models'

    def handle(self, *args, **options):
        file_path = 'schoolapp/data/dummy_data.txt' 
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split(',')
                pincode_code = data[0].strip()
                school_name = data[1].strip()
                school_address = data[2].strip()

               
                pincode, created = Pincode.objects.get_or_create(code=pincode_code)
                if not School.objects.filter(name=school_name, address=school_address, pincode=pincode).exists():
                    
                    School.objects.create(name=school_name, address=school_address, pincode=pincode)

            self.stdout.write(self.style.SUCCESS('Dummy data added successfully!'))
        else:
            self.stdout.write(self.style.ERROR(f"File '{file_path}' does not exist."))
