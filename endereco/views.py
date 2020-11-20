from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .forms import EnderecoForm
from .models import Endereco


@login_required(login_url='/login/')
def lista_search(request):
    template_name = 'endereco/enderecos_lista.html'
    search = request.GET.get('search')

    if search:

        objects_list = Endereco.objects.filter(nome__icontains=search)
        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)
    else:
        lista = Endereco.objects.all().order_by('rua')

        paginator = Paginator(lista, 10)
        page = request.GET.get('page')
        objects_list = paginator.get_page(page)

        context = {
            'object_list': objects_list
        }
        return render(request, template_name, context)


@login_required(login_url='/login/')
def endereco_detail(request, pk):
    template_name = 'endereco/enderecos_detail.html'
    obj = Endereco.objects.get(pk=pk)

    context = {
        'object': obj
    }
    return render(request, template_name, context)


@login_required(login_url='/login/')
def endereco_add(request):
    template_name = 'endereco/enderecos_form.html'
    return render(request, template_name)


@login_required(login_url='/login/')
def endereco_delete(request, pk):
    rastreador = get_object_or_404(Endereco, pk=pk)
    rastreador.delete()
    return HttpResponseRedirect('/')


class EnderecoCreate(CreateView):
    model = Endereco
    template_name = 'endereco/enderecos_form.html'
    form_class = EnderecoForm


class EnderecoUpdate(UpdateView):
    model = Endereco
    template_name = 'endereco/enderecos_form.html'
    form_class = EnderecoForm
