from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.ReservationsLCView.as_view()),
    path('user/', views.UserReservationsView.as_view()),
    path('car/<pk>', views.CarReservationsView.as_view()),
    path('cancel/<pk>', views.ReservationCancelView.as_view()),
    path('create-review/', views.CreateReview.as_view()),
]
