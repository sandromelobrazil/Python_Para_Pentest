import Pyro4, crack

uri = "PYRO:dist@192.168.0.3:666" #1
proxy = Pyro4.Proxy(uri) #2

(ssid, aNonce, sNonce, apMac, cliMac, \
frame802_1, frame802_2, frame802_3, mic1, mic2, mic3) = proxy.pega_info() #3

crack.info(ssid, aNonce, sNonce, apMac, cliMac, \
frame802_1, frame802_2, frame802_3, mic1, mic2, mic3) #4

while True:
    if proxy.verifica_se_achou_a_senha(): #5
        break
    else:
        try:
            psk = proxy.quebra() #6
            quebrou = crack.RunTest(psk) #7
            if quebrou: #8
                proxy.achou(quebrou) #9
            proxy.incrementa_listaAuxiliar(psk) #10

        except KeyError: #11
            break

        except Exception as e: #12
            print e