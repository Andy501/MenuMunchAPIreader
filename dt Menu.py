import datetime
import urllib #docs
import json
#https://rapidapi.com/spoonacular/api/recipe-food-nutrition

def main():
    #url = website full url
    #how to interact with api
    today = datetime.datetime.today().weekday() #day of the week as integer 0 through 6
    print(today)
    '''json_obj = urllib.urlopen(url)
    data = json.load(json_obj)
    Menu_Option()'''
    this_day = Named_Day(today)
    print (this_day)

#Odd = vegan food random choice. is it possible to search api with terms.randomschoice x =[brown rice, potatoes], y =[edamame, black beans]
#Even = meat food


def Menu_Options():
    if today % 2 == 0:
        print ("IS Even Meat API or webscrape")
    else:
        print ("IS ODD Vegan API or webscrape")

def Named_Day(today):
    if today == 0:
        day = "MONDAY"

    if today == 1:
        day = "TUESDAy"

    if today == 2:
        day = "WENDSDAY"

    if today == 3:
        day = "THURSDAY"

    if today == 4:
        day = "FRIDAy"

    if today == 5:
        day = "SATURDAY"

    if today == 6:
        day = "SUNDAY"

    return day

if __name__ == '__main__':
    main()
