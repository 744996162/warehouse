from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
import MySQLdb
from models import Book
from contact.forms import ContactForm
# Create your views here.

def hello(request):
    return HttpResponse("hello zhangchao,this is book page")

def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

def ua_display_good1(request):
    ua=request.META['HTTP_USER_AGENT']
    return HttpResponse("Welcome to the page at %s" % request.path)


def book_list1(request):
    db=MySQLdb.connect(user="root",db="mysite",passwd="root",host="localhost")
    cursor=db.cursor()
    cursor.execute("select name from books order by name ")
    names=[row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html',{'name':names})
    pass


# def book_list(request):
#     books=Book.objects.order_by('name')
#     return render_to_response('book_list.html',{'books':books})
#     pass

# def search_form(request):
#     return render_to_response("search_form.html")

def search(request):
    errors = []
    if "q" in request.GET:
        q = request.GET["q"]
        if not q:
            errors.append("Enter a search term.")
        elif len(q)>20:
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__contains=q)
            return render_to_response("search_result.html",{"books":books,"query":q})
            # message = "You searched for : %r" %request.GET["q"]
    else:
        return  render_to_response("search_form.html",{"errors":errors})
        # return HttpResponse("You submitted an empty form")

def contact1(request):
    errors = []
    if request.method == "post":
        if not request.POST.get("subject",""):
            errors.append("Enter a subject")
        if not request.POST.get("email",""):
            errors.append("Enter a email")
        if request.POST.get("email") and "@" not in request.POST["email"]:
            errors.append("Enter a valid e-mail address.")
        if not errors:
            send_mail(
            request.POST["subject"],
            request.POST["message"],
            request.POST.get("email","784412595@qq.com"),
            ["784412595@qq.com"],
            )
            return HttpResponseRedirect("thanks/")

    return render_to_response("contact_form.html",{"errors":errors,
                                                   "subject":request.POST.get("subject",""),
                                                   "message":request.POST.get("message",""),
                                                   "email":request.POST.get("email",""),
                                                   })

def thanks(request):
    return HttpResponse("Thanks for your contact" )
    pass

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd["subject"],
                cd["message"],
                cd.get("email","784412595@qq.com"),
                ["744996162@qq.com"],
            )
            return HttpResponseRedirect("/book/thanks")
    else:
        form = ContactForm()
    return render_to_response("contact_form.html",{"form":form})
    pass

