from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


def home(request):
    page = 'Dashboard'
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Deliverd').count()
    pending = orders.filter(status='Pending').count()
    context = {'page': page, 'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    page = 'Product'
    products = Product.objects.all()
    context = {'page': page, 'products': products}
    return render(request, 'accounts/products.html', context)


def customer(request, pk):
    page = 'Customer'
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'page': page, 'customer': customer,
               'orders': orders, 'total_orders': total_orders}
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
