with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    req = input()
    reader.sort(key=lambda x: x['date'])
    while req != 'эксперимент':
        req = req.split('.')
        req = req[::-1]
        req = '-'.join(req)
        l = 0
        r = len(reader) - 1
        while l <= r:
            center = (l + r) // 2
            if req == reader[center]['date']:
                scientist = reader[center]
                scientist_name = scientist['ScientistName'].split()
                print(f'Ученый {scientist_name[0]} {scientist_name[1][0]}.{scientist_name[2][0]}.'
                      f' создал препарат: {scientist["preparation"]} - {scientist["date"]}')
                break
            if req > reader[center]['date']:
                l = center + 1
            else:
                right = center - 1
        req = input()