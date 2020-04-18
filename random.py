print('\033[33m')

# Functions
def generateRandom(arr, i, m, a, c, s):
    return (a*arr[i-1]+c)%m

# Random numbers array
nums = []

# MOD number
m = 8255355451

# Multiplier
a = 1377312

# Addition
c = 52267

# Custom seed
s = int(input('Valor de la semilla: '))

# Append the seed
nums.append(s)

for i in range(1,101):
    res = generateRandom(nums, i, m, a, c, s)
    nums.append(res)
    print(str(i)+ ' -> \033[32m' + str(res) + '\033[33m')

print('\033[0m')
