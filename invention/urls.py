from django.urls import path
from .views import (
    InventionDetailView,
    InventionCreateView,
    InventionUpdateView,
    InventionDeleteView,
    InventionListView,
    UserInventionListView,
)

# from . import views

urlpatterns = [
    # path("", views.home, name="invention-home"),
    path("", InventionListView.as_view(), name="invention-home"),
    path(
        "user/<str:username>", UserInventionListView.as_view(), name="user-inventions"
    ),
    path("<int:pk>/", InventionDetailView.as_view(), name="invention-detail"),
    path("new/", InventionCreateView.as_view(), name="invention-create"),
    path("<int:pk>/update", InventionUpdateView.as_view(), name="invention-update"),
    path("<int:pk>/delete", InventionDeleteView.as_view(), name="invention-delete"),
]
