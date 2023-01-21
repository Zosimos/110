from mock_data import catalog


def say_hello():
    print("Hello there!")



# say_hello()


def print_the_sum(a,b):
    print(a+b)

# print_the_sum(21, 21)


def print_the_division(a,b):
    #if denominator is zero print an error "zero division error"
    #else divide and print the result
    if b == 0:
        print("Error: Divison by zero is not allowed")
    else:
        print (a/b)

def print_the_cheaper(a,b):
    if a > b:
        print (b)
    else:
        print (a)

def print_all_numbers():
    nums = [22, 15, 17, 23, 56, 85, 93, 99, 64]
    for n in nums:
        print (n)

def print_the_sum():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    #print the sum of all numbers
    total = 0
    for n in nums:
        total += n
    print(total)

def sum_over_forty():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    total = 0
    for n in nums:
        if n > 40:
            total += n
    print(total)

def count_lower_fifty():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    count = 0
    for n in nums:
        if n <= 50:
            count = count + 1
        print(count)


def print_catalog_total():
#sum all prices and print result
#create a variabl, create a for loop, get the price from product, add the price to total
    total = 0
    for prod in catalog:
        total = prod["price"] + total

#both below lines work, the benefit of the lower one is you can add text after {total}
        print("The total of the catalog is: " + str(total))
        #print(f"The total of the catalog is: {total}")
        


print_catalog_total()

# count_lower_fifty()

#um all the numbers greater than 40

# print_the_sum()
# sum_over_forty()
# print_the_cheaper(10, 5)
# print_the_division(12, 3)
# print_the_division(300, 0)
# print_all_numbers()