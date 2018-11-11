import ctypes
#Adaptacao: https://msdn.microsoft.com/en-us/library/windows/desktop/ms645505%28v=vs.85%29.aspx

botao = {
    'MB_ABORTRETRYIGNORE'  : 0x00000002L,
    'MB_CANCELTRYCONTINUE' : 0x00000006L,
    'MB_HELP'              : 0x00004000L,
    'MB_OK'                : 0x00000000L,
    'MB_OKCANCEL'          : 0x00000001L,
    'MB_RETRYCANCEL'       : 0x00000005L,
    'MB_YESNO'             : 0x00000004L,
    'MB_YESNOCANCEL'       : 0x00000003L
    } #1

icone = {
    'MB_ICONEXCLAMATION' : 0x00000030L,
    'MB_ICONWARNING'     : 0x00000030L,
    'MB_ICONINFORMATION' : 0x00000040L,
    'MB_ICONASTERISK'    : 0x00000040L,
    'MB_ICONQUESTION'    : 0x00000020L,
    'MB_ICONSTOP'        : 0x00000010L,
    'MB_ICONERROR'       : 0x00000010L,
    'MB_ICONHAND'        : 0x00000010L,
    } #2

botaoPadrao = {
    'MB_DEFBUTTON1' : 0x00000000L,
    'MB_DEFBUTTON2' : 0x00000100L,
    'MB_DEFBUTTON3' : 0x00000200L,
    'MB_DEFBUTTON4' : 0x00000300L,
    } #3

texto = u"Mensagem qualquer"
titulo = u"Titulo qualquer"
retorno = ctypes.windll.user32.MessageBoxW(0, texto, titulo, botao["MB_YESNO"]) #4
if retorno == 6: #5
    print "O usuario clicou no botao YES"
elif retorno == 7: #6
    print "O usuario clicou no botao NO"

texto = u"Mensagem de Warning"
titulo = u"Warning"
ctypes.windll.user32.MessageBoxW(0, texto, titulo,
                                    botao["MB_RETRYCANCEL"] |
                                    icone["MB_ICONWARNING"]) #7

texto = u"Mensagem de Erro"
titulo = u"Error"
ctypes.windll.user32.MessageBoxW(0, texto, titulo,
                                    botao["MB_ABORTRETRYIGNORE"] |
                                    icone["MB_ICONERROR"] |
                                    botaoPadrao["MB_DEFBUTTON2"]) #8

texto = u"Mensagem de Erro 2"
titulo = u"Error 2"
ctypes.windll.user32.MessageBoxW(0, texto, titulo,
                                    botao["MB_ABORTRETRYIGNORE"] |
                                    botaoPadrao["MB_DEFBUTTON3"]) #9