from django.db import models

# Create your models here.
GENDER_CHOICE = (
    ('M', 'MALE'),
    ('F', 'FEMALE')
)
class Student(models.Model):
    Name = models.CharField(help_text='name', max_length=100)
    Gender = models.CharField(help_text='gender', max_length=100, choices=GENDER_CHOICE)
    Email = models.EmailField(help_text='email')
    Program = models.CharField(help_text='program', max_length=100)
    Room = models.CharField(help_text='room number', max_length=100)
    Image = models.ImageField(verbose_name='image', upload_to='images')

    def __str__(self):
        return self.Name
    