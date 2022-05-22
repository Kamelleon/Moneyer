from django.urls import path
from to_return_money.views import ReturnListView, ReturnCreateView, ReturnDetailView, ReturnDeleteView, ReturnUpdateView


app_name = "to_return_money"
urlpatterns = [
    path('', ReturnListView.as_view(), name='to-return-list'),
    path('create', ReturnCreateView.as_view(), name='to-return-create'),
    path('<int:id>', ReturnDetailView.as_view(), name='to-return-details'),
    path('delete/<int:id>', ReturnDeleteView.as_view(), name='to-return-delete'),
    path('update/<int:pk>', ReturnUpdateView.as_view(), name='to-return-update'),
]