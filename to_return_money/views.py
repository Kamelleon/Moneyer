from django.shortcuts import render, get_object_or_404, redirect
from .models import ReturnMoney
from .forms import ReturnModelForm
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView, UpdateView
)

class ReturnListView(ListView):
    model = ReturnMoney
    template_name = "to_return.html"

class ReturnDetailView(DetailView):
    template_name = "details_to_return.html"
    queryset = ReturnMoney.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ReturnMoney, id=id_)

class ReturnDeleteView(DeleteView):
    template_name = "details_to_return.html"
    queryset = ReturnMoney.objects.all()
    success_url = "/to_return/"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ReturnMoney, id=id_)

class ReturnCreateView(CreateView):
    template_name = 'create_to_return.html'
    form_class = ReturnModelForm
    success_url = '/to_return/'
    queryset = ReturnMoney.objects.all()

class ReturnUpdateView(UpdateView):
    template_name = "update_to_return.html"
    form_class = ReturnModelForm
    model = ReturnMoney