# Write your code here
water = int(input('Write how many ml of water the coffee machine has:\n'))
milk = int(input('Write how many ml of milk the coffee machine has:\n'))
coffee = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
cups = int(input('Write how many cups of coffee you will need:\n'))

min_cups = int(min(water//200, milk//50, coffee // 15))
N = min_cups - cups

if min_cups == cups:
    print('Yes, I can make that amount of coffee')
elif min_cups > cups:
    print('Yes, I can make that amount of coffee (and even', N, 'more than that)')
else:
    print('No, I can make only', min_cups, 'cup(s) of coffee')
