from django.db import models

# Create your models here.
class Director(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Cast(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class NewArrival(models.Model):
    img=models.ImageField(upload_to='')
    title=models.CharField(max_length=30)
    director=models.ForeignKey(Director,on_delete=models.CASCADE)
    casting=models.ForeignKey(Cast,on_delete=models.CASCADE,default=True)
    
    #ratings=
    
    class Meta:
        ordering = ['-title']
    
    def __str__(self):
        return self.title
    
    
    
