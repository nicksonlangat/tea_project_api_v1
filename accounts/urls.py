from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .import views

router = DefaultRouter()
router.register(r'register', views.RegisterUserView)
router.register(r'users', views.UserViewset)
router.register(r'employees', views.EmployeeViewset)

urlpatterns =[
    path('get/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls