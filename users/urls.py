from django.urls import path
from rest_framework_jwt import views as jwt_views

from. import views

urlpatterns = [
    path('api/token/', jwt_views.obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.refresh_jwt_token, name='token_refresh'),
    path('api/token/verify/', jwt_views.verify_jwt_token, name='token_refresh'),
    path('all/', views.UserList.as_view()),
    path('user/<pk>', views.OwnUserRUD.as_view()),
    path('register/', views.CreateUser.as_view()),
    path('check-username/', views.CheckUsername.as_view()),
    path('check-email/', views.CheckEmail.as_view()),
    path('add-favourite/', views.AddFavourite.as_view()),
    path('favourites/', views.Favourites.as_view()),
]
