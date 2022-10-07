import time
tiempo_segundos=time.time()

##convierte la cadena de segundos al tiempo actual
tiempo_cadenas=time.ctime(tiempo_segundos)

hora=tiempo_cadenas[11]+tiempo_cadenas[12]
minutos=tiempo_cadenas[14]+tiempo_cadenas[15]
hora_salida=1860

if(int(hora)>=19 or int(hora)<=8):
    print("Es hora de ir a casa, el horario de trabajo termina a las 7 de la tarde")
else:
    if(int(hora)>8 and int(hora)<19):
        print("quedan ",19-int(hora),"horas y ",60-int(minutos)," minutos para el horario de salida")
