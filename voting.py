print("options are BJP,SP,CNG,BSP,AAP")
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        print(f'Error: {candidate} is not a valid candidate')
def tally_votes(votes):
    total_votes = 0
    for candidate, count in votes.items():
        total_votes += count
        print(f'{candidate}: {count} votes')
    print(f'Total votes: {total_votes}')
candidates = input('Enter the candidates (separated by commas): ').split(',')
votes = {}
for candidate in candidates:
    votes[candidate.strip()] = 0
cast_vote(votes, 'BJP')
cast_vote(votes, 'CNG')
cast_vote(votes, 'SP')
cast_vote(votes, 'AAP')
cast_vote(votes, 'BSP')
tally_votes(votes)
