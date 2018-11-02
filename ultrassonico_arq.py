import sys
import time
import signal
import RPi.GPIO as GPIO
import datetime
 
# numeração dos pinos de acordo com a placa
GPIO.setmode(GPIO.BOARD)
 
# finalizar o acesso à GPIO do Raspberry de forma segura
def clean():
    GPIO.cleanup()
 
# finalizar o programa de forma segura com CTRL-C
def sigint_handler(signum, instant):
    clean()
    sys.exit()

def distancia():	
    delta_t = end_t - start_t
    distance = 100*(0.5 * delta_t * speed_of_sound)
    return distance
# Ativar a captura do sinal SIGINT (Ctrl-C)
signal.signal(signal.SIGINT, sigint_handler)
 
# TRIG  18. ECHO  16.
TRIG = 18
ECHO = 16
 
# Variáveis para auxiliar no controle do loop principal
# sampling_rate: taxa de amostragem em Hz, isto é, em média,
# quantas leituras do sonar serão feitas por segundo
# speed_of_sound: velocidade do som no ar a 30ºC em m/s
# max_distance: máxima distância permitida para medição
# max_delta_t: um valor máximo para a variável delta_t,
#   baseado na distância máxima max_distance
sampling_rate = 1.0
speed_of_sound = 349.10
max_distance = 15.0
max_delta_t = max_distance / speed_of_sound
 
# Define TRIG como saída digital
# Define ECHO como entrada digital
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
 
# Inicializa TRIG em nível lógico baixo
GPIO.output(TRIG, False)
time.sleep(2)
 
print ("Sampling Rate:", sampling_rate, "Hz")
print ("Distances (cm)")
 
# Loop principal. Será executado até que que seja pressionado CTRL-C
while True:
 
    # Gera um pulso de 10ms em TRIG.
    # Essa ação vai resultar na transmissão de ondas ultrassônicas pelo
    # transmissor do módulo sonar.
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
 
    # Atualiza a variável start_t enquanto ECHO está em nível lógico baixo.
    # Quando ECHO trocar de estado, start_t manterá seu valor, marcando
    # o momento da borda de subida de ECHO. Este é o momento em que as ondas
    # sonoras acabaram de ser enviadas pelo transmissor.
    while GPIO.input(ECHO) == 0:
      start_t = time.time()
 
    # calcula o tempo de propagacao da onda
    while GPIO.input(ECHO) == 1 and time.time() - start_t < max_delta_t:
      end_t = time.time()
 
    # calculo distancia
    if end_t - start_t < max_delta_t:
        delta_t = end_t - start_t
        distance = 100*(0.5 * delta_t * speed_of_sound)
    else:
        distance = -1
 
    # Imprime o valor da distância arredondado para 0 casa decimal
    #valor x do parametro de leitura do obstaculo
   
    print ("Distancia sensor" , round(distance, 1))
    vetor1 = []   
  
    r=15
    deltaEspaco=(2*3.1415*r)
    	
    if (distance > 9 ):
        t1=time.ctime()        
        arquivo1=open('tempo.txt','a')
        arquivo1.write(str(t1))
        arquivo1.write('\n')
        arquivo1.close()       
    if ((distance > 6) & (distance <= 9)):
        arquivo2 = open('tempo.txt', 'r')
        n_linhas2 = sum(1 for linha in arquivo2)
        if (n_linhas2 > 0):
            velocidade = (deltaEspaco/(n_linhas2))
            arquivo2.close()
            arquivo3 = open('velocidade.txt','w')
            arquivo3.write(str(velocidade))            
            arquivo3.close()
    if (distance <= 6 ):
        arquivo4 = open('tempo.txt', 'w')
        arquivo4.close()
         
    time.sleep(1.00)            
          
