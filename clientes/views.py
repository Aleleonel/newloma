from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import ClienteForm
from .models import Cliente


def lista_search(request):
    template_name = 'clientes/clientes_lista.html'
    search = request.GET.get('search')

    if search:

        objects_list = Cliente.objects.filter(nome__icontains=search)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)
    else:
        objects_list = Cliente.objects.all()
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


def clientes_detail(request, pk):
    template_name = 'clientes/clientes_detail.html'
    obj = Cliente.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


def clientes_add(request):
    template_name = 'clientes/clientes_form.html'
    return render(request, template_name)


def clientes_delete(request, pk):
    rastreador = get_object_or_404(Cliente, pk=pk)
    rastreador.delete()
    return HttpResponseRedirect('/')


class ClientesCreate(CreateView):
    model = Cliente
    template_name = 'clientes/clientes_form.html'
    form_class = ClienteForm


class ClientesUpdate(UpdateView):
    model = Cliente
    template_name = 'clientes/clientes_form.html'
    form_class = ClienteForm
