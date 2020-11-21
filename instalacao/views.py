from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView

from instalacao.forms import InstalacaoForm
from instalacao.models import Instalacao


def instalacao_list(request):
    template_name = 'instalacao/instalacao_list.html'
    search = request.GET.get('search')

    if search:
        objects_list = Instalacao.objects.filter(inst_placa__icontains=search, user=request.user)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)
    else:
        lista = Instalacao.objects.all().order_by('inst_placa').filter(user=request.user)

        paginator = Paginator(lista, 10)
        page = request.GET.get('page')
        objects_list = paginator.get_page(page)

        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


@login_required(login_url='/login/')
def instalacao_detail(request, pk):
    template_name = 'instalacao/instalacao_detail.html'
    obj = Instalacao.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


@login_required(login_url='/login/')
def instalacao_add(request):
    template_name = 'instalacao/instalacao_form.html'
    return render(request, template_name)


@login_required(login_url='/login/')
def instalacao_delete(request, pk):
    instalacao = get_object_or_404(Instalacao, pk=pk)
    instalacao.delete()
    return HttpResponseRedirect('/')


class InstalacaoCreate(CreateView):
    model = Instalacao
    template_name = 'instalacao/instalacao_form.html'
    form_class = InstalacaoForm


class InstalacaoUpdate(UpdateView):
    model = Instalacao
    template_name = 'instalacao/instalacao_form.html'
    form_class = InstalacaoForm
