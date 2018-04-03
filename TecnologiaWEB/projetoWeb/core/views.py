from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def contato(request):
    if request.method == 'GET':
        print('Isso é um GET')
    else:
        print('Isso é um POST')
        print("Nome: ",request.POST.get('nomeCompleto'))
        print("Email: ",request.POST.get('email'))
        print("Assunto da mensagem: ",request.POST.get('opcao'))
        print("Texto da Mensagem: ",request.POST.get('mensagem'))
        print("Palavras chave: ",request.POST.get('selecao'))
        # Desse jeito só pegou uma palavra chave (a última).
    return render(request,'contato.html')

def login(request):
    
    if request.method == 'GET':
        print('Isso é um GET')
    else:
        print('Isso é um POST')

        if request.POST.get('senha') == "teste123":
            print('Usuário',request.POST.get('email'), 'entrou com sucesso!')
            return render(request, 'index.html')# < -- BÔNUS: O login certo deve redirecionar para o index novamente! :-)
            #Render não é redirect
        else:
            print('Usuário',request.POST.get('email'),' digitou a senha errada!')
            
    return render(request,'login.html')
    
    
