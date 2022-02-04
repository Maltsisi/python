print ("Hello World!")
print ('Hello, ' + 'World!')
greeting = 'Hello'
print (greeting[0])

print ("Hello" [1])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (numbers [3:6])
print (numbers [10:0:-2])
print (numbers [0:10:1])
print (numbers [0:10:2])
print (numbers [::4])
print (numbers [5::-2])
print (numbers [:5:-2])
print (len(numbers)) #prints how many entries there are
print (max(numbers)) #prints highest number
print (min(numbers)) #prints lowest number
numbers.reverse()
print (numbers)

print ([1, 2, 3] + [4, 5, 6])

print ('python' * 5)
print ('python ' * 5)

print ([42] * 10)

sequence = [None] * 10
print (sequence)
print (list ('hello'))

x = [1, 1, 1]
x[1] = 2 #changed the 1 (second) spot to a 2
#x[2] = 3 #if i add this it will change it to [1,2,3]
print (x)
print (x.count(1)) #this counts how many times '1' is in the list. there are 2.

name = list('Perl')
print (name)
name[2:] = list('ar')
print (name)
name [1:] = list('ython')
print (name)

num = [1, 5]
num [1:1] = [2, 3, 4] #adding number into the sequence
print (num)
num [1:4] = [] #deleating numbers from sequence without 'del' function
print (num)

lst = [1, 2, 3]
print (lst)
lst.append(4) #append adds () to the end of the list
print (lst)

sentance = ("to be or not to be")
print (sentance.count('to'))

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print (a) #this is dif from a+b because in this one, 'a' changes to include 'b'
