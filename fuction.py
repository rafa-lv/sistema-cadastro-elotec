
#funcao para cadastrar uma missao dentro da nossa lista
def CadastrarMissao(lista):
    print("seja bem vindo a pagina de cadastro");
    
    nave = input("digite o nome da nave");
    destino = input("digite o destino")
    tripulantes = int(input("diga a quantidade de tripulantes"));
    combustivel = float(input("diga a quantidade de combustivel (litros)"))
    tempo = int(input("diga o tempo de duração da viagem (dias)"));
    
    missao = {
        "nave" : nave,
        "destino" : destino,
        "tripulantes" : tripulantes,
        "combustivel" : combustivel,
        "tempo" : tempo
    }

    lista.append(missao);
    print("missao cadastrada com sucesso");

def ListarMissoes(lista):
    if len(lista)==0:
        print("nao ha missoes cadastrada na nossa lista");
    else: 
        for indice,missao in enumerate(lista):
            print(f"{missao[i + 1]}");
            print(f"missao{missao['nave']}" (nome da nave)");
            print(f"missao{missao['destino']} (destino da nave)");
            print(f"missao{missao['tripulantes']} (quantidade de tripulante)");
            print(f"missao{missao['combustivel']} (quantiade de combustivel)");
            print(f"missao{missao['tempo']} (tempo de duracao da viagem)");
           