a="bhavya"
print(len(a))
# # #

string="3.414"
print(string)
print(type(string))
float =float(string)
print(float)
print(type(float))
# # #

test_list = [{'a': '1', 'b': '2'}, {'c': '3', 'd': '4'}]
print("The original list is : " + str(test_list))
for dicts in test_list:
     for keys in dicts:
         dicts[keys] = int(dicts[keys])
print("The modified converted list is : " + str(test_list))