import re

hand_groups = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
}

j_hand_groups = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
}

alpha_map = {
    'A': 'A',
    'K': 'B',
    'Q': 'C',
    'J': 'D',
    'T': 'E',
    '9': 'F',
    '8': 'G',
    '7': 'H',
    '6': 'I',
    '5': 'J',
    '4': 'K',
    '3': 'L',
    '2': 'M',
}

def convert_hand_to_alpha(hand, with_jokers=False):
    cards = re.findall(r'[A-Z\d]', hand)
    alpha_string = ''
    for card in cards:
        alpha_string += alpha_map[card]
    if with_jokers == True:
        alpha_string = alpha_string.replace('D', 'N')
    return alpha_string

def get_hand_type(hand, with_jokers=False):
    cards = re.findall(r'[A-Z\d]', hand)
    cardCount = {}
    for card in cards:
        if card in cardCount:
            cardCount[card] = cardCount[card] + 1
        else:
            cardCount[card] = 1

    if with_jokers == True and 'J' in cardCount:
        j_count = cardCount['J']
        if j_count == 5:
            return 0
        sorted_cards = sorted(cardCount.items(), key=lambda x:x[1], reverse=True)
        for s_card, s_count in sorted_cards:
            if s_card == 'J':
                continue
            cardCount[s_card] = s_count + j_count
            cardCount.pop('J')
            break

    counts = list(cardCount.values())
    if 5 in counts:
        """5-of-a-kind"""
        return 0
    if 4 in counts:
        """4-of-a-kind"""
        return 1
    if 3 in counts:
        if 2 in counts:
            """Full house"""
            return 2
        else:
            """3-of-a-kind"""
            return 3
    if 2 in counts:
        if counts.count(2) == 2:
            """2 pair"""
            return 4
        else:
            """1 Pair"""
            return 5
    """High Card"""
    return 6


handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()
for line in data:
    [hand, bid] = line.split(' ')
    hand_type = get_hand_type(hand)
    j_hand_type = get_hand_type(hand, True)
    alpha = convert_hand_to_alpha(hand)
    j_alpha = convert_hand_to_alpha(hand, True)
    hand_groups[hand_type].update({alpha: int(bid)})
    j_hand_groups[j_hand_type].update({j_alpha: int(bid)})

final_ranks = {}
for group in hand_groups.values():
    sorted_group = dict(sorted(group.items()))
    final_ranks.update(sorted_group)
winnings = 0
total = len(final_ranks)
for bid in final_ranks.values():
    winnings = winnings + (total * bid)
    total = total - 1

print('Part one:')
print(winnings)

j_final_ranks = {}
for j_group in j_hand_groups.values():
    j_sorted_group = dict(sorted(j_group.items()))
    j_final_ranks.update(j_sorted_group)
j_winnings = 0
j_total = len(j_final_ranks)
for j_bid in j_final_ranks.values():
    j_winnings = j_winnings + (j_total * j_bid)
    j_total = j_total - 1

print('Part two:')
print(j_winnings)