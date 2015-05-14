from django.contrib import admin
from .models import Publisher
from .models import Book
from .models import Author



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    pass

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')
    pass

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields=("title","authors",'publisher','publication_date')


# Register your models here.
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)