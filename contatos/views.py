from django.shortcuts import render, redirect
from . models import Contatos

def index(request):
    contatos = Contatos.objects.all().order_by('-id')
    return render(request, 'pages/index.html', {'contatos':contatos})

def search(request):
    q = request.GET.get('search')
    contatos = Contatos.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'contatos':contatos})

def detalhes(request, id):
    contato = Contatos.objects.get(id=id)
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
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')
        novo_contato = Contatos(nome=nome,cpf=cpf, email=email, altura=altura, descricao=descricao, data_nascimento=data, telefone=telefone, imagem=imagem, ativo=True)
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