__author__ = 'Administrator'
from books.models import  Publisher

p1=Publisher(name='Addison-Wesley', address='75 Arlington Street',city='Boston', state_province='MA', country='U.S.A.',website='http://www.apress.com/')

publisher_list = Publisher.objects.all()
