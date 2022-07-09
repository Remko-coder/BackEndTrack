# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print(f"Leek is {leek_price} euro per kilo.")
order = 'leek 4'
amount_leek_ordered = int(order[order.find(" ") + 1:])
sum_total = leek_price * amount_leek_ordered
print(sum_total)
broccoli_price = 2.34
amount_broccoli_ordered = 1.6
tot_broccoli_price = round(broccoli_price * amount_broccoli_ordered, 2)
print(f"{amount_broccoli_ordered}kg broccoli costs {tot_broccoli_price}e")