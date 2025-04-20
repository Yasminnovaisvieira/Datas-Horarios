import pytz #Trabalha com os fusos horários do mundo todo.
import datetime

print("Olá! O programa irá solicitar o nome de um país e informar a data e o horário atual dele.\n")

print("FORMATO A SER PERQUISADO: Região/Cidade (1ª letra maiúscula, sem espaços e em inglês).\n")

print("Acesse esse site para verificar as opções disponíveis: https://mljar.com/blog/list-pytz-timezones/\n")

pais = input("Digite o país que deseja saber o horário: ")

if pais in pytz.all_timezones:
    horario = datetime.datetime.now(pytz.timezone(pais))
    print(horario.strftime("%d/%m/%Y %H:%M:%S"))
else:
    print("País não encontrado. Tente novamente.")