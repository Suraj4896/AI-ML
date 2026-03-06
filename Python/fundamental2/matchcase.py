color = input('enter color: ')

match color:
    case 'Green':
        print('go')
    case 'yellow':
        print('look')
    case 'red':
        print('stop')
    case _:
        print('wrong color')