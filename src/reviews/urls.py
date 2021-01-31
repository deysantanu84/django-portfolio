from django.urls import path
from .views import (
    MyListView,
    ReviewCreateView,
    ReviewDeleteView,
    ReviewView,
    ReviewListView,
    ReviewUpdateView
)

app_name = 'reviews'
urlpatterns = [
    # path('', ReviewDetailView.as_view(template_name='contact.html'), name='reviews-detail'),
    # path('', MyListView.as_view(), name='reviews-list'),
    path('', ReviewListView.as_view(), name='reviews-list'),
    path('create/', ReviewCreateView.as_view(), name='reviews-create'),
    path('<int:id>/', ReviewView.as_view(), name='reviews-detail'),
    path('<int:id>/update/', ReviewUpdateView.as_view(), name='reviews-update'),
    path('<int:id>/delete/', ReviewDeleteView.as_view(), name='reviews-delete'),
]
