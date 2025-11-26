import socket
from urllib.parse import urlparse

def get_ip_from_url(url):
    print(f"[*] Resolvendo IP para: {url}...")
    
    try:

        hosturl = urlparse(url).netloc or url

        if hosturl.endswith('/'):
            hosturl = hosturl[:-1]

        ip = socket.gethostbyname(hosturl)
        return ip
        
    except socket.gaierror:
        return "Erro: Não foi possível resolver o hostname (verifique a URL ou conexão)."
    
    except Exception as e:
        return f"Erro inesperado: {e}"