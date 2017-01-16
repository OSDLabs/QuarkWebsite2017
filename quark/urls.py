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
    url(r'^events/$', 'events.views.events', name='events'),
    url(r'^workshop/$', 'events.views.workshop', name='workshop'),
    url(r'^workshop-register/$', 'events.views.workshopregister', name= 'workshopregister'),

    url(r'^workshop-register/([0-9]+)$', 'events.views.Workshop_Reg', name= 'workshopregisterpage'),

    url(r'^events/individual/$','events.views.Ind_Events', name='indevents'),
    url(r'^events/individual/([0-9]+)$','events.views.Ind_Events_Reg', name='indeventsreg'),
    url(r'^events/team/$','events.views.Team_Events', name='teamevents'),
    url(r'^events/team/([0-9]+)$','events.views.Team_Events_Reg', name='teameventsreg'),

    url(r'^profile/$', 'panel.views.SeeProfile', name='profile'),
    url(r'^update-profile/$', 'panel.views.FillProfile', name='fillprofile'),
    url(r'^dashboard/$', 'panel.views.Dashboard', name='dashboard'),
    url(r'^pay/$', 'panel.views.pay', name='pay'),

    url(r'^sponsors/$', 'sponsor.views.sponsors', name='contact'),
    url(r'^quick-reg/$', 'quickreg.views.quickreg', name='quickreg'),
    url(r'^payment/$', 'quickreg.views.payment', name='payment'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
