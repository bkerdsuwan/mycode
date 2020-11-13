farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for elem_list in farms:
    for key in elem_list:
        if elem_list[key] == "NE Farm":
            #need line below to not print farm 
            if key == "agriculture":
                for produce in elem_list[key]:
                    if produce != "carrots" and produce != "celery":
                        print (produce, end = " ")
                print()

yucky = ["carrots", "celery"]

choice = int(input("Which farm do you want to check out? (0,1,2):"))

for x in farms[choice]["agriculture"]:
    if not x in yucky:
        print(x, end = " ")
print()

