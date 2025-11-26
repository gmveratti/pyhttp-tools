import requests
import json

def get_json_response(url):
    print(f"[*] Buscando JSON em: {url}...")
    
    # 1. Garante que a URL tenha esquema (http ou https)
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        # Faz a requisição
        response = requests.get(url, timeout=10)
        
        # 2. Tenta converter para JSON
        # Se o site retornar HTML (ex: google.com), isso vai dar erro e cair no except
        dados = response.json()
        
        # 3. Retorna uma string formatada (bonita) em vez de dicionário puro
        return json.dumps(dados, indent=4, ensure_ascii=False)
        
    except requests.exceptions.JSONDecodeError:
        return "Erro: O servidor retornou dados, mas NÃO é um JSON válido (provavelmente é HTML)."
    except requests.exceptions.ConnectionError:
        return "Erro: Falha na conexão (Verifique a URL ou sua internet)."
    except Exception as e:
        return f"Erro inesperado: {e}"