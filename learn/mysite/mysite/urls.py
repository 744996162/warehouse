from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import *
import blog
import book

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^blog/', include('blog.urls')),
    url(r'^book/', include('book.urls')),
    # url(r'^url/',current_url_view_good),
    url(r'^url/', ua_display_goood1),
    url(r'^brower_info/', display_meta),
)
