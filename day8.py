# Enter your code here. Read input from STDIN. Print output to STDOUT
book = dict()

num_entries = int(input())
for i in range(num_entries):
    entry = input()
    split_entries = entry.split()
    book[split_entries[0]] = split_entries[1]
    

while True:
    try:
        query = input()
    except:
        break    
    if query in book:
        print(query+"="+book[query])
    else:
        print("Not found")
