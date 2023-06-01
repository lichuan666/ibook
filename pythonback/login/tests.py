from django.test import TestCase
from models import Student
# Create your tests here.

def mytestStudent():
    student1 = Student.objects.create(name='AAA', password='123456', phone='12345678900', email='tom@example.com',
                                      photo='Student/photo/tom.jpg')
