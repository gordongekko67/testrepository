from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.utils import timezone
import datetime
import requests

from .models import Titoli2, Giornalista,  PublishedManager, Cliente

from funzioni_iot.forms import FormContatto, FormTitoli, TitoliModelForm, FormRegistrazioneUser
from funzioni_iot.serializers import ClienteSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


def titoli_list(request):
    posts = Titoli2.objects.all()
    object_list = Titoli2.objects.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def clienti_list(request):
    cli = Cliente.objects.all()
    object_list = Cliente.objects.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/listcli.html', {'page': page, 'posts': posts})


def titoli_detail(request, year, month, day, post):
    post = get_object_or_404(Titoli2, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


def invio_mail(request):
    send_mail('Django mail', 'This e-mail was sent with Django.', 'enrico.saccheggiani@gmail.com', ['ensa77@yahoo.com'], fail_silently=False)
    msg = f'invio mail in Django'
    return HttpResponse(msg, content_type='text/plain')
    

def homep(request):
    return render(request, "index.html")


def prova_django(request):
    msg = f'prova visualizzazione dati django'
    return HttpResponse(msg, content_type='text/plain')


def hellocontattaci(request):
    if request.method == 'POST':
        form = FormContatto(request.POST)
        if form.is_valid():
            print("il form e' valido")
            print("NomE ",  form.cleaned_data["nome"])
            print("Cognome ",  form.cleaned_data["cognome"])
            return HttpResponse("<h1> Grazie per averci contattato </h1>")

    else:
        form = FormContatto()
    context = {"form": form}
    return render(request, "contattaci.html", context)


def crea_titoli(request):
    if request.method == 'POST':
        form = TitoliModelForm(request.POST)
        if form.is_valid():
            # inserimento dati nel data base
            new_titolo = form.save()
            titolo = Titoli2.objects.all()
            context = {"titoli": titolo}
            return render(request, 'blog/post/homepage2.html', context)

    else:
        form = TitoliModelForm()
    context = {"form": form}
    return render(request, "institoli.html", context)


def mod_titoli(request):
    if request.method == 'POST':
        pk1 = request.POST.get("pk")
        print(pk1)
        codtit = request.POST.get("codtit2")
        codslugtit = request.POST.get("codslugtit2")
        isin = request.POST.get("isin")
        body = request.POST.get("body")
        autor = request.POST.get("autor")
        Titoli2.objects.filter(pk=pk1).update(codtit2=codtit, codslugtit2=codslugtit,  codisintit2=isin, codbodytit2=body, codpublishtit2=datetime.datetime.now(
        ), codcreatedtit2=datetime.datetime.now(), codupdatedtit2=datetime.datetime.now(), codmintit2=1, codmaxtit2=10)
        titolo = Titoli2.objects.all()
        context = {"titoli": titolo}
        return render(request, 'blog/post/homepage2.html', context)


def can_titoli(request):
    if request.method == 'POST':
        pk = request.POST.get("pk")
        titol = Titoli2.objects.get(id=pk)
        titol.delete()
        titolo = Titoli2.objects.all()
        context = {"titoli": titolo}
        return render(request, 'blog/post/homepage2.html', context)


def visuatitoli(request):
    return render(request, "contattaci.html", context)


def registrazione(request):
    if request.method == 'POST':
        form = FormRegistrazioneUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create_user(
                username=username, password=password, email=email)

            user = authenticate(username=username, password=password)
            login(request, user)
        return HttpResponseRedirect

    else:
        form = FormRegistrazioneUser()
        context = {"form": form}
        return render(request, "registrazione.html", context)


def form2(request):
    template = loader.get_template('scelta.html')
    return HttpResponse(template)


def homeiot(request):
    return render(request, "scelta.html")


def base(request):
    return render(request, "base.html")


def titoli2(request):
    msg = f'prova  django Today is '
    return HttpResponse(msg, content_type='text/plain')


def home(request):
    g = []
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response = str(g)
    print(response)
    return HttpResponse(response, content_type='text/plain')


def homeTitoly(request):
    titolo = Titoli2.objects.all()
    context = {"titoli": titolo}
    return render(request, 'blog/post/homepage2.html', context)


def titoloDetailView(request, pk):
    titolo = Titoli2.objects.get(pk=pk)
    context = {"titoli": titolo}
    return render(request, 'blog/post/titolo_detail.html', context)

#  CBV   Class Based Views
#  Documentazione ufficiale


class TitoloDetailViewCB(DetailView):
    model = Titoli2
    template_name = "titolo_detail.html"


class AboutView(TemplateView):
    template_name = "blog/post/about2.html"


class Titoli_list_view(ListView):
    model = Titoli2
    template_name = "lista_titoli.html"


class Clienti_list_view(ListView):
    model = Cliente
    template_name = "lista_clienti.html"


def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = Loginform()

    return render(request, 'login.html', {"username": username})


def logout_enrico(request):
    logout(request)
    return render(request, 'logged_out.html')


def chiamata_request(request):
    print("chiamata  request")
    r = requests.get('https://api.exchangeratesapi.io/latest')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    msg = r.json()
    print(msg)
    return HttpResponse(msg, content_type='text/plain')


def chiamata_request_payload(request):
    print("chiamata  request con payload ")
    payload = {'base': 'USD', 'symbols': 'GBP'}
    r = requests.get('https://api.exchangeratesapi.io/latest', params=payload)
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    msg = r.json()
    print(msg)
    return HttpResponse(msg, content_type='text/plain')


def risposta_rest(request):
    titoli = Titoli2.objects.all()
    data1 = {"titoli": list(titoli.values("codtit2", "codbodytit2"))}
    data2 = {"titoli": list(titoli.values())}
    response = JsonResponse(data2)
    return response


@api_view(['GET'])
def cliente_collection(request):
    cli = Cliente.objects.all()
    serializer = ClienteSerializer(cli, many=True)
    print(serializer.data)
    content = JSONRenderer().render(serializer.data)
    print(content)
    #

    """
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)

    serializer = ClienteSerializer(data=data)
    #serializer.is_valid()
    # True
    serializer.validated_data
    # OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
    serializer.save()
"""
    return Response(serializer.data)
