from django.conf.urls import patterns, url

from demo import views

# import pdb; pdb.set_trace()
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pdb/$', views.pdb_view, name='pdb_view'),
    url(r'^rpdb/$', views.rpdb_view, name='rpdb_view'),
)
