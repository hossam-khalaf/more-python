# print(range(3))

## increment    + +1 +2 +6
## decrement    - -1 -4 

# for num in range(6):
#   print(num)
ages = [13,16,43,70,26, 6]
names = ['Heba','Karma', 'Lili', 'Hayfa', 'Raya', 'Sherry']

print(names[1])
print()

for name in range(len(names)):
  print(f'{name} - Name: {names[name]} | Age: {ages[name]}')