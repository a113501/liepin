import random
import socket
import struct

def proxy():
    ALL_PROXIES = [
{"HTTP":"218.4.101.130:83"},
{"HTTP":"117.93.110.23:808"},
{"HTTP":"183.207.95.25:80"},
{"HTTP":"114.239.146.250:808"},
{"HTTP":"121.232.144.228:9000"},
{"HTTP":"183.207.95.18:8080"},
{"HTTP":"183.207.95.22:8080"},
{"HTTP":"218.92.219.86:8080"},
{"HTTP":"121.237.141.74:808"},
{"HTTP":"222.95.20.102:808"},
{"HTTP":"183.207.95.22:80"},
{"HTTP":"183.207.95.28:80"},
{"HTTP":"122.96.59.107:82"},
{"HTTP":"114.239.148.155:808"},
{"HTTP":"180.119.76.101:808"},
{"HTTP":"121.232.145.89:9000"},
{"HTTP":"121.232.146.66:9000"},
{"HTTP":"121.232.147.67:9000"},
{"HTTP":"183.207.95.21:80"},
{"HTTP":"183.207.95.24:8080"},
{"HTTP":"121.232.144.37:9000"},
{"HTTP":"122.96.59.107:83"},
{"HTTP":"121.232.147.69:9000"},
{"HTTP":"180.97.220.1:8081"},
{"HTTP":"121.232.145.92:9000"},
{"HTTP":"221.230.72.181:80"},
{"HTTP":"183.207.95.20:80"},
{"HTTP":"122.96.59.99:82"},
{"HTTP":"121.232.146.178:9000"},
{"HTTP":"61.160.190.34:8888"},
{"HTTP":"222.95.17.107:808"},
{"HTTP":"121.232.148.12:9000"},
{"HTTP":"180.108.64.163:808"},
{"HTTP":"180.108.46.146:808"},
{"HTTP":"221.229.45.193:808"},
{"HTTP":"121.232.148.95:9000"},
{"HTTP":"122.96.59.103:80"},
{"HTTP":"121.232.146.190:9000"},
{"HTTP":"222.185.23.129:808"},
{"HTTP":"180.125.31.133:808"},
{"HTTP":"222.94.148.60:808"},
{"HTTP":"222.94.144.92:808"},
{"HTTP":"121.232.146.39:9000"},
{"HTTP":"183.207.95.24:80"},
{"HTTP":"210.29.29.20:80"},
{"HTTP":"183.207.95.23:8080"},
{"HTTP":"121.232.144.205:9000"},
{"HTTP":"121.232.147.171:9000"},
{"HTTP":"202.119.162.138:80"},
{"HTTP":"183.207.95.25:8080"},
{"HTTP":"117.90.0.80:9000"},
{"HTTP":"121.232.144.24:9000"},
{"HTTP":"121.232.144.196:9000"},
{"HTTP":"117.91.138.168:808"},
{"HTTP":"121.232.145.113:9000"},
{"HTTP":"222.95.17.129:808"},
{"HTTP":"58.218.196.126:808"},
{"HTTP":"117.90.3.157:9000"},
{"HTTP":"121.232.145.31:9000"},
{"HTTP":"121.232.144.2:9000"},
{"HTTP":"117.90.0.41:9000"},
{"HTTP":"117.90.3.153:9000"},
{"HTTP":"210.29.26.250:80"},
{"HTTP":"183.207.95.19:8080"},
{"HTTP":"218.92.219.49:8080"},
{"HTTP":"114.239.0.62:808"},
{"HTTP":"222.94.151.39:808"},
{"HTTP":"117.81.29.60:808"},
{"HTTP":"183.207.95.21:8080"},
{"HTTP":"117.90.1.53:9000"},
{"HTTP":"117.90.137.229:9000"},
{"HTTP":"58.208.28.31:808"},
{"HTTP":"183.207.176.252:1080"},
{"HTTP":"183.207.95.18:80"},
{"HTTP":"218.94.242.34:808"},
{"HTTP":"58.221.38.170:8080"},
{"HTTP":"117.90.1.215:9000"},
{"HTTP":"114.217.97.109:808"},
{"HTTP":"121.232.145.67:9000"},
{"HTTP":"122.96.59.103:81"},
{"HTTP":"183.207.95.28:8080"},
{"HTTP":"121.232.146.122:9000"},
{"HTTP":"117.91.138.87:808"},
{"HTTP":"121.232.147.100:9000"},
{"HTTP":"121.232.147.219:9000"},
{"HTTP":"117.90.4.107:9000"},
{"HTTP":"183.207.95.19:80"},
{"HTTP":"121.232.144.155:9000"},
{"HTTP":"183.207.95.23:80"},
{"HTTP":"121.232.147.113:9000"},
{"HTTP":"183.207.95.20:8080"},
{"HTTP":"183.207.95.17:80"},
{"HTTP":"49.85.199.175:808"},
{"HTTP":"121.232.146.181:9000"},
{"HTTP":"210.29.26.144:80"},
{"HTTP":"58.221.38.70:8080"},
{"HTTP":"121.232.144.21:9000"},
{"HTTP":"121.232.144.234:9000"},
{"HTTP":"49.89.77.196:808"},
{"HTTP":"49.89.101.137:808"},
]
    ALL_PROXIESA = [{"HTTP":"218.191.247.51:80"},
{"HTTP":"183.207.95.22:80"},
{"HTTP":"121.11.65.6:8080"},
{"HTTP":"218.60.55.3:8080"},
{"HTTP":"183.207.95.18:8080"},
{"HTTP":"47.89.41.164:80"},
{"HTTP":"111.8.22.210:8080"},
{"HTTP":"111.23.10.174:80"},
{"HTTP":"60.178.6.104:8081"},
{"HTTP":"111.23.10.123:80"},
{"HTTP":"180.110.17.148:808"},
{"HTTP":"111.8.22.207:8080"},
{"HTTP":"183.156.174.55:808"},
{"HTTP":"117.63.193.80:808"},
{"HTTP":"125.89.122.230:808"},
{"HTTP":"103.235.245.35:8080"},
{"HTTP":"182.38.21.53:808"},
{"HTTP":"112.192.17.211:8118"},
{"HTTP":"175.155.224.13:808"},
{"HTTP":"106.46.3.221:808"},
{"HTTP":"117.135.198.66:80"},
{"HTTP":"123.206.6.17:808"},
{"HTTP":"117.95.66.67:808"},
{"HTTP":"180.110.133.196:808"},
{"HTTP":"61.130.97.212:8099"},
{"HTTP":"58.59.133.214:63000"},
{"HTTP":"220.194.213.52:8080"},
{"HTTP":"220.166.96.90:82"},
{"HTTP":"36.249.31.222:808"},
{"HTTP":"111.23.10.45:80"},
{"HTTP":"117.143.109.132:80"},
{"HTTP":"182.87.242.229:808"},
{"HTTP":"60.178.138.106:8081"},
{"HTTP":"119.6.87.191:8081"},
{"HTTP":"111.23.10.33:80"},
{"HTTP":"60.178.6.58:8081"},
{"HTTP":"101.67.249.3:80"},
{"HTTP":"182.87.239.172:808"},
{"HTTP":"119.48.13.192:8888"},
{"HTTP":"60.178.10.142:8081"},
{"HTTP":"121.226.153.12:808"},
{"HTTP":"111.23.10.10:8080"},
{"HTTP":"101.71.17.132:8081"},
{"HTTP":"111.23.10.27:8080"},
{"HTTP":"120.27.113.72:8888"},
{"HTTP":"124.42.7.103:80"},
{"HTTP":"210.29.26.144:80"},
{"HTTP":"221.14.7.241:8080"},
{"HTTP":"183.207.95.24:8080"},
{"HTTP":"123.56.237.57:80"},
{"HTTP":"111.8.22.211:80"},
{"HTTP":"121.193.143.249:80"},
{"HTTP":"58.210.202.234:808"},
{"HTTP":"114.238.62.101:808"},
{"HTTP":"111.23.10.51:8080"},
{"HTTP":"111.23.10.172:8080"},
{"HTTP":"222.33.192.238:8118"},
{"HTTP":"123.56.243.31:83"},
{"HTTP":"221.229.47.46:808"},
{"HTTP":"101.200.126.6:8080"},
{"HTTP":"182.42.37.129:808"},
{"HTTP":"112.91.135.184:8080"},
{"HTTP":"111.8.22.209:8080"},
{"HTTP":"117.143.109.157:80"},
{"HTTP":"111.23.10.47:80"},
{"HTTP":"58.221.38.70:8080"},
{"HTTP":"111.23.10.36:80"},
{"HTTP":"123.125.212.171:8080"},
{"HTTP":"182.87.240.79:808"},
{"HTTP":"60.178.11.170:8081"},
{"HTTP":"27.40.136.48:808"},
{"HTTP":"111.23.10.14:80"},
{"HTTP":"180.110.134.248:808"},
{"HTTP":"221.5.5.232:8081"},
{"HTTP":"47.52.3.230:443"},
{"HTTP":"60.169.5.68:8080"},
{"HTTP":"111.23.10.38:8080"},
{"HTTP":"121.232.144.197:9000"},
{"HTTP":"111.23.10.26:8080"},
{"HTTP":"120.199.64.163:8081"},
{"HTTP":"106.3.129.108:80"},
{"HTTP":"113.252.129.133:8383"},
{"HTTP":"60.167.20.242:808"},
{"HTTP":"47.52.33.227:443"},
{"HTTP":"114.230.107.172:808"},
{"HTTP":"162.105.75.105:80"},
{"HTTP":"183.207.95.17:8080"},
{"HTTP":"121.10.1.181:8080"},
{"HTTP":"120.83.120.29:808"},
{"HTTP":"60.178.4.210:8081"},
{"HTTP":"111.23.10.36:8080"},
{"HTTP":"114.230.106.107:808"},
{"HTTP":"125.89.124.204:808"},
{"HTTP":"175.155.154.124:808"},
{"HTTP":"175.155.138.11:808"},
{"HTTP":"182.45.92.10:808"},
{"HTTP":"113.123.36.100:808"},
{"HTTP":"59.62.42.225:808"},
{"HTTP":"113.122.150.217:808"},
{"HTTP":"111.23.10.34:80"}]
    random_one = random.choice(ALL_PROXIESA)
    return random_one

