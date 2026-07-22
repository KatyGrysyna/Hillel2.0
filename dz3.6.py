def check_even_odd(number):
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")

def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list