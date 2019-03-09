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
        "invention/user/<str:username>", UserInventionListView.as_view(), name="user-inventions"
    ),
    path("invention/<int:pk>/", InventionDetailView.as_view(), name="invention-detail"),
    path("invention/new/", InventionCreateView.as_view(), name="invention-create"),
    path(
        "invention/<int:pk>/update",
        InventionUpdateView.as_view(),
        name="invention-update",
    ),
    path(
        "invention/<int:pk>/delete",
        InventionDeleteView.as_view(),
        name="invention-delete",
    ),
]
