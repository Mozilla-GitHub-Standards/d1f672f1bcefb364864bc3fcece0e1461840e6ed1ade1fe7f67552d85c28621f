from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^apply/$', views.create, name='submissions.create_entry'),
    url(r'^entries/all/$', views.list, name='submissions.entry_list'),
    url(r'^entries/export/$', views.export_csv,
        name='submissions.export_csv'),
    url(r'^entries/in/(?P<category>[\w-]+)/$', views.list, name='submissions.entry_list'),
    url(r'^entries/(?P<slug>[\w-]+)/$', views.single,
        name='submissions.entry_single'),
    url(r'^entries/(?P<slug>[\w-]+)/edit/$', views.edit_entry,
        name='submissions.entry_edit'),
)
