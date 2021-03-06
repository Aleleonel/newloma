from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import ClienteForm
from .models import Cliente


@login_required(login_url='/login/')
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
        lista = Cliente.objects.all().order_by('nome')

        paginator = Paginator(lista, 10)
        page = request.GET.get('page')
        objects_list = paginator.get_page(page)

        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


@login_required(login_url='/login/')
def clientes_detail(request, pk):
    template_name = 'clientes/clientes_detail.html'
    obj = Cliente.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


@login_required(login_url='/login/')
def clientes_add(request):
    template_name = 'clientes/clientes_form.html'
    return render(request, template_name)


@login_required(login_url='/login/')
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
