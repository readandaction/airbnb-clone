from django.urls import path
from . import views

app_name = "rooms"
urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
    path("<int:pk>/photos/", views.RoomPhotosView.as_view(), name="photos"),
    path("<int:pk>/edit/", views.EditRoomView.as_view(), name="edit"),
    path("<int:pk>/", views.RoomDetail.as_view(), name="detail"),
]

