from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.CharField(max_length =200)
    date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Images_image = models.ImageField(upload_to = 'images/')
    

    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.dele
        
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image 
     
     
    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image
     
     
    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return image 
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
  
    def __str__(self):
        return self.name 
     
class Location(models.Model):
    name = models.CharField(max_length=60)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category = models.CharField(max_length =100)

    @classmethod
    def get_all_categories(cls):
        '''
        Method to get all categories
        '''
        categories = cls.objects.all()
        return categories

    def save_category(self):
        '''
        Method to save category
        '''
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()
    
    def __str__(self):
        return self.category
    
