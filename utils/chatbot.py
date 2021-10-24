
def get_answer(input_):
    keywords = [["menu","There is a second window open, displaying the menu!"],
                ["menu good","We recommend a cheese chilli toast for starters, with cheese lasagna as the main course."],
                ["menu best","We recommend a cheese chilli toast for starters, with cheese lasagna as the main course."],
                ["menu recommend","We recommend a cheese chilli toast for starters, with cheese lasagna as the main course."],
                ["menu recommend","We recommend a cheese chilli toast for starters, with cheese lasagna as the main course."],
                ["wi-fi wifi password","The password is password12345"],
                ["vegetables come","We have our own farm yard, we only take the best vegetables for your taste!"],
                ["wine beer","I'm sorry but we don't allow alcohol in this restaurant."],
                ["when food arrive","We have the best chefs that make sure that the food will come, indeed, very fast."],
                ["when food come","We have the best chefs that make sure that the food will come, indeed, very fast."],
                ["carry","Yes sure! We will pack the dish for you!"],
                ["take","Yes sure! We will pack the dish for you!"],
                ["pack","Yes sure! We will pack the dish for you!"],
                ["water","Here you go!"],
                ["time open","We open from 8 am."],
                ["time close","We close at 11 pm"],
                ["timing","We open from 8 am and close at 11 pm"],
                ["manager","Hi karen, I am the manager and i can kick you out anytime i want"],
                ["cooked more","Sorry! We will have it heated immediately."],
                ["owner","Owners are Shaurya and Neil. I think they're a little busy coding though.."],
                ["card","Of course!"],
                ["paypal","Of course!"],
                ["cash","Of course!"],
                ["payment accept","We accept card,paytm,cash,paypal."],
                ["good","Thank you!"],
                ["who you","Max"],
                ["name","Max"],
                ["cost","The prices are written in the menu and are also confirmed when you order the dish"]]
    
    input_ = input_.lower()
    
    menu = [["chilli cheese toast",1.50],["falafel",1.70],
             ["cheese sticks",1.99],["bread with cheese dip",2.50],
             ["cheese toast",1.99],["cheese samples",1.50],
             ["cheese lasagna",1.30],["cheese parantha",1.70],
             ["cheese pasta",1.00],["cheese grill sandwich",1.80],
             ["chicken",3.99],["roast beef",4.99],
             ["ham and cheese",3.99],["smoked salmon",5.99],
             ["mango cheesecake",1.50],["egg cheesecake",1.30],
             ["apple pie",1.00],["soda",1.30],["juice",1.50],["iced tea",1.50],
             ["coffee iced",1.00],["coffee hot",1.00],["cold coffee",1.00],
             ["milk",1.30],["hot chocolate",1.50]]
    scores = []
    for i in menu:
        s = 0
        for j in i[0].split():
            if j in input_:
                s+=1
            else:
                s-=1
        scores.append(s)
    scores2 = []
    
    for i in keywords:
        s = 0
        for j in i[0].split():
            if j in input_:
                s+=1
            else:
                s-=1
            
        scores2.append(s)
    if max(scores2) > max(scores):
        return [keywords[scores2.index(max(scores2))][1],1]
    if max(scores2) < max(scores):
        return [menu[scores.index(max(scores))],0]
    elif sum(scores) == 0 and sum(scores2) == 0:
        return None
    
               
             
    

