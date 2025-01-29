def metrosQuilometros(metros):
    return metros / 1000

def quilometrosMetros(quilometros):
    return quilometros * 1000

def gramasQuilogramas(gramas):
    return gramas / 1000

def quilogramasGramas(quilogramas):
    return quilogramas * 1000

while True:
    opcao = input('''             
------------ Menu -------------

(1) - Metros para Quilômetros
(2) - Quilômetros para Metros
(3) - Gramas para Quilogramas    
(4) - Quilogramas para Gramas   
(5) - Sair  

-------------------------------                                 
Escolha uma opção: ''')

    match opcao:
        case '1':
            metros = float(input('Digite o valor em METROS: '))
            print(f'{metros:.2f} metros equivale a {metrosQuilometros(metros):.3f} quilômetros.\n')
        case '2':
            quilometros = float(input('Digite o valor em QUILÔMETROS: '))
            print(f'{quilometros:.2f} quilômetros equivale a {quilometrosMetros(quilometros):.3f} metros.\n')
        case '3':
            gramas = float(input('Digite o valor em GRAMAS: '))
            print(f'{gramas:.2f} gramas equivale a {gramasQuilogramas(gramas):.2f} quilogramas.\n')
        case '4':
            quilogramas = float(input('Digite o valor em QUILOGRAMAS: '))
            print(f'{quilogramas:.2f} quilogramas equivale a {quilogramasGramas(quilogramas):.2f} gramas.\n')
        case '5':
            print('Saindo do Conversor de Unidades...')
            break
        case _:
            print('Opção inválida! Escolha uma opção do menu.\n')