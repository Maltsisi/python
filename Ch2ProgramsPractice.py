

fourth = input('Year: ')[3]
print (fourth)


months = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec'
   ]
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] +  7 * ['th'] \
        + ['st']
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')
month_number = int(month)
day_number = int(day)
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print (month_name + ' ' + ordinal + ', ' + year)
 
  

tag = '<a href="http://www.python.org">Python web site</a>'
print (tag[9:30]) #Prints 'www.python.org'
print (tag[32:-4])#Prints 'python web site'
#print (tag) #prints the whole 'tag'

sentence = input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print ()
print (' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print (' ' * left_margin + '|  ' + ' ' * text_width + '  |')
print (' ' * left_margin + '|  ' + sentence + '  |')
print (' ' * left_margin + '|  ' + ' ' * text_width + '  |')
print (' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print ()

permissions = 'rw'
print ('w' in permissions)
print ('r' in permissions)
print ('k' in permissions)

#users = ['matt', 'ally', 'aum'] #cant figure this one out :( 
#input ("Enter name:") in users #dont know how to get it to print true or false

database = [
  ['albert', '1234'],
  ['dilbert', '4242'],
  ['smith', '7524'],
  ['jones', '9843']
]
username = input('User name: ') #needs check for wrong names
pin = input('PIN code: ')

if [username, pin] in database: print ('Access granted')
else: print ('Access denied') #Added this myself. there are other checks to do

