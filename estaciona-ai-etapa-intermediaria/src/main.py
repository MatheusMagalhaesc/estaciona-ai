import requests

def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url, timeout=5)
    return response.json()

def menu():
    while True:
        print("\n=== ESTACIONA AÍ ===")
        print("1 - Buscar endereço por CEP")
        print("2 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cep = input("Digite o CEP: ")
            dados = buscar_endereco(cep)

            if "erro" in dados:
                print("CEP inválido.")
            else:
                print(f"Rua: {dados.get('logradouro')}")
                print(f"Bairro: {dados.get('bairro')}")
                print(f"Cidade: {dados.get('localidade')}")
                print(f"Estado: {dados.get('uf')}")

        elif opcao == "2":
            break

if __name__ == "__main__":
    menu()
