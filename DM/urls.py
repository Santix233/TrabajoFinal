from django.urls import path, re_path
from.views import *
from django.conf.urls import include
urlpatterns=[
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r"canal/(?P<pk>[\w-]+)", CanalDetailView.as_view(),name="canal"),
    path("DM/<str:username>",mensajes_privados),
    path("MS/<str:username>",DetailMs.as_view(),name= "detailms"),
    path("DM/",Inbox.as_view(),name="inbox"),






]


