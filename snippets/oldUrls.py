from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # Snippets
    url('snippet/view', views.Snippets.as_view()),
    url('snippet/findById/(?P<id>[0-9]+)/', views.FindSnippetById.as_view()),
    url('snippet/changeView/(?P<id>[0-9]+)/', views.DeletePutSnippetById.as_view()),

    # Users
    url('user/view', views.GetCreateUser.as_view()),
    url('user/deleteById/(?P<id>[0-9]+)/', views.Users.deleteById),
    url('user/update/(?P<id>[0-9]+)/', views.Users.change),
    url('user/findById/(?P<id>[0-9]+)/', views.Users.findById),
    # AuthUser
    url('admin/findAll/', views.AdminList.as_view()),
    url('admin/findById/(?P<id>[0-9]+)/', views.FindAdminById.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
