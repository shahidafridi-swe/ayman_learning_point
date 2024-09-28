from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract = True

class StudentProfile(Profile):
    LEVEL_CHOICE = (
        ('one','One'),
        ('two','Two'),
        ('three','Three'),
        ('four','Four'),
        ('five','Five'),
        ('six','Six'),
        ('seven','Seven'),
        ('eight','Eight'),
        ('nine','Nine'),
        ('ten','Ten'),
        ('eleven','Eleven'),
        ('twelve','Twelve'),
    )
    level = models.CharField(max_length=10, choices=LEVEL_CHOICE)
    enrollment_level = models.CharField(max_length=10,blank=True, null=True)
    enrollment_date = models.DateField()
    school = models.CharField(max_length=255)

class TeacherProfile(Profile):
    subject = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    bio = models.CharField(max_length=255)
    
class StaffProfile(Profile):
    domain = models.CharField(max_length=50)
    
    
    
    

