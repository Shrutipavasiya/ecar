from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
#$ pip install django-ckeditor
from ckeditor_uploader.fields import RichTextUploadingField

from multiselectfield import MultiSelectField
#$ pip install django-multiselectfield

# Create your models here.

class Car(models.Model):
    #A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
    #The basics:
    #Each model is a Python class that subclasses django.db.models.Model.
    #Each attribute of the model represents a database field.
    #With all of this, Django gives you an automatically-generated database-access API

    state_choice = (
        ('GJ', 'Gujarat'),
        ('MH', 'Maharashtra'),
        ('RJ', 'Rajasthan'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )


    years_choice=[]
    for r in range(2000, (datetime.now().year+1)):
        years_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title=models.CharField(max_length=255)
    state=models.CharField(choices=state_choice, max_length=100)
    city= models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField(('year'), choices=years_choice)
    condition = models.CharField(max_length=100)
    price= models.IntegerField()
    description= RichTextField()
    car_photo= models.ImageField(upload_to='photos/%Y/%m/%d/')
    # pip install Pillow
    #For example, say your MEDIA_ROOT is set to '/home/media', and upload_to is set to 'photos/%Y/%m/%d'.
#The '%Y/%m/%d' part of upload_to is strftime formatting.

#%Y is the four-digit year.
#%m is the two-digit month.
#%d is the two-digit day.
#If you upload a file on Jan. 15, 2007, it will be saved in the directory /home/media/photos/2007/01/15.

    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features= MultiSelectField(choices=features_choices)
    body_style= models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission= models.CharField(max_length=100)
    interior=models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured= models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
