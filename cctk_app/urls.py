from django.conf.urls import url

from cctk_app import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^query_char/(?P<qchar>.*)/$', views.query_char, name='q'),
  url(r'^ajax/$', views.convert, name='convert')
]