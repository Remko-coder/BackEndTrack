# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
PlayerScored0 = 'Ruud Gullit' 
PlayerScored1 = 'Marco van Basten' 
goal_0 = 32
goal_1 = 54
scorers = PlayerScored0 + " " + str(goal_0) + ", " + PlayerScored1 + " " + str(goal_1)
#print(scorers)
#report = print(f"{PlayerScored0} scored in the {goal_0}nd minute \n{PlayerScored1} scored in the {goal_1}th minute")
#report = print(f"{PlayerScored0} scored in the {goal_0}nd minute \n{PlayerScored1} scored in the {goal_1}th minute")
#report = f"{PlayerScored0} scored in the {goal_0}nd minute \n{PlayerScored1} scored in the {goal_1}th minute"
report = PlayerScored0 + " scored in the " + str(goal_0) + "nd minute\n" + PlayerScored1 + " scored in the " + str(goal_1) +"th minute"
print(report)
player = 'Igor Belanov'
first_name = player[0:player.find(" ")]
last_name_len = len(player[(player.find(" ")+1) :])
name_short = first_name[0:1] + ". " + player[-7:]
chant_0 = (first_name + '! ') * len(first_name) 
chant = chant_0[:len(chant_0) - 1]
#print(chant, " ", len(chant))
good_chant = (chant[-1] != " ") 
#print(good_chant)