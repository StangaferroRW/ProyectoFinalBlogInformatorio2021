from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListarPosts.as_view(), name='lista'),
    path('<slug:pk>', views.DetallePosts.as_view(), name='detalle'),
]