from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import *
from .forms import *


def home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def inventory(request):
    return render(request, 'blog/inventory.html', {'title': 'Inventory'})


def display_bebidas(request):
    items = Bebidas.objects.all()
    context = {
        'items': items,
        'header': 'Bebidas'
    }
    return render(request, 'blog/inventory.html', context)


def display_alimentos(request):
    items = Alimentos.objects.all()
    context = {
        'items': items,
        'header': 'Alimentos'
    }
    return render(request, 'blog/inventory.html', context)


def display_accesorios(request):
    items = Accesorios.objects.all()
    context = {
        'items': items,
        'header': 'Accesorios'
    }
    return render(request, 'blog/inventory.html', context)


def display_limpieza(request):
    items = Limpieza.objects.all()
    context = {
        'items': items,
        'header': 'Limpieza'
    }
    return render(request, 'blog/inventory.html', context)


def add_device(request, cls, route, title):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect(route)
    else:
        form = cls()
        return render(request, "blog/add_new.html", {'form': form, 'title': title})


def add_bebidas(request):
    return add_device(request, BebidasForm, '/inventory/bebidas', 'BEBIDA')


def add_alimentos(request):
    return add_device(request, AlimentosForm, '/inventory/alimentos', 'ALIMENTOS')


def add_accesorios(request):
    return add_device(request, AccesoriosForm, '/inventory/accesorios', 'ACCESORIOS')


def add_limpieza(request):
    return add_device(request, LimpiezaForm, '/inventory/limpieza', 'ARTICULOS DE LIMPIEZA')


def edit_device(request, pk, model, cls, route):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(route)
    else:
        form = cls(instance=item)
        return render(request, 'blog/edit_item.html', {'form': form})


def edit_bebidas(request, pk):
    return edit_device(request, pk, Bebidas, BebidasForm, '/inventory/bebidas')


def edit_alimentos(request, pk):
    return edit_device(request, pk, Alimentos, AlimentosForm, '/inventory/alimentos')


def edit_accesorios(request, pk):
    return edit_device(request, pk, Accesorios, AccesoriosForm, '/inventory/accesorios')


def edit_limpieza(request, pk):
    return edit_device(request, pk, Limpieza, LimpiezaForm, '/inventory/limpieza')


def delete_bebidas(request, pk):

    Bebidas.objects.filter(id=pk).delete()

    items = Bebidas.objects.all()

    context = {
        'items': items
    }

    return redirect('/inventory/bebidas')


def delete_alimentos(request, pk):

    Alimentos.objects.filter(id=pk).delete()

    items = Alimentos.objects.all()

    context = {
        'items': items
    }

    return redirect('/inventory/alimentos')


def delete_accesorios(request, pk):

    Accesorios.objects.filter(id=pk).delete()

    items = Accesorios.objects.all()

    context = {
        'items': items
    }

    return redirect('/inventory/accesorios')


def delete_limpieza(request, pk):

    Limpieza.objects.filter(id=pk).delete()

    items = Limpieza.objects.all()

    context = {
        'items': items
    }

    return redirect('/inventory/limpieza')
