from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Invention
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    context = {"inventions": Invention.objects.all()}
    return render(request, "invention/home.html", context)


class InventionListView(ListView):
    model = Invention
    # Default view is something like <app>/<model>_<viewtype>.html
    # But can change to existing template
    template_name = "invention/home.html"
    context_object_name = "inventions"  # which I am already using
    ordering = ["-date_created"]  # sets the order by in revers (-)
    paginate_by = 5


class UserInventionListView(ListView):
    model = Invention
    # Default view is something like <app>/<model>_<viewtype>.html
    # But can change to existing template
    template_name = "invention/user_inventions.html"
    context_object_name = "inventions"  # which I am already using
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Invention.objects.filter(inventor=user).order_by("-date_created")


class InventionDetailView(DetailView):
    model = Invention


class InventionCreateView(LoginRequiredMixin, CreateView):
    model = Invention
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.inventor = self.request.user
        return super().form_valid(form)


class InventionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Invention
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.inventor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        invention = self.get_object()
        if self.request.user == invention.inventor:
            return True
        return False


class InventionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Invention
    success_url = "/invention/"

    def test_func(self):
        invention = self.get_object()
        if self.request.user == invention.inventor:
            return True
        return False

