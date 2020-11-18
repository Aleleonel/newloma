from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.core.paginator import Paginator
from .forms import PrestadorForm
from .models import Prestador

import pycep_correios
from pycep_correios.excecoes import ExcecaoPyCEPCorreios


@login_required(login_url='/login/')
def error(request):
    template_name = 'buscaprest/error.html'
    return render(request, template_name)


@login_required(login_url='/login/')
def my_static(request, pk):
    template_name = 'buscaprest/estatico.html'
    objects = Prestador.objects.get(pk=pk)

    local = pycep_correios.consultar_cep(objects.cep)
    if local:
        context = {
            'local': local
        }
        return render(request, template_name, context)


@login_required(login_url='/login/')
def lista_search(request):
    template_name = 'buscaprest/buscaprest_lista.html'
    search = request.GET.get('search')
    search2 = request.GET.get('search2')

    if search or search2:

        objects_list = Prestador.objects.filter(categoria__icontains=search, cidade__icontains=search2)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)
    else:
        objects_list = Prestador.objects.all()
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


@login_required(login_url='/login/')
def prestadores_detail(request, pk):
    template_name = 'buscaprest/buscaprest_detail.html'
    obj = Prestador.objects.get(pk=pk)

    try:
        local = pycep_correios.consultar_cep(obj.cep)
        if local:
            context = {
                'local': local,
                'object': obj
            }
            return render(request, template_name, context)

    except ExcecaoPyCEPCorreios as exc:
        return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def prestadores_add(request):
    template_name = 'buscaprest/buscaprest_form.html'
    return render(request, template_name)


@login_required(login_url='/login/')
def prestadores_delete(request, pk):
    prestador = get_object_or_404(Prestador, pk=pk)
    prestador.delete()
    return HttpResponseRedirect('/')


class PrestadorCreate(CreateView):
    model = Prestador
    template_name = 'buscaprest/buscaprest_form.html'
    form_class = PrestadorForm


class PrestadorUpdate(UpdateView):
    model = Prestador
    template_name = 'buscaprest/buscaprest_form.html'
    form_class = PrestadorForm
