stats = {
    "p": 5412,
    ";": 73,
    "u": 1428
}

def do_something(dictionary):
    lsorted_list = []

    print(f"Printing the entire dict:\n{dictionary}\n=====================================\n")

    for i in dictionary:
        print(i)

    for i in dictionary:
        print(dictionary[i])


do_something(stats)