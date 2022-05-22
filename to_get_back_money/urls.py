
from django.urls import path
from to_get_back_money.views import GetBackListView, GetBackCreateView, GetBackDetailView, GetBackDeleteView, GetBackUpdateView

app_name = 'to_get_back_money'
urlpatterns = [
    path('', GetBackListView.as_view(), name='to-get-back-list'),
    path('create', GetBackCreateView.as_view(), name='to-get-back-create'),
    path('<int:id>', GetBackDetailView.as_view(), name='to-get-back-details'),
    path('delete/<int:id>', GetBackDeleteView.as_view(), name='to-get-back-delete'),
    path('update/<int:pk>', GetBackUpdateView.as_view(), name='to-get-back-update'),
]
