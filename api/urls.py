 

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .import views
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
	path('api/token/',
		jwt_views.TokenObtainPairView.as_view(),
		name ='token_obtain_pair'),
    path('account/register', views.UserCreate.as_view()),
	path('api/token/refresh/',
		jwt_views.TokenRefreshView.as_view(),
		name ='token_refresh'),
	 
]
