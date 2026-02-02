import json
import time

ARQUIVO = "usuariosJSON.json"

def pedir_usuario():
        while True:
                nome = input("Qual o seu nome? (Caso queira cancelar, digite cancelar.)\n").strip()

                if nome.lower() == "cancelar":
                       return

                if nome:
                        return nome
                
                else:
                        print("Insira um nome válido...\n")
                        continue
                
def pedir_idade():
        while True:
                
            idade = input("Qual a sua idade?\n").strip()

            if not idade:
                        print("Insira um digito válido...\n")
                        continue
            try:
                    idade = int(idade)
                    if idade <= 0:
                            print("Idade Inválida.\n")
                            continue
                    return idade
                
            except ValueError:
                    print("Digite apenas números.\n")        


def carregar_usuarios():
        try:
                with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                    return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
                return []

def salvar_usuarios(usuarios):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

def adicionar_usuarios(nome, idade):
        usuarios = carregar_usuarios()

        usuarios.append({
            "nome": nome,
            "idade": idade})
            
        salvar_usuarios(usuarios)
        print("\nUsuário salvo com sucesso!\n")


def listar_usuarios():
        usuarios = carregar_usuarios()

        if not usuarios:
                print("\n Nenhum usuário cadastrado...\n")
                return
        print("------ Usuários Cadastrados ------")
        for user in usuarios:
                print(f"Nome: {user['nome']} | Idade: {user['idade']}")
                time.sleep(0.5)
        print("----------------------------------")
        time.sleep(1)


def buscar_usuario():
       
        usuarios = carregar_usuarios()

        if not usuarios:
               print("\n Nenhum usuário cadastrado...\n")
               return

        buscar = input("\nQuem gostaria de encontrar?\n")

        for user in usuarios:
                if user['nome'].lower() == buscar.lower():
                        print(f"\nNome: {user['nome']} | Idade: {user['idade']}\n")
                        time.sleep(1)
                        return
        print("\nUsuário não encontrado\n")
                

def remover_usuario():
        usuarios = carregar_usuarios()

        if not usuarios:
                print("Nenhum usuário cadastrado...\n")
                return
        
        nome_remover = input("Digite o nome do usuário que deseja remover.\n").strip().lower()
        
        if not nome_remover:
              print("Usuário não existe.\n")
        
        for user in usuarios:
                if user['nome'].lower() == nome_remover:
                        confirmacao = input(f"\nDeseja remover {user['nome']}? (s/n)\n").strip().lower()

                        if confirmacao == "s":
                                usuarios.remove(user)
                                salvar_usuarios(usuarios)
                                print("\nUsuário removido com sucesso!\n")

                        else:
                                print("\nAção cancelada com sucesso!\n")
                        salvar_usuarios(usuarios)
                        return

        print("\nUsuário não existe.\n")

        

def editar_usuario():
       usuarios = carregar_usuarios()
       if not usuarios:
                print("\n Nenhum usuário cadastrado...\n")
                return
       nome_editar = input("Qual usuário deseja editar?\n").strip().lower()

       if not nome_editar:
              print("Usuário não existe.\n")
              return

       for user in usuarios:
              if user['nome'].lower() == nome_editar:
                     confirmaNome = input("\nDeseja editar nome de usuário? (s/n) \n").strip().lower()

                     if confirmaNome == "s":
                            nome = pedir_usuario()
                            if nome is None:
                                   continue
                                
                            else:
                                   user['nome'] = nome
                            
                     
                     confirmaIdade = input("Deseja editar idade de usuário? (s/n)\n").strip().lower()

                     if confirmaIdade == "s":
                            user['idade'] = pedir_idade()
                            
                     salvar_usuarios(usuarios)
                     return
                            

                

        

def menu():
    print("\n====== MENU ======")
    print("1. Cadastrar novo usuário.")
    print("2. Listar usuários.")
    print("3. Buscar usuário.")
    print("4. Remover usuário.")
    print("5. Editar usuário.")
    print("6. Sair.")
            
def main():
       while True:
            
            usuarios = carregar_usuarios()
            menu()
            
            opcao = input("\nPressione o número referente a opção desejada...\n").strip()
            
            if opcao == "1":
                nome = pedir_usuario()

                if nome is None:
                        continue

                emUso = False
                for user in usuarios:
                        if nome.lower() == user['nome'].lower():
                                print("Este nome de usuário já está em uso.\n")
                                emUso = True
                                break
                if not emUso:
                        idade = pedir_idade()
                        adicionar_usuarios(nome, idade)        
            
            elif opcao == "2":
                listar_usuarios()
            
            elif opcao == "3":
                buscar_usuario()

            elif opcao == "4":
                remover_usuario()

            elif opcao == "5":
                editar_usuario()
                
            elif opcao == "6":
                print("Até mais! 👋")
                break

            else:
                print("\nOpção inválida.\n")

if __name__ == "__main__":
       main()