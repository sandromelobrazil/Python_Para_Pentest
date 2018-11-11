from scapy.all import *
conf.verb = 0

#Pacotes do tipo ICMP
ICMPechoRequest = IP(dst="192.168.0.1")/ICMP()
ICMPechoReply = IP(dst="192.168.0.1")/ICMP(type=0, code=0)
ICMPtimestampRequest = IP(dst="192.168.0.1")/ICMP(type=13, code=0)
ICMPpayload = IP(dst="192.168.0.1")/ICMP()/"Insira o payload desejado"

#Pacote TCP com a flag SYN
pacoteTCP = IP(dst="192.168.0.1")/TCP(flags="S")

#Pacote TCP com a flag SYN, payload desejado e porta de origem 666
pacoteTCP = IP(dst="192.168.0.1")/TCP(sport=666)/"Payload"

#Pacote TCP com a flag SYN e destino a porta 80
pacoteTCP2 = IP(dst="192.168.0.1")/TCP(dport=80)

#Pacote TCP com a flag SYN e destino as portas 23 e 80
pacoteTCP3 = IP(dst="192.168.0.1")/TCP(dport=[23,80])

#Pacote TCP com a flag SYN, destino a porta 80 e IPs 192.168.0.1 e 192.168.0.2
pacoteTCP4 = IP(dst=["192.168.0.1", "192.168.0.2"])/TCP(dport=80)

#Pacote TCP com a flag ACK
pacoteTCP = IP(dst="192.168.0.1")/TCP(flags="A")

#Pacote TCP com as flags SYN/ACK
pacoteTCP = IP(dst="192.168.0.1")/TCP(flags="SA")

#Pacote TCP com IP de origem falso
pacoteTCP = IP(src="6.6.6.6")/TCP()

#Pacote UDP com destino a porta 53
pacoteUDP = IP(dst="192.168.0.1")/UDP(dport=53)

#Pacote UDP com destino a porta 53 e porta de origem 666
pacoteUDP2 = IP(dst="192.168.0.1")/UDP(dport=53, sport=666)