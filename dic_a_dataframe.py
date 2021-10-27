


import pandas as pd
clients = [{
        "Personal_Data": [
            {
                "First_name": "Pedro",
                "Last_name": "Aguilar",
                "Phone": "+569888888",
                "Address": "Fake street 396, NY",
                "Email": "fake@fake.com",
                "Account_id": "325452",
                "VIP_FLG": "1",
                "Shipping_Address": "Fake street 398, NY"
            }
        ],
        "Order": [
            {
                "OrderID": "12345",
                "products": [
                    {
                        "sku": 43900,
                        "name": "Duracell - AAA Batteries (4-Pack)",
                        "type": "HardGood",
                        "price": 5.49,
                        "upc": "041333424019",
                        "category": [
                            {
                                "id": "pcmcat312300050015",
                                "name": "Connected Home & Housewares"
                            },
                            {
                                "id": "pcmcat248700050021",
                                "name": "Housewares"
                            },
                            {
                                "id": "pcmcat303600050001",
                                "name": "Household Batteries"
                            },
                            {
                                "id": "abcat0208002",
                                "name": "Alkaline Batteries"
                            }
                        ],
                        "shipping": 5.49,
                        "description": "Compatible with select electronic devices; AAA size; DURALOCK Power Preserve technology; 4-pack",
                        "manufacturer": "Duracell",
                        "model": "MN2400B4Z",
                        "url": "http://www.bestbuy.com/site/duracell-aaa-batteries-4-pack/43900.p?id=1051384074145&skuId=43900&cmp=RMXCC",
                        "image": "http://img.bbystatic.com/BestBuy_US/images/products/4390/43900_sa.jpg"
                    }
                ]
            }
        ]
    }]

nuevo_diccionario={}

for di in clients:
    nuevo_diccionario[di['First_name']]={}
    for k in di.keys():
        if k =='First_name': continue
        nuevo_diccionario[di['First_name'][k]]=di[k]

print(nuevo_diccionario)

""" df = pd.DataFrame([key for key in clients.keys()], columns=['Name'])
df['First_name'] = [value['First_name'] for value in clients.values()]
df['Last_name'] = [value['Last_name'] for value in clients.values()]
df['Phone'] = [value['Phone'] for value in clients.values()]
df['Address'] = [value['Address'] for value in clients.values()]
df['Email'] = [value['Email'] for value in clients.values()]
df['Acount_id'] = [value['Acount_id'] for value in clients.values()]
df['VIP_FLG'] = [value['VIP_FLG'] for value in clients.values()]
df['Shipping_Adress'] = [value['Shipping_Adress'] for value in clients.values()]
print(df)
 """




























""" clientes = {
    "Waldon Astling": 1.83,
    "Catherine MacTerlagh": 0.15,
    "Gusty Wondraschek": 9.19,
    "Arepico": 3.33,
    "Lois Vaan": 1.28,
    "Baird Eberts": 0.82,
    "Amalia Flieg": 2.88,
    "Leontine Wildbore": 9.44,
    "Rikki Chasteney": 7.01,
    "Augustine Papierz": 0.22,
    "Maynord Lawrance": 0.33

}


df = pd.DataFrame([[key, clientes[key]] for key in clientes.keys()], columns=['Name', 'Amount'])
print(df)


 """