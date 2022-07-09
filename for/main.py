from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def shortest_names(list_countries):
    list_short_country_names = []
    for name in list_countries:
        if len(name) < 5:
            list_short_country_names.append(name)
    #print(f"de lijst met korte landen: {list_short_country_names}")
    return(list_short_country_names)

def most_vowels(list_countries):
    list_countries_vowel_count = []
    for name in list_countries:
        #count vowels
        name_tmp = name.lower()
        count = 0
        for letter in name_tmp:
            if letter in 'aeiou':
                count += 1
        list_countries_vowel_count.append([name, count])
        #schrijf in nieuwe lijst: country + klinker-aantal
    #print(f"VOOR: {list_countries_vowel_count}")
    
    # sorting on 2nd column, reversed = highest first
    sorted_list_countries = sorted(list_countries_vowel_count, key=lambda x: x[1], reverse=True)
    # select first 3 countries
    top_three = []
    for i in range(3):
        print(f" test: {sorted_list_countries[i][0]}")
        top_three.append(sorted_list_countries[i][0])
     #return eerste 3
    #print(f" EIND RESULTAAT: {top_three}")
    return(top_three)

def alphabet_set(list_countries):
    #order country-list for most distinct letters (high to low)
    amount_different_letters = 0
    list_countries_different_vowels = []
    for name in list_countries:
        #count vowels
        name_tmp = ""
        for ch in name:
            if ch.isalpha():
                name_tmp += ch.lower() 
        different_letters = ''.join(set(name_tmp))
        
        amount_different_letters = len(set(name_tmp))
        list_countries_different_vowels.append([name, different_letters, amount_different_letters])
        different_letters = ""
        amount_different_letters = 0

        #schrijf in nieuwe lijst: country + klinker-aantal
    # sorting on 3rd column, reversed = highest first
    sorted_list_countries = sorted(list_countries_different_vowels, key=lambda x: x[2], reverse=True)
    
    #sorted list available: country_name, different letters, amount different letters
    #find all distinct letters from the alphabet, and check how many countries it takes to do so 
    letter = []
    country_counter = 0
    country_checked = False
    checked_country_list = []
    for country in sorted_list_countries:
        #print(country)
        for ch in range(len(country[1])):
            #print(f" in loopje {country[1][ch]}")
            if country[1][ch] in letter:
                continue
            else:
                letter += country[1][ch]
                country_checked = True
        if country_checked:
            country_counter += 1
            country_checked = False
            country_tmp = country[0]
            #print(f"land geteld, namelijk: {country_tmp}")
            checked_country_list.append(country_tmp)
        
    #print(f"TOTAAL landen: {country_counter}")
    #print(checked_country_list)
    return(checked_country_list)


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)    
    most_vowels(countries)
    alphabet_set(countries)