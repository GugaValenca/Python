import time
from datetime import datetime

def relogio_digital():
    try:
        while True:
            agora = datetime.now()
            hora_formatada = agora.strftime('%H:%M:%S')
            print(f'\rHora atual: {hora_formatada}', end='')
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nOxente, relógio parado!')

# Exemplo de uso
relogio_digital()
