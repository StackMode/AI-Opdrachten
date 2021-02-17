import pymongo

myclient = pymongo.MongoClient("mongodb+srv://StackMode:Gaming1.0@huwebshop.vcizg.mongodb.net")
mydb = myclient["huwebshop"]
mycol = mydb["products"]

def eerste_product():
    prijs = mycol.find_one({},{"_id": 0, "price": 1})
    naam = mycol.find_one({}, {"_id": 0, "name": 1})
    return 'De naam en de prijs van het eerste product zijn:\n' + naam.get('name') + ' & ' + (str(prijs['price']['selling_price']) + ' euro.')


def naam():
    for namen in mycol.find({}, {"_id": 0,"name": 1}):
        for naam in namen.values():
            if naam[0] == 'R':
                return '\nDe naam van het eerste product dat begint met de letter "R" is:\n' + naam

def gemiddelde_berekenen():
    prijslijst = []
    prijzen = []
    som = 0
    for product in mycol.find():
        prijslijst.append(product['price'])
    for prijs in prijslijst:
        prijzen.append(prijs['selling_price'])
    for x in prijzen:
        som += x
    gemiddelde = som / len(prijzen)
    return '\nHet gemiddelde van alle prijzen is:\n' + str(gemiddelde) + ' euro.'


print(eerste_product())
print(naam())
print(gemiddelde_berekenen())