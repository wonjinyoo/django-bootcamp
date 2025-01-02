import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProThird.settings')
django.setup()

from AppThird.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakegen.email()

        # Putting new entry
        # user = User.objects.get_or_create(fname=fake_fname,
        #                                   lname=fake_lname,
        #                                   email=fake_email)[0]
        
        User.objects.create(fname=fake_fname,
                            lname=fake_lname,
                            email=fake_email)
        
if __name__ == '__main__':
    print("Populating databases")
    populate(20)
    print("Complete")