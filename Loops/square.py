def calculate_squares(start, end):
    for i in range(start, end):
        square = i * i 
        print(f"{i} squared = {square}")
    # ?


# Don't edit below this line


def test(start, end):
    print(f"Calculating squares from {start} until {end}:")
    calculate_squares(start, end)
    print("=====================================")


def main():
    test(100, 105)
    test(1, 3)
    test(11, 14)


main()
