import argparse
import untangle
from models import ProductKey, Product

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merging multiple MSDN product key export XMLs.')
    parser.add_argument('INPUTS', nargs='*', help='Input files')
    parser.add_argument('--output', default='out.xml', help='Output path, default out.xml')
    args = parser.parse_args()
    docs = args.INPUTS
    out = args.output

    products = {}

    for f in docs:
        doc = untangle.parse(f)
        for product in doc.YourKey.Product_Key:
            name = product['Name']
            if name not in products:
                products[name] = Product(name)
            for key in product.Key:
                k = key.cdata
                if k not in products[name]:
                    products[name].Key[k] = ProductKey(key['ID'], key['Type'], key['ClaimedDate'], k)

    with open(out, 'w', encoding='utf-8') as f:
        f.write('<YourKey>\n')
        for key, value in products.items():
            f.write(str(value))
        f.write('</YourKey>\n')