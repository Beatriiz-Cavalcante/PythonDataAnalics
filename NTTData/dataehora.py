from datetime import date, datetime, time  #importação da biblioteca date-data -datetime-dataehora

#data
data = date(2024,9,15) #os argumentos passados são (ano, mês, dia)
print(data)

#data atual
print(date.today())

#data e hora
data_hora = datetime(2024, 9, 10, 20, 50)
print(data_hora)
print(datetime.today())

#hora

tempo = time(20, 50, 30)
print(tempo)

#timedelta - para calcular a diferença entre horários
from datetime import timedelta
tipo_carro = 'P' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno) 
    print(f'O carro chegou às {data_atual} e ficará pronto às {data_estimada}') 
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio) 
    print(f'O carro chegou às {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande) 
    print(f'O carro chegou às {data_atual} e ficará pronto às {data_estimada}')

#no deltatime se passa o parâmetro a ser acrecentado ou decrementaro (day, hour, minutes e etc)

# Formatando data e hora
d = datetime.now()
print(d.strftime("%d/%m/%Y %H:%M")) 

# Convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")  

#pytz para trabalhar com fuso horário (precisa baixar no terminal)
import pytz
data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)

#fuso horário sem pytz e sim com timezone
from datetime import timezone
d2 = datetime.now(datetime.timezone(datetime.timedelta(hour=-3)))
print(d2)