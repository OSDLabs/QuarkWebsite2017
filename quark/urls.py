from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^speakers/$', 'home.views.speakers', name='speakers'),
    url(r'^exhibits/$', 'home.views.exhibits', name='exhibits'),
    url(r'^nites/$', 'home.views.nites', name='nites'),
    url(r'^team/$', 'home.views.team', name='team'),
    url(r'^about/$', 'home.views.about', name='about'),
    url(r'^ca/$', 'home.views.ca', name='ca'),
    url(r'^sponsor/$', 'home.views.sponsor', name='ca'),

    url(r'^profile/$', 'panel.views.SeeProfile', name='profile'),
    url(r'^update-profile/$', 'panel.views.FillProfile', name='fillprofile'),
    url(r'^dashboard/$', 'panel.views.Dashboard', name='dashboard'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
