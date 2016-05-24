
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from models import Item, Purchase
from forms import ItemCreateForm, OrderCreateForm

def home(request):
    return render_to_response('home.html', {})

def items_list(request):
    items = Item.objects.all()
    return render_to_response('items_list.html', {'items': items})

def items_create(request):
    ctx = {}
    form = ItemCreateForm()
    ctx.update({'form': form})
    if request.method == 'POST':
        post = request.POST
        form = ItemCreateForm(post, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('item_list')

        ctx.update({'form': form})
        return render(request, 'item_create.html', ctx)
    return render(request, 'item_create.html', ctx)

def order_create(request):
    ctx = {}
    form = OrderCreateForm()
    ctx.update({'form': form})
    if request.method == 'POST':
        post = request.POST
        form = OrderCreateForm(post, request.FILES)
        if form.is_valid():
            item = Item.objects.get(id=request.POST.get('item'))
            if item.inventory != 0:
                obj = form.save()
                item.inventory = item.inventory - 1
                item.save()
                return redirect('item_list')
            else:
                ctx.update({'msg': "item not avaliable in inventory, please select another item"})

        ctx.update({'form': form})
        return render(request, 'order_create.html', ctx)
    return render(request, 'order_create.html', ctx)
