import untangle
from models import ProductKey, Product

def merge(docs, out):
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