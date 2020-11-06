from django.conf.urls import url, include

from employment import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employments', views.EmploymentViewSet)
router.register('users', views.UsersViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('employments/findByBarcode/(?P<barcode>[a-z0-9]+)/', views.FindEmploymentByBarcode.as_view()),
    url('api-auth/', include('rest_framework.urls', namespace='rest_employment'))
]
