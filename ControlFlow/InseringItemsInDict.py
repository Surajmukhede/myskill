# there are two method to adding item to dict data type

# 1 By using setdefault function

clothes = {'pants':10,'shirt':15}
clothes.setdefault('tshirt',5)

print(clothes)


# 2 By using for if  method


clothes = {'pants':10,'shirt':15}

if 'tshirt' not in clothes:
    clothes['tshirt'] = 5
    print(clothes)