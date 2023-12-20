from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView

from .models import *


def index(request):
    return render(request, 'webcake/index.html')


def sign(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, email, password)
        my_user.save()
        return redirect('logins')
    return render(request, 'webcake/signup.html')


def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pas = request.POST.get('pass')
        user = authenticate(request, username=username, password=pas)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre')
            return render(request, 'webcake/login.html')

    return render(request, 'webcake/login.html')


def log_out(request):
    logout(request)
    return redirect('logins')


def keks(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'webcake/keks.html', context)


def pirog(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'webcake/pirog.html', context)


def tort(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'webcake/tort.html', context)

# def basket(request):
#     return render(request, 'webcake/detail.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'webcake/detail.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'webcake/checkout.html', context)


def base(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'webcake/base.html', context)


class Search(ListView):
    template_name = 'webcake/base.html'
    context_object_name = 'pr'

    def get_queryset(self):
        return Product.objects.filter(aty__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)