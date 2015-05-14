from django.conf.urls import patterns,include,url
from . import views


urlpatterns = patterns('',
        # url(r'^test/',views.post_list),
        # url(r'^$',views.post_list),
        url(r'^hello',views.hello),
        url(r'^url',views.current_url_view_good),
        # url(r'^search_form',views.search_form),
        url(r'^search/',views.search),
        url(r'^contact/',views.contact),
        url(r'^thanks',views.thanks),
)
