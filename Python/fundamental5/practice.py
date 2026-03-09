#word search
data = True
count = 0
Word = input('enter word: ')
with open('sample.txt') as f:
    while data:
        data = f.readline()
        count += 1
        if f'{Word}' in data:
            print(f'{Word} found at row number: {count}')
            break