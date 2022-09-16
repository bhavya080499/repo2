a = (10,5,4,20,1,15,12)
x = sorted(a)
print(x)
######

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)
##########
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
print(py_solution().reverse_words('sree .py'))
#############
list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")
        