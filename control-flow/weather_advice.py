weather = input("what's the weather like today?(sunny/rainy/cold): ").lower()
if weather == "sunny":
    print("wear a t-shirt and sunglasses") 
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat")
elif weather == "cold": 
    print("Make sure to wear a warm coat and a scarf.") 
else:
    print("sorry, i don't have recommendations for that weather.")