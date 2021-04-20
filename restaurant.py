class Table:
    def __init__(self, number, name, status):
        self.TableNumber = number
        self.Name = name
        self.status = status

def findWaiterWiseTotalNoOfTables(tables):
    dic = {}
    for i in tables:
        if i.Name not in dic:
            dic[i.Name] = 1
        else:
            dic[i.Name]+=1
    return dic

def findWaiterNameByTableNo(tables, number):
    for i in tables:
        if i.TableNumber == number:
            return i.Name
    return None
     
print("\nWelcome..!\n")
n = int(input("Enter Number of tables: "))
print(" ")
tables = []

for i in range(n):
    num = int(input("Enter Table {} number: ".format(i+1)))
    name = input("Enter Table {} Waiter name: ".format(i+1))
    status = input("Enter Table {} status: ".format(i+1))
    print(" ")
    tables.append(Table(num, name, status))

d = findWaiterWiseTotalNoOfTables(tables)
print("Waiter Name with Count: ")
for key in sorted(d.keys()):
    print(key + " - " + str(d[key]))
print(" ")

numb = int(input("Enter Table number to find its Waiter Name: "))

strr = findWaiterNameByTableNo(tables, numb)
if strr != None:
    print("Table number {} belongs to {}".format(numb,strr))
else:
    print("No Table Found")
print(" ")
    

