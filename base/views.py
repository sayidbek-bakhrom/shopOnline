from django.shortcuts import render
from .models import Product
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'base/index.html')


def items_page(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'base/items_page.html', context)


class AddItem(CreateView):
    model = Product
    template_name = 'base/add_item.html'
    fields = '__all__'
    success_url = reverse_lazy('items')


def login_page(request):
    pass


def register(request):
    pass


def logout(request):
    pass

