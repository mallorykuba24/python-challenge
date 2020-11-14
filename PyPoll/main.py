import csv

with open('Resources/election_data.csv.csv') as csv_file:
    read_csv = csv.DictReader(csv_file)

    total = 0
    candidates = []
    votes = {}

    for row in read_csv:
        total += 1
        name = row['Candidate']
        
        if name not in candidates:
            candidates.append(name)
            votes[name] = 0
        
        votes[name] += 1

    output = (
        'Election Results\n'
        '-------------------------\n'
        f'Total Votes: {total}\n'
        '-------------------------\n'
    )
    winner_votes = 0
    for name in candidates:
        output += f'{name}: {votes[name]/total*100:.3f}% ({votes[name]})\n'
        
        if votes[name] > winner_votes:
            winner_votes = votes[name]
            winner = name

    output += '-------------------------\n'
    output += f'Winner: {winner}\n-------------------------\n'
print(output)

with open('C:/Users/mallo/Documents/python-challenge/PyPoll/Analysis/output.txt', 'w') as output_txt:
    output_txt.write(output)