import argparse
from functions import merge

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merging multiple MSDN product key export XMLs.')
    parser.add_argument('INPUT', nargs='*', help='Input files')
    parser.add_argument('--output', default='output.xml', help='Output path, default output.xml')
    args = parser.parse_args()
    docs = args.INPUT
    if not docs:
        print('No input file specified.')
        exit()
    out = args.output
    merge(docs, out)