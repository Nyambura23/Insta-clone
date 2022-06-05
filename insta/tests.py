from django.test import TestCase
from .models import Image, Comment, Profile, Like

# Create your tests here.

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Pic= Image(id = '1', image = 'example.jpg', name = 'bianca', caption ='Viva la vida', user ='bianca', location ='Timbuktu')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pic,Image)) 
    
     # Testing Save Method
    def test_save_method(self):
        self.Pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
        
    def test_delete_method(self):
        self.Pic.delete_location()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)    
        
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= Profile(id = '1', profile_photo = 'example.jpg', bio = 'Hola amigo', user ='bianca')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,Profile)) 
    
     # Testing Save Method
    def test_save_method(self):
        self.Prof.save_profile()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
        
    def test_delete_method(self):
        self.Prof.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)           
        
class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Comm= Comment(id = '1', image = 'example.jpg', comment = 'Wauuuu', user ='bianca')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Comm,Comment))         

class LikeTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Lik= Like(id = '1', image = 'example.jpg', liker ='bianca')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Lik,Like))                 