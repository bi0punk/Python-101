import pandas as pd

clients = [
    {
        "Personal_Data": {
            "First_name": "Pedro",
            "Last_name": "Aguilar",
            "Phone": "+569888888",
            "Address": "Fake street 396, NY",
            "Email": "fake@fake.com",
            "Account_id": "325452",
            "VIP_FLG": "1",
            "Shipping_Address": "Fake street 398, NY"
        },
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
    }
]

# Crear un DataFrame de pandas a partir de la lista de diccionarios 'clients'
df = pd.DataFrame.from_records(
    [
        {
            'First_name': client['Personal_Data']['First_name'],
            'Last_name': client['Personal_Data']['Last_name'],
