from django.contrib import admin
from Ele import views
from django.conf.urls import patterns, include, url
from Ele.views import Data
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Elena.views.home', name='home'),
    # url(r'^Elena/', include('Elena.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	(r'^admin/', include(admin.site.urls)),
	(r'^Ingresando_datos/$', 'Ele.views.Ingresando_datos'),
	(r'^buscar/$', 'Ele.views.Buscar'),
	url(r'^data/$', views.Data.as_view(), name='data'),
	url(r'^(?P<dato_id>\d+)/$', views.qu, name='qu'),
		
		
)
