from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import qrcode
from PIL import Image
from django.contrib.auth.models import User
esfn = []
fsfn = []

# Create your models here.
class Spaceship(models.Model):
    name = models.CharField(max_length=250)
    image_path = models.ImageField(upload_to='Spaceship')
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Spaceship"

    def __str__(self):
        return str(f"{self.name}")


    def save(self, *args, **kwargs):
        super(Spaceship, self).save(*args, **kwargs)
        print(self.image_path)
        if not self.image_path == '':
            imag = Image.open(self.image_path.path)
            width = imag.width
            height = imag.height
            if imag.width > 640:
                perc = (width - 640) / width
                width = 640
                height = height - (height * perc)
            if imag.height > 480:
                perc = (height - 480) / height
                height = 480
                width = width - (width * perc)
            output_size = (width, height)
            imag.thumbnail(output_size)
            imag.save(self.image_path.path)

    def delete(self, *args, **kwargs):
        super(Spaceship, self).delete(*args, **kwargs)
        storage, path = self.image_path.storage, self.image_path.path
        storage.delete(path)
        
class Spaceport(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Spaceports"

    def __str__(self):
        return str(f"{self.name}")

class Shuttles(models.Model):
    code = models.CharField(max_length=250)
    airline = models.ForeignKey(Spaceship, on_delete=models.CASCADE)
    from_Spaceport = models.ForeignKey(Spaceport, on_delete=models.CASCADE, related_name="From_Spaceport")
    to_Spaceport = models.ForeignKey(Spaceport, on_delete=models.CASCADE, related_name="To_Spaceport")
    air_craft_code = models.CharField(max_length=250)
    departure = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    business_class_slots = models.IntegerField(default=0)
    economy_slots = models.IntegerField(default=0)
    business_class_price = models.FloatField(default=0)
    economy_price = models.FloatField(default=0)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Shuttles"

    def __str__(self):
        return str(f"{self.code} [{self.from_Spaceport.name} - {self.to_Spaceport.name}]")

    def b_slot(self):
        try:
            number = Bookings.objects.exclude(status = 2).filter(flight=self, type = 1).count()
            if number is None:
                number = 0

        except:
            number = 0
        dhruva = self.business_class_slots - number
        if dhruva < 0:
            dhruva = 0
        
        fsfn.append(dhruva)
        return dhruva


    def e_slot(self):
        try:
            number = Bookings.objects.exclude(status = 2).filter(flight=self, type = 2).count()
            if number is None:
                number = 0

        except:
            number = 0

        dhruva2 = self.business_class_slots - number
        if dhruva2 < 0:
            dhruva2 = 0
        esfn.append(dhruva2)
        return dhruva2

        
class Bookings(models.Model):
    flight = models.ForeignKey(Shuttles, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=(('1','Business Class'), ('2','Economy')), default = '2')
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=(('Male','Male'), ('Female','Female')), default = 'Male')
    email = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    address = models.TextField()
    status = models.CharField(max_length=2, choices=(('0','Pending'),('1','Confirmed'), ('2','Cancelled')), default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Bookings"

    def __str__(self):
        return str(f"{self.flight.code} - {self.first_name} {self.last_name}")
    
    def name(self):
        return str(f"{self.last_name}, {self.first_name} {self.middle_name}")

        
class Subscriber(models.Model):
    email = models.EmailField(null = True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email

class Transport(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    address = models.TextField()
    ship_type = models.CharField(max_length=50, choices=(('1','Millenium Falcon'), ('2','Milano'),('3','Enterprise')), default = '1')
    weight = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Transport"


    def __str__(self):
        return self.first_name + ' ' + self.last_name

        