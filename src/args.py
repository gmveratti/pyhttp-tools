import argparse

def setup_parser():
    parser = argparse.ArgumentParser(
        prog='pyhttp',
        description='PyHTTP - CLI Tool',
        usage='%(prog)s [options] <argument>'
    )

    group_network = parser.add_argument_group('Network Tools')

    group_network.add_argument(
        '-sS', '--search-server', 
        dest='iphostserver', 
        type=str,
        help='Search ServerHost by IP (Ex: 8.8.8.8)'
    )
    
    group_network.add_argument(
        '-sIP', '--search-IP', 
        dest='searchipbyurl', 
        type=str,
        help='Search IP by url (google.com)'
    )

    return parser