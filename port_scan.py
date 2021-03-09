import socket
import sys
import ipaddress

#help
#documentado o suficiente nele mesmo para precisar de uma descricao
ajuda = input("Ajuda? s/n: ")
if ajuda == "s":
	print (''' 
	1-Primeiro voce terá de digitar o IP (em numeros com ponto) para a analise
	
	2-Você deverá selecionar um scan para ser analisado no IP
	que voce forneceu

		''')

	portas = input("Gostaria de ver quais portas disponiveis pra scan? s/n: ")
	if portas == "s":
		print (''' 
	Simples: 21,22,25,80,443,8080
	Moderado: 21, 22, 25, 53, 80, 110, 135, 137, 138, 139, 143, 443, 465, 587, 995, 1521, 2525, 3306, 8000, 8080
	Completo: 1 a 65535
	''')
#entrada do ip para o scan
ip_informado = input("Digite o IP: ")
#entrada dos modelos de scan para analise do IP 
scan = input('''Diga um modo de Scan 
	Exemplo: 
	Simples = 1 
	Moderado = 2
	Completo = 3  ''' )
#para saber se no resultado do scan,sera mostrado as portas fechadas (abertas sempre mostrarao)
fechada = input("Mostrar portas fechadas? s/n: ")

tempo = float(input('''Qual o tempo de espera de cada porta? 
	Exemplo:
	0.1 <- Mais rápido (dependendo do caso pode ser menos eficaz)
	0.3 <- Medio(recomendado)
	0.5 <- Mais lento
	Velocidade: '''))
#Selecao dos modelos de scan do IP entrado pelo usuário
if scan == '1': ports = [21, 22, 25, 80, 443, 8080]
elif scan == '2': ports = [21, 22, 25, 53, 80, 110, 135, 137, 138, 139, 143, 443, 465, 587, 995, 1521, 2525, 3306, 8000, 8080]
elif scan == '3': ports = range(1, 65535)

#"validando" o ip de analise
try:
	ips = ipaddress.ip_network(ip_informado, strict=False)
except:
	print("IP Inválido")
	sys.exit()

#Scan
for ip in ips:
	print("Scanning", ip)
	for port in ports:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(tempo)
		code = s.connect_ex((str(ip), port))
		if code == 0:
			print("A Porta", port, "esta aberta")
		if fechada == "s":	
			if code > 0:
				print("A porta", port, "esta fechada")
		s.close()
