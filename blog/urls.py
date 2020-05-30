from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('inventory/', views.inventory, name='blog-inventory'),
    path('inventory/bebidas', views.display_bebidas,
         name='blog-inventory-bebidas'),
    path('inventory/alimentos', views.display_alimentos,
         name='blog-inventory-alimentos'),
    path('inventory/accesorios', views.display_accesorios,
         name='blog-inventory-accesorios'),
    path('inventory/limpieza', views.display_limpieza,
         name='blog-inventory-limpieza'),
    path('inventory/add/bebidas', views.add_bebidas,
         name='blog-inventory-add-bebidas'),
    path('inventory/add/alimentos', views.add_alimentos,
         name='blog-inventory-add-alimentos'),
    path('inventory/add/accesorios', views.add_accesorios,
         name='blog-inventory-add-accesorios'),
    path('inventory/add/limpieza', views.add_limpieza,
         name='blog-inventory-add-limpieza'),
    path('inventory/edit/bebidas/<int:pk>/', views.edit_bebidas,
         name='blog-inventory-edit-bebidas'),
    path('inventory/edit/alimentos/<int:pk>/', views.edit_alimentos,
         name='blog-inventory-edit-alimentos'),
    path('inventory/edit/accesorios/<int:pk>/', views.edit_accesorios,
         name='blog-inventory-edit-accesorios'),
    path('inventory/edit/limpieza/<int:pk>/', views.edit_limpieza,
         name='blog-inventory-edit-limpieza'),
    path('inventory/delete/bebidas/<int:pk>/', views.delete_bebidas,
         name='blog-inventory-delete-bebidas'),
    path('inventory/delete/alimentos/<int:pk>/', views.delete_alimentos,
         name='blog-inventory-delete-alimentos'),
    path('inventory/delete/accesorios/<int:pk>/', views.delete_accesorios,
         name='blog-inventory-delete-accesorios'),
    path('inventory/delete/limpieza/<int:pk>/', views.delete_limpieza,
         name='blog-inventory-delete-limpieza'),
]


# <app>/<model>_<viewtype>.html
