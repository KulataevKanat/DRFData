from django.conf.urls import url, include

from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('admins', views.AdminViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_snippets'))
]
