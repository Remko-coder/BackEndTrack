# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(film_names_input):
    return(sorted(film_names_input))

def won_golden_globe(film_name):
    golden_globe_awards = ['jaws', 'star wars: episode IV - a new hope', 'e.t. the extra-terrestrial', 'memoirs of a geisha']
    if film_name.lower() in golden_globe_awards:
        return(True)
    else: 
        return(False)

# uitproberen met for-loop:  remove werkt op alle lijsten. Beetje vreemd
#def remove_toto_albums(list_songs):
#    toto_albums = ['Fahrenheit', 'The Seventh One','Falling in Between', 'Toto XX', 'Toto XIV', 'Old Is New']
#    compare_list = list_songs
#    end_loop = len(list_songs) - 1
#    for i in range(0, end_loop):
#        if list_songs[i] in toto_albums:
#            print(f"teller: {i}, {list_songs[i]} ")
#            remove_value = list_songs[i]
#            compare_list.remove(remove_value)
#    return(compare_list)

# uitproberen met for-loop:  remove werkt op alle lijsten. Beetje vreemd
'''def remove_toto_albums(list_songs):
    toto_albums = ['Fahrenheit', 'The Seventh One','Falling in Between', 'Toto XX', 'Toto XIV', 'Old Is New']
    old_list = list_songs
    end_loop = len(old_list) - 1
    nieuwe_lijst = []
    print(f"end_loop: {end_loop}")
    for i in range(0, end_loop):
        print(f"teller: {i}, old_list = {old_list[i]} ")
        if old_list[i] in toto_albums:
            print(f"match: {old_list[i]} ")
            #compare_list.remove(toto_albums[i])
        else:
            print(f"GEEN match: {old_list[i]} ")
            nieuwe_lijst += old_list[i]
            print(f"nieuw lijst: {nieuwe_lijst}")
    return(compare_list)

nieuwe_lijst = ['abc', 'Fahrenheit', 'def', 'ghi', 'Toto XX', 'xyz']
print(nieuwe_lijst)
remove_toto_albums(nieuwe_lijst )
'''        
def remove_toto_albums(list_songs):
    toto_albums = ['Fahrenheit', 'The Seventh One','Falling in Between', 'Toto XX', 'Toto XIV', 'Old Is New']
    if 'Fahrenheit' in list_songs:
        list_songs.remove('Fahrenheit')
    if 'The Seventh One' in list_songs:
        list_songs.remove('The Seventh One')
    if 'Falling in Between' in list_songs:
        list_songs.remove('Falling in Between')
    if 'Toto XX' in list_songs:
        list_songs.remove('Toto XX')
    if 'Toto XIV' in list_songs:
        list_songs.remove('Toto XIV')
    if 'Old Is New' in list_songs:
        list_songs.remove('Old Is New')
    return(list_songs)
   
nieuwe_lijst = ['abc', 'Fahrenheit', 'def', 'ghi', 'Toto XX', 'xyz']
remove_toto_albums(nieuwe_lijst )

