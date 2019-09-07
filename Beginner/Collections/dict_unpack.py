#Complete the favorite_food function below. It accepts a dictionary as an argument. 
#Your function should unpack that dictionary and pass it to the format method s keywords, then return the resulting string.

def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)
