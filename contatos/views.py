from django.shortcuts import render, redirect, get_object_or_404
from . models import Contatos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import openai

@login_required(redirect_field_name='login')
def index(request):
    contatos = Contatos.objects.filter(usuario_id=request.user.id).order_by('-id')
    return render(request, 'pages/index.html', {'contatos':contatos})

def search(request):
    q = request.GET.get('search')
    contatos = Contatos.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'contatos':contatos})

def detalhes(request, id):
    # contato = Contatos.objects.get(id=id)
    contato = get_object_or_404(Contatos, id=id)
    return render(request, 'pages/detalhes.html', {'contato':contato})

def deletar(request, id):
    contato = Contatos.objects.get(id=id)
    contato.delete()
    return redirect('home')

def adicionar(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        if descricao == '':
            descricao = gerarDescricao(nome)
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')
        novo_contato = Contatos(usuario_id=request.user.id, nome=nome,cpf=cpf, email=email, altura=altura, descricao=descricao, data_nascimento=data, telefone=telefone, imagem=imagem, ativo=True)
        novo_contato.save()
        return redirect('home')
    else:
        return render(request, 'pages/adicionar.html')


def editar(request, id):
    contato = Contatos.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        check = request.POST.get('check')
        if check == None:
            check = False
        else:
            check = True    
        imagem = request.FILES.get('imagem')
        print(imagem)
        contato.nome = nome
        contato.cpf = cpf
        contato.email = email
        contato.telefone = telefone
        contato.data = data
        if imagem != None:
            contato.imagem = imagem
        contato.altura = altura
        contato.descricao = descricao
        contato.ativo = check
        contato.save()
        return redirect('home')
    else:    
        return render(request, 'pages/editar.html', {'contato':contato})



def gerarDescricao(nome):

    API_KEY = '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' # API_KEY professor
    modelo = 'text-davinci-003'
    pergunta = f'gerar descrição para o contato de nome {nome} contendo no máximo de 100 caracteres'

    openai.api_key = API_KEY

    response = openai.Completion.create (
    engine = modelo,
    prompt = pergunta,
    max_tokens = 1024
    )

    return (response.choices[0]['text'])

def ver_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'pages/ver_usuarios.html', {'usuarios':usuarios})