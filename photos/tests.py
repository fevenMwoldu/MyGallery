from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.asmara= Location(Loc_name = 'Asmara')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.asmara,Location))

    # Testing Save Method
    def test_save_method(self):
        self.asmara.save_Location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.city= Category(Cat_name = 'City')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.city,Category))

    # Testing Save Method
    def test_save_method(self):
        self.city.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.asmara= Location(Loc_name = 'Asmara')
        self.asmara.save_Location()

        # Creating a new category and saving it
        self.new_cat = Category(name = 'testing')
        self.new_cat.save()

        self.new_image= Image(Img_name = 'Asmara',Img_description = 'It is a beautiful city',image="/home/feven/Documents/Django/My-gallery/media/photos/Eritrea_2012_0430107671-e1516381677957.jpg")
        self.new_image.save()

        self.new_image.Category.add(self.new_cat)

        def tearDown(self):
            Location.objects.all().delete()
            Category.objects.all().delete()
            Image.objects.all().delete()
