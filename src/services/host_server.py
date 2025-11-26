import requests

def search_host_server(ip):

    print(f"[*] Buscando informações para: {ip}...")
    
    try:
        url = f"http://ip-api.com/json/{ip}"
        response_get = requests.get(url, timeout=5)
        data_response = response_get.json()
        
        if data_response['status'] == 'fail':
            return f"Erro: {data_response['message']}"
            
        return data_response .get('org') or data_response .get('isp')
        ''
    except Exception as e:
        return f"Erro de conexão: {e}"