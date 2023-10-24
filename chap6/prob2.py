scores = {}

print('\tHigh Scores Keeper\n')
scores['NAME'] = 'SCORE'
while True:
    print('\t0 - Quit')
    print('\t1 - List Scores')
    print('\t2 - Add a Score\n')

    cho = int(input('Choice: '))

    if cho == 0:
        break
    if cho == 1:
        print(f'{"NAME":<7} {"SCORE":<7}')
        list1 = sorted(list(scores.items())[1:], key=lambda x: x[1], reverse=True)
        for name, score in list1:
            print(f'{name:<7} {score:<7}')

    if cho == 2:
        name = input()
        score = int(input())

        scores[name] = score
