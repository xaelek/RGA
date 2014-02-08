from portal import views
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',

    #Admin Authentication based views
    (r'^admin/', include(admin.site.urls)),

    #User Authentication based views
    (r'^/?$', views.mainview),

    #General User Pages
    (r'^rga/?$', views.rga),

    #Console Pages
    (r'^consoles/?$', views.consoles),
    (r'^consoles/(?P<console_id>\d+)/$', views.consoleDetails),

    #Games Pages
    (r'^games/?$', views.games),
    (r'^games/(?P<game_id>\d+)/$', views.gameDetails),

    #Achievements Pages
    (r'^achievements/?$', views.achievements),
    (r'^achievements/(?P<achievement_id>\d+)/$', views.achievementDetails),
)

# lets us serve our media
if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)