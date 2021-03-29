from django.shortcuts import render, redirect

from .models import PosModel
from .forms import Pos

def list(request):
    pos_model = PosModel.objects.all()
    form = Pos(request.POST or None)

    context = {
        'judul': 'CRUD',
        'content': 'Simple CRUD',
        'form': form,
        'pos_model': pos_model
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('pos:list')

    return render(request, 'pos/index.html', context)

def delete(request,delete_id):
    PosModel.objects.filter(id=delete_id).delete()
    return redirect('pos:list')

def update(request,update_id):
    pos_model = PosModel.objects.get(id=update_id)

    data = {
        'product_name': pos_model.product_name,
        'price': pos_model.price,
        'qty': pos_model.qty
    }

    form = Pos(request.POST or None, initial=data, instance=pos_model)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('pos:list')

    context = {
        'judul': 'CRUD Update',
        'content': 'Simple CRUD',
        'form': form,
    }

    return render(request, 'pos/index.html', context)