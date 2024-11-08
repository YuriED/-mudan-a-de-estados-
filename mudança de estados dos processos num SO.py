import random
import time

# Definindo as informações dos processos
processos = [
    {'PID': 0, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 10000},
    {'PID': 1, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 5000},
    {'PID': 2, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 7000},
    {'PID': 3, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 3000},
    {'PID': 4, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 3000},
    {'PID': 5, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 8000},
    {'PID': 6, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 2000},
    {'PID': 7, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 5000},
    {'PID': 8, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 4000},
    {'PID': 9, 'TP': 0, 'CP': 1, 'EP': 'PRONTO', 'NES': 0, 'N_CPU': 0, 'tempo_total': 10000}
]

quantum = 1000
arquivo = "tabela_processos.txt"

def atualizar_tabela():
    with open(arquivo, "w") as f:
        for p in processos:
            f.write(f"PID: {p['PID']}, TP: {p['TP']}, CP: {p['CP']}, EP: {p['EP']}, NES: {p['NES']}, N_CPU: {p['N_CPU']}\n")

def imprimir_troca_contexto(processo, estado_destino):
    print(f"PID {processo['PID']} {processo['EP']} >>> {estado_destino}")
    atualizar_tabela()

def simular_executando(processo):
    processo['EP'] = 'EXECUTANDO'
    imprimir_troca_contexto(processo, 'EXECUTANDO')
    
    for ciclo in range(quantum):
        processo['TP'] += 1
        processo['CP'] = processo['TP'] + 1
        processo['N_CPU'] += 1
        
        if random.randint(1, 100) <= 1:
            processo['EP'] = 'BLOQUEADO'
            processo['NES'] += 1
            imprimir_troca_contexto(processo, 'BLOQUEADO')
            break
        
        if processo['TP'] >= processo['tempo_total']:
            processo['EP'] = 'TERMINADO'
            imprimir_finalizacao(processo)
            return

    if processo['EP'] == 'EXECUTANDO':
        processo['EP'] = 'PRONTO'
        imprimir_troca_contexto(processo, 'PRONTO')

def imprimir_finalizacao(processo):
    print(f"Processo {processo['PID']} finalizado. Detalhes: TP={processo['TP']}, CP={processo['CP']}, EP={processo['EP']}, NES={processo['NES']}, N_CPU={processo['N_CPU']}")

def gerenciar_bloqueados():
    for processo in processos:
        if processo['EP'] == 'BLOQUEADO' and random.randint(1, 100) <= 30:
            processo['EP'] = 'PRONTO'
            imprimir_troca_contexto(processo, 'PRONTO')

def escalonar_processos():
    while any(p['EP'] != 'TERMINADO' for p in processos):
        for processo in processos:
            if processo['EP'] == 'PRONTO':
                simular_executando(processo)
            gerenciar_bloqueados()
            time.sleep(0.1)  # Simulação de tempo para observar o ciclo

escalonar_processos()
print("Simulação concluída. Verifique o arquivo tabela_processos.txt para os detalhes.")
