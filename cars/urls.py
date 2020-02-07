from django.urls import path

from. import views

urlpatterns = [
    path('all/', views.CarListView.as_view()),
    path('car-details/<pk>', views.CarDetailsView.as_view()),
    path('create/', views.CarCreateView.as_view()),
    path('picture/', views.PictureCreateView.as_view()),
    path('extra-categories/', views.ExtraCategoryLC.as_view()),
    path('extras/', views.ExtraLC.as_view())
]