def user_agent(**type):
    USER_AGENTS_PC = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",

    ]
    USER_AGENTS_MOBILE = [
        'Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Letv X501 Build/DBXCNOP5501304131S) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.800 U3/0.8.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 5.1.1)',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/13D15 UCBrowser/10.9.15.793 Mobile',
        'Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.7 Mobile/13D15 Safari/8536.25 MttCustomUA/2',
        'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MX4 Pro Build/LMY48W) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.800 U3/0.8.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m2 note Build/LMY47D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.10.788 U3/0.8.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; CHM-CL00 Build/CHM-CL00) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/7.1 (Baidu; P1 4.4.4)',
        'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 MxBrowser/4.5.9.3000',
        'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    ]
    if type == 'mobile':
        random_one = random.choice(USER_AGENTS_MOBILE)
    elif type == 'pc':
        random_one = random.choice(USER_AGENTS_PC)
    else:
        USER_AGENTS_ALL = USER_AGENTS_MOBILE + USER_AGENTS_PC
        random_one = random.choice(USER_AGENTS_ALL)
    return random_one

def random_ip():
    RANDOM_IP_POOL = ['192.168.10.222/0']
    str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | (1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

def headers(user_agent_type='',**kw):
    headers = {
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent	': user_agent(user_agent_type),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-Forwarded-For': random_ip(),
        'Host':'',
        'Accept-Encoding':'',
        'Referer':'',
    }
    if 'Cache-Control' in kw:
        headers['Cache-Control'] = kw['Cache-Control']
    if 'Connection' in kw:
        headers['Connection'] = kw['Connection']
    if 'Host' in kw:
        headers['Host'] = kw['Host']
    if 'Referer' in kw:
        headers['Referer'] = kw['Referer']
    if 'Accept-Encoding' in kw:
        headers['Accept-Encoding'] = kw['Accept-Encoding']

    return headers



if __name__=='__main__':
    pass

