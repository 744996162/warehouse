__author__ = 'Administrator'
# python manage.py shell
from django import template

t=template.Template("My name is {{name}}.")
c=template.Context({"name":"zhangchao"})
print t.render(c)

def test1():

    pass

