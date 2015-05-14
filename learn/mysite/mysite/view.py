__author__ = 'Administrator'
from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return HttpResponse("hello zhangchao.")


def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s hours(s), it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)

def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" %request.get_full_path())


def ua_display_goood1(request):
    try:
        ua = request.META["HTTP_USER_AGENT"]
    except KeyError:
        ua = "unknown"
    return HttpResponse("Your brower is %s." %ua)

def ua_display_goood2(request):
    ua = request.META.get("HTTP_USER_AGENT","unknow")
    return HttpResponse("Your brower is %s." %ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    list_k = []
    list_v = []
    for k, v in values:
        html.append("<tr><td>%s</td></tr>%s</td></tr>" %(k, v))
        list_k.append(k)
        list_v.append(v)
    return HttpResponse(values)


