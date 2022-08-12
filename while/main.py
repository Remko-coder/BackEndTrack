from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


""" Write your functions here. """
def unique_koala_facts(input_max):
    unique_facts_list = []
    num_fact = 0 
    i = 0
    while i < 1000 and num_fact < input_max:
        fact = random_koala_fact()
        i += 1
        if fact in unique_facts_list:
            #already know
            continue
        else:
            #unknown so far
            unique_facts_list.append(fact)
            num_fact += 1
            #print(f"num_fact= {num_fact} < {input_max}")
            #print(" ")
            #print(f"eindtotaal: {num_fact}")
    return(num_fact)

def num_joey_facts():
    joey_num_fact = 0
    unique_facts_list = []
    particular_fact = random_koala_fact()
    particular_count = 0
    i = 0

    while particular_count < 10 and i < 1000:
        fact = random_koala_fact()
        i += 1
        if fact == particular_fact:
            particular_count += 1
            #print(f" teller: {i} {particular_count} {fact} en {particular_fact}")
        if fact in unique_facts_list:
            #already know
            continue
        else:
            #unknown so far
            unique_facts_list.append(fact)
            if 'joey' in fact:
                joey_num_fact += 1       
    #print(f"joey_eind: {joey_num_fact}")
    return(joey_num_fact)

def koala_weight():
    weight_known = False

    while weight_known == False:
        fact = random_koala_fact()
        if 'kg' in fact:
            #print(F"gevonden: {fact}")
            weight_known = True
            position_in_string = fact.find('kg')
            weight_koala = int(fact[position_in_string-2:position_in_string])
            #print(weight_koala)
    return(weight_koala)

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    #print(unique_koala_fact())

    """ Write the calls to your functions here. """
    unique_koala_facts(15)
    num_joey_facts()
    koala_weight()