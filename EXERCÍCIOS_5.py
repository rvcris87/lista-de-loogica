usuario_correto = "admin"
senha_correta = "1234"
tentativas = 0
acesso_permitido = False

while tentativas < 3 and acesso_permitido == False:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso permitido.")
        acesso_permitido = True
    else:
        tentativas += 1
        print("Dados incorretos.")

if acesso_permitido == False:
    print("Acesso bloqueado.")