import csv
import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_n = [n for n in nums if n['date'] < q['date']]
    e_n = [q] * nums.count(q)
    b_n = [n for n in nums if n['date'] > q['date']]
    return quicksort(l_n) + e_n + quicksort(b_n)


with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    reader = quicksort(reader)

with open('scientist.txt', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['ScientistName', 'preparation', 'date', 'components'], delimiter='#')
    writer.writeheader()
    writer.writerows(reader)