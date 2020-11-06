from django.conf.urls import url, include

from employment import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('create_employments', views.CreateEmploymentViewSet)
router.register('findByBarcode', views.FindEmploymentByBarcode, basename='findByBarcode')
router.register('employments', views.EmploymentViewSet)
router.register('users', views.UsersViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_employment'))
]
