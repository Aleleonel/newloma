from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import VeiculosForm
from .models import Veiculos


@login_required(login_url='/login/')
def lista_search(request):
    template_name = 'veiculos/veiculos_lista.html'
    search = request.GET.get('search')
    search2 = request.GET.get('search2')

    if search:

        objects_list = Veiculos.objects.filter(placa__icontains=search)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)

    elif search2:

        objects_list = Veiculos.objects.filter(renavam__icontains=search2)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)

    else:
        lista = Veiculos.objects.all()

        paginator = Paginator(lista, 10)
        page = request.GET.get('page')
        objects_list = paginator.get_page(page)

        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


@login_required(login_url='/login/')
def veiculos_detail(request, pk):
    template_name = 'veiculos/veiculos_detail.html'
    obj = Veiculos.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


@login_required(login_url='/login/')
def veiculos_add(request):
    template_name = 'veiculos/veiculos_form.html'
    return render(request, template_name)


@login_required(login_url='/login/')
def veiculos_delete(request, pk):
    veiculo = get_object_or_404(Veiculos, pk=pk)
    veiculo.delete()
    return HttpResponseRedirect('/')


class VeiculosCreate(CreateView):
    model = Veiculos
    template_name = 'veiculos/veiculos_form.html'
    form_class = VeiculosForm


class VeiculosUpdate(UpdateView):
    model = Veiculos
    template_name = 'veiculos/veiculos_form.html'
    form_class = VeiculosForm
