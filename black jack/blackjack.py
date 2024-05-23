import random

valörer = ['hjärter', 'spader', 'ruter', 'klöver']
värden = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'knäckt', 'dam', 'kung', 'ess']

kortlek = []

for valör in valörer:
    for värde in värden:
        kortlek.append (f'{valör} {värde}')

random.shuffle(kortlek)

def deal_kort (kortlek: list, hand: list):
    kort = kortlek[0]
    kortlek.pop(0)
    hand.append(kort)

def calculate_hand_value(hand):
    value = 0
    får_ace = False 

    for kort in hand:
        värde = kort.split()[1]

        if isinstance(värde, int):
            value += int(värde)
        elif värde in ['dam', 'kung', 'knäckt']:
            value += 10
        elif värde == 'ess':
            får_ace = True
            value += 11
    if får_ace and value > 21:
        value -= 10
    
    return value
        
spelare_hand = []
dealer_hand = []

deal_kort(kortlek, spelare_hand)
deal_kort(kortlek, spelare_hand)
deal_kort(kortlek, dealer_hand)
deal_kort(kortlek, dealer_hand)


while True:
    print(f'din hand: {spelare_hand} ({calculate_hand_value(spelare_hand)})')
    print(f'dealers hand: [{dealer_hand [0]} ||||||]')

    if calculate_hand_value(spelare_hand) > 21:
        print ('du förlorade ')
        break

    action = input('Vill du hit eller stå över?')
        
    if action.lower() == 'hit' :
        deal_kort(kortlek, spelare_hand)
    
    else:
        break

print(f'spelarens hand: {spelare_hand} ({calculate_hand_value(spelare_hand)})')
print(f'dealerns hand : {dealer_hand} ({calculate_hand_value(dealer_hand)})')


if calculate_hand_value(spelare_hand) > 21:
    print('Du förlora!')
elif calculate_hand_value(dealer_hand) > 21:
    print('Dealern förlorar! Du vinner!')
elif calculate_hand_value(spelare_hand) > calculate_hand_value(dealer_hand):
    print('Du vinner!')
elif calculate_hand_value(spelare_hand) < calculate_hand_value(dealer_hand):
    print('Dealern vinner!')
else:
    print('Push!')

