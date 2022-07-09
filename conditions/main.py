# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action (weather, time_of_day, cow_milking_status, cow_location, season, slurry_tank, grass_status):
    if cow_location == 'pasture' and (weather == 'rainy' or time_of_day == 'night'):  
        return('take cows to cowshed')
    elif cow_milking_status == True: 
        if cow_location == 'pasture':
            return('take cows to cowshed\nmilk cows\ntake cows back to pasture')
        elif cow_location == 'cowshed':
            return('milk cows')
        else: return('cow location unknow')
    elif slurry_tank == True and weather != 'sunny' and weather != 'windy':
        if cow_location == 'pasture':
            return('take cows to cowshed\nfertilize pasture\ntake cows back to pasture')
        elif cow_location == 'cowshed':
            return('fertilize pasture')
        else: return('cow location unknow')
    elif grass_status == True and season == 'spring' and weather == 'sunny':
        if cow_location == 'pasture':
            return('take cows to cowshed\nmow grass\ntake cows back to pasture')
        elif cow_location == 'cowshed':
            return('mow grass')
        else: return('cow location unknow')
    else: return('wait')
