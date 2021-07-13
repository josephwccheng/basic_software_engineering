''' 
Input: List of lists
Within each list, sort the list by value, but keeping the index as the output
'''

tickets = [
    [0.23486008, 0.1902059,  0.19009577, 0.19272467, 0.19211353],
    [0.20444456, 0.1977669,  0.19765238, 0.20038578, 0.19975035]
]

print("input ticket is: ", tickets)

for ticket in tickets:
    sorted_list = sorted(enumerate(ticket), key=lambda x: x[1], reverse=True)
    for i in sorted_list:
        print(i[0])
        print(i[1])
