"""This application takes a number, breaks it down and squares each."""

def square(number):
    """Square a number."""
    num_list = [number]
    print(num_list)
    for i in int(len(num_list)):
        print(i)
        print(num_list)
    num = number**2
    return num


number = square(22)
print(number)
