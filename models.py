class ProductKey:
    Id = ''
    Type = ''
    ClaimedDate = ''
    Key = ''
    def __init__(self, id, ty, date, key):
        self.Id = id
        self.Type = ty
        self.ClaimedDate = date
        self.Key = key
    def __str__(self):
        return '<Key ID="{}" Type="{}" ClaimedDate="{}">{}</Key>\n'.format(self.Id, self.Type, self.ClaimedDate, self.Key)

class Product:
    Name = ''
    Key = {}
    def __init__(self, name):
        self.Key = {}
        self.Name = name
    def __len__(self):
        return len(self.Key)
    def __str__(self):
        s = '  <Product_Key Name="{}">\n'.format(self.Name)
        for key, value in self.Key.items():
            s += '    {}'.format(str(value))
        s += '  </Product_Key>\n'
        return s
    def __contains__(self, item):
        return item in self.Key