from random import sample


class Jogador:
    def __init__(self, nome):
        self.quantidade_vitorias = 0
        self.saldo = 300
        self.nome = nome
        self.ordem = 0
        self.ultima_casa_tabuleiro = 0

class Imoveis:
    def __init__(self, nome, venda, aluguel):
        self.nome=nome
        self.custo_venda = venda
        self.valor_aluguel = aluguel
        self.proprietario = None
        
def criar_imoveis():
    imoveis = []
    custo_venda = 0
    valor_aluguel = 0
    for seq in range(21):
        imoveis.append(
            Imoveis(f'Imovel - {seq}', custo_venda, valor_aluguel)
        )
        custo_venda += 100
        valor_aluguel += 100

    return imoveis

def definir_ordem_de_jogo(jogadores):
    opcoes = list(range(1,5))
    ordem = sample(opcoes, 4)
    index = 0
    for jogador in jogadores:
        jogador.ordem = ordem[index]
        index+= 1

    return sorted(jogadores, key=lambda jogador: jogador.ordem)

def jogar_dado():
    opcoes = list(range(1,7))
    ordem = sample(opcoes,1)
    return ordem[0]

def jogar_rodada(jogador):
    qty_casas = jogar_dado()
    if (jogador.ultima_casa_tabuleiro + qty_casas) > 20:
        jogador.ultima_casa_tabuleiro = (jogador.ultima_casa_tabuleiro + qty_casas) - 20
    else:
        jogador.ultima_casa_tabuleiro += qty_casas
    
    return imoveis[jogador.ultima_casa_tabuleiro]

def remover_do_jogo(jogador, index):
    if jogador.saldo < 0:
        for imo in imoveis:
            if imo.proprietario.nome == jogador.nome:
                imo.proprietario = None
            
        del(ordem_de_jogo[index])
        return 'removido'

    return 'nada a fazer'

def pagar_aluguel(jogador, imovel):
    jogador.saldo -= imovel.valor_aluguel
    imovel.proprietario.saldo += imovel.valor_aluguel

def compar_imovel(imovel, jogador):
    imovel.proprietario = jogador
    jogador.saldo -= imovel.custo_venda
    
impulsivo = Jogador('impulsivo')
exigente = Jogador('exigente')
cauteloso = Jogador('cauteloso')
aleatorio = Jogador('aleatorio')

ordem_de_jogo = definir_ordem_de_jogo([impulsivo, exigente, cauteloso, aleatorio])
imoveis = criar_imoveis()

qty_numero_rodada = 1
qty_maximo_rodadas = 1000


for partidas in range(1):
    for rodadas in range(1):
        for index, jogador in enumerate(ordem_de_jogo):
            
            if jogador.nome == 'impulsivo':
                imovel = jogar_rodada(jogador)
                if imovel.proprietario is None:
                    compar_imovel(imovel, jogador)
                    remover_do_jogo(jogador, index)

                elif imovel.proprietario is not None:
                    pagar_aluguel(jogador, imovel)
                    remover_do_jogo(jogador, index)

            elif jogador.nome == 'exigente':
                imovel = jogar_rodada(jogador)
                if imovel.proprietario is None and imovel.valor_aluguel > 50:
                    compar_imovel(imovel, jogador)
                    remover_do_jogo(jogador, index)

                elif imovel.proprietario is not None:
                    pagar_aluguel(jogador, imovel)
                    remover_do_jogo(jogador, index)

            elif jogador.nome == 'cauteloso':
                imovel = jogar_rodada(jogador)
                saldo_pos_compra = jogador.saldo - imovel.custo_venda
                if imovel.proprietario is None and saldo_pos_compra > 80:
                    compar_imovel(imovel, jogador)
                    remover_do_jogo(jogador, index)

                elif imovel.proprietario is not None:
                    pagar_aluguel(jogador, imovel)
                    remover_do_jogo(jogador, index)

            elif jogador.nome == 'aleatorio':
                    opcoes = list(range(1,3))
                    compra = sample(opcoes,1)[0] > 1
                    if imovel.proprietario is None and comprar is True:
                        compar_imovel(imovel, jogador)
                        remover_do_jogo(jogador, index)

                    elif imovel.proprietario is not None:
                        pagar_aluguel(jogador, imovel)
                        remover_do_jogo(jogador, index)

            jogador.saldo += 100




