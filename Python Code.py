def calcular_area(tipo_area, dimensoes):
    if tipo_area == 'retangulo':
        return dimensoes[0] * dimensoes[1]
    elif tipo_area == 'triangulo':
        return (dimensoes[0] * dimensoes[1]) / 2
    elif tipo_area == 'circulo':
        return np.pi * (dimensoes[0]**2)
    else:
        return 0
def calcular_insumos(aplicacao, area):
    return aplicacao * area
dados = []

def menu():
    while True:
        print("\n1. Adicionar cultura")
        print("2. Listar culturas")
        print("3. Atualizar cultura")
        print("4. Remover cultura")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cultura = input("Nome da cultura: ")
            tipo_area = input("Tipo de área (retangulo, triangulo, circulo): ").lower()
            
            if tipo_area == 'retangulo':
                largura = float(input("Digite a largura (m): "))
                comprimento = float(input("Digite o comprimento (m): "))
                dimensoes = [largura, comprimento]
            elif tipo_area == 'triangulo':
                base = float(input("Digite a base (m): "))
                altura = float(input("Digite a altura (m): "))
                dimensoes = [base, altura]
            elif tipo_area == 'circulo':
                raio = float(input("Digite o raio (m): "))
                dimensoes = [raio]
            else:
                print("Tipo de área inválido!")
                continue
            
            area = calcular_area(tipo_area, dimensoes)
            produto = input("Produto aplicado: ")
            aplicacao = float(input("Quantidade por metro quadrado (L/m²): "))
            total_insumos = calcular_insumos(aplicacao, area)
            
            dados.append({'cultura': cultura, 'area': area, 'produto': produto, 'insumos': total_insumos})
            print("Cultura adicionada com sucesso!")
        
        elif opcao == '2':
            if not dados:
                print("Nenhuma cultura cadastrada.")
            else:
                for i, d in enumerate(dados):
                    print(f"{i+1}. Cultura: {d['cultura']}, Área: {d['area']:.2f} m², Produto: {d['produto']}, Insumos: {d['insumos']:.2f} L")
        
        elif opcao == '3':
            if not dados:
                print("Nenhuma cultura cadastrada.")
                continue
            idx = int(input("Digite o índice da cultura para atualizar: ")) - 1
            if 0 <= idx < len(dados):
                dados[idx]['produto'] = input("Novo produto aplicado: ")
                print("Cultura atualizada!")
            else:
                print("Índice inválido!")
        
        elif opcao == '4':
            if not dados:
                print("Nenhuma cultura cadastrada.")
                continue
            idx = int(input("Digite o índice da cultura para remover: ")) - 1
            if 0 <= idx < len(dados):
                dados.pop(idx)
                print("Cultura removida!")
            else:
                print("Índice inválido!")
        
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()