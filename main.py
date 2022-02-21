print('Lista zakupów')
shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
shopping_list["drogeria"] = ["szampon", "mydło", "waciki"]
suma=0

for shops, products in shopping_list.items():
    
    shops= shops.title()
    products = [product.title() for product in products]
    print(f"Idę do {shops} i kupuję tam {products}")
    for product in products:
       suma = suma + 1
print(f"W sumie kupuję {suma} produktów")

