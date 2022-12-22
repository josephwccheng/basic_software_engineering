list_dicts = [{"key": 'test1', "order": 3}, {"key": 'test2', "order": 2}, {"key": 'test3', "order": 1}]

sorted_list = sorted(list_dicts, key=lambda element: element['order'], reverse=True)[:2]

for i in sorted_list:
    i['key'] = i['key'] + 'edited'
    print(i['key'])


print(sorted_list)