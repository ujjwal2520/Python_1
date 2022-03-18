*/

(1)	Write a Python program to combine values in python list of dictionaries. Go to the editor
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
  
   
(2)	WAP to get user id, user name, and user age from user and based on the entered id print the details foe particular user. Hint: use dictionary.

*/

Write a Python program to combine values in python list of dictionaries.
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)


***************************************************************************************************************************************************



def my_diect():
    id,name, age = 121, "Rahul", 21
    address = "Chandigarh India"
    print("Id: {}\nName: {}\nAge: {}\nAddress: {}".format(id,name, age, address))

my_diect()





