# Do not modify these lines
from xmlrpc.client import FastMarshaller
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        'name'          : name,
        'date_of_birth' : date_of_birth,
        'place_of_birth': place_of_birth,
        'height'        : height,
        'nationality'   : nationality
        }
    #print(passport)
    return(passport)

def add_stamp(passport, country):
    home_country = False
    stamps_exists_in_passport = False

    if country == passport['nationality']:
        #no stamp for home-country, do nothing
        home_country = True
    if passport.get('stamps', -1) == -1:
        stamps_exists_in_passport = False
        #no stamps exists in passport
    else:
        stamps_exists_in_passport = True

    if not home_country and not stamps_exists_in_passport:
        stamps = {
            'stamps':   [country]
            }
        passport.update(stamps)

    if not home_country and stamps_exists_in_passport and country not in passport['stamps']:
        passport['stamps'] += [country]
        #passport has stamp, but not yet this country. Add it
    return(passport)


def add_biometric_data(passport, type_bio_data, bio_data, date_bio_recording):
    
    if passport.get('biometric', -1) == -1:
        #biometric is new in passport.  Alternatief: if "biometric" not in passport:
        passport.update({'biometric': {}})
    passport['biometric'].update({type_bio_data: {'date': date_bio_recording, 'value': bio_data}})
    print(f"NIEUWE paspoort: {passport}")
    print(" ")
    return(passport)

passport = {
        'name'          : 'Peter',
        'date_of_birth' : '1971-12-25',
        'place_of_birth': 'Den Haag',
        'height'        : 1.71,
        'nationality'   : 'Belgium',
        'stamps'        : ['France', 'China']
        }

fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

#create_passport('Remko','1970-02-03', 'Voorburg', 1.89, 'Netherlands' )
#add_stamp(passport, 'Belgium')
#add_biometric_data(passport,'eye_color_left', 'brown', '2022-04-06')
add_biometric_data(passport,'finger_prints', fingerprint_data, '2022-05-05')