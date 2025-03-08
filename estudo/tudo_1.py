import json


produtos = [
    {"produto": "Dell Laptop", "Preço": 15000},
    {"produto": "HP Desktop", "Preço": 12000},
    {"produto": "MacBook Pro", "Preço": 25000},
    {"produto": "Lenovo ThinkPad", "Preço": 13000},
    {"produto": "Acer Monitor", "Preço": 3000},
    {"produto": "Samsung SSD", "Preço": 5000},
    {"produto": "Logitech Mouse", "Preço": 150},
    {"produto": "Logitech Teclado", "Preço": 200},
    {"produto": "Canon Printer", "Preço": 3500},
    {"produto": "Sony Headphones", "Preço": 1200},
    {"produto": "Bose Speakers", "Preço": 5000},
    {"produto": "Microsoft Surface", "Preço": 22000}
]


# for produto in produtos:
#     print(f'O produto {produto['produto']}, preço: {produto['Preço']}')


primeiro_produto = produtos[0]

print(f'O produto {primeiro_produto['produto']}, preço: {primeiro_produto['Preço']}')