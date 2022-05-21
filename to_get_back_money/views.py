from django.shortcuts import render, get_object_or_404
from .models import GetBackMoney
from .forms import GetBackModelForm
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
DeleteView
)

class GetBackListView(ListView):
    model = GetBackMoney
    template_name = "to_get_back.html"

class GetBackDetailView(DetailView):
    template_name = "details.html"
    queryset = GetBackMoney.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(GetBackMoney, id=id_)

class GetBackDeleteView(DeleteView):
    template_name = "details.html"
    queryset = GetBackMoney.objects.all()
    success_url = "/to_get_back/"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(GetBackMoney, id=id_)

class GetBackCreateView(CreateView):
    template_name = 'create_return.html'
    form_class = GetBackModelForm
    success_url = '/to_get_back/'
    queryset = GetBackMoney.objects.all()