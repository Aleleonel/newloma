from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import RastreadorForm
from .models import Rastreador


@login_required(login_url='/login/')
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
        lista = Rastreador.objects.all()

        paginator = Paginator(lista, 10)
        page = request.GET.get('page')
        objects_list = paginator.get_page(page)

        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


@login_required(login_url='/login/')
def rastreadores_detail(request, pk):
    template_name = 'rastreadores/rastreadores_detail.html'
    obj = Rastreador.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


@login_required(login_url='/login/')
def rastreadores_add(request):
    template_name = 'rastreadores/rastreadores_form.html'
    return render(request, template_name)


@login_required(login_url='/login/')
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
