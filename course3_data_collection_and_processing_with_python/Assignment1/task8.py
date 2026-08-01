#Given below is a list of lists of athletes. Create a list, t_athletes, that includes an athlete's name if it contains a lowercase "t". If it does not contain the letter "t", save that athlete's name into list others.

athletes = [
    ['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'],
    ['Felix', 'Bolt', 'Gardner', 'Eaton'],
    ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t_athletes = []
others = []

for Il_ath in athletes:
    for athlete in Il_ath:
        if 't' in athlete:
            t_athletes.append(athlete)
        else:
            others.append(athlete)

print('t_athletes: \n', t_athletes)
print('others: \n',others)