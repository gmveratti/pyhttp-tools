# main.py
import sys
from src.args import setup_parser

from src.services.host_server import search_host_server
from src.services.search_ip import get_ip_from_url
from src.services.http_service import get_json_response

def main():
    
    parser = setup_parser()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.iphostserver:
        resultado = search_host_server(args.iphostserver)
        print(f"\nResultado:\nHost: {resultado}")

    if args.searchipbyurl:
        resultado = get_ip_from_url(args.searchipbyurl)
        print(f"\nResultado:\nIP: {resultado}")

    if args.json_url:
        resultado = get_json_response(args.json_url)
        print("\n--- Resposta JSON ---")
        print(resultado)



if __name__ == "__main__":
    main()