import argparse

def main():
    parser = argparse.ArgumentParser(description='IDK')
    parser.add_argument('-q', '--quiet', help='Nomes mostra els errors i el missatge de acabada per pantalla.', action="store_false")
    parser.add_argument('-v', '--versio', help='Mostra la versio', action='version', version='pyproject vs0.1')
    args = parser.parse_args()





main()