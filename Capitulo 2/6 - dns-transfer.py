# -*- coding: utf-8 -*-
import dns.query
import dns.zone
import dns.resolver

dominio = "dominio.com"
registrosNS = dns.resolver.query(dominio, "NS") #1
lista = []

for registro in registrosNS: #2
    lista.append( str(registro) )

for registro in lista:
    try:
        transferenciaZona = dns.zone.from_xfr(dns.query.xfr(registro, dominio)) #3
    except:
        print "Erro na transferência de zona"
    else: 
        registroDNS = transferenciaZona.nodes.keys()
        registroDNS.sort()
        for n in registroDNS:
            print transferenciaZona[n].to_text(n)