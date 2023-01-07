# This is match (Switch) implementation available after python 3.10
# Program that greets you based on input
inputstr = input('enter input  :  ')
match inputstr:
    case 'hello there':
        print('general kenobi')
    case 'sith':
        print('dark something something dark')
    case 'anakin':
        print('because of obi wan')
    case other:
        print('soory bot')
    
