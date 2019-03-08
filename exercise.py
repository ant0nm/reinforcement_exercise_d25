our_ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

def find_winner(ballots):
    candidates = {}
    for ballot in ballots:
        for place, person in ballot.items():
            score = 0
            if place == 'gold':
                score = 3
            elif place == 'silver':
                score = 2
            elif place == 'bronze':
                score = 1

            if person in candidates:
                candidates[person] += score
            else:
                candidates[person] = score
    max_score = 0
    winner = None
    print(candidates)
    for candidate, score in candidates.items():
        if score > max_score:
            max_score = score
            winner = candidate
    return winner

w = find_winner(our_ballots)
print(w)
