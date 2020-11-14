from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import RastreadorForm
from .models import Rastreador


def lista_search(request):
    template_name = 'rastreadores/rastreadores_lista.html'
    search = request.GET.get('search')

    if search:

        objects_list = Rastreador.objects.filter(nr_rastreador__icontains=search)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)
    else:
        objects_list = Rastreador.objects.all()
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


def rastreadores_detail(request, pk):
    template_name = 'rastreadores/rastreadores_detail.html'
    obj = Rastreador.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


def rastreadores_add(request):
    template_name = 'rastreadores/rastreadores_form.html'
    return render(request, template_name)


def rastreadores_delete(request, pk):
    rastreador = get_object_or_404(Rastreador, pk=pk)
    rastreador.delete()
    return HttpResponseRedirect('/')


class RastreadoresCreate(CreateView):
    model = Rastreador
    template_name = 'rastreadores/rastreadores_form.html'
    form_class = RastreadorForm


class RastreadoresUpdate(UpdateView):
    model = Rastreador
    template_name = 'rastreadores/rastreadores_form.html'
    form_class = RastreadorForm
