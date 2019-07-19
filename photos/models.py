from django.db import models

# Create your models here.

class Location(models.Model):
    Loc_name = models.CharField(max_length =30)

    def __str__(self):
        return self.Loc_name

    def save_Location(self):
        self.save()

class Category(models.Model):
    Cat_name = models.CharField(max_length =30)

    def __str__(self):
        return self.Cat_name

    def save_category(self):
        self.save()
        

class Image(models.Model):
    Img_name = models.CharField(max_length =30)
    Img_description = models.CharField(max_length =200)
    image = models.ImageField(upload_to = 'photos/')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    

    def __str__(self):
        return self.Img_name

    def save_Img(self):
        self.save()
    