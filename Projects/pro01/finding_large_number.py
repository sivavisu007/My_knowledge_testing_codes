def checker(num_list):
    if not num_list:
        return None
    
    largest = num_list[0]

    for num in num_list:
        if num > largest:
            largest = num
    
    return largest

if __name__ == "__main__":
    # num_list = list(map(int, input("Enter number you need to find: ").split()))

    # print(num_list)

    # largest_number = checker(num_list)

    # if largest_number is not None:
    #     print(f"the largest number is in this list: {largest_number}")

    # else:
    #     print("List is empty")

    try:
        with open("number.txt", "r") as file:

            num_list = list(map(int, file.read().split()))

        largest_number = checker(num_list) 

        if largest_number is not None:
            print(f"The largest numnber is: {largest_number}")
        else:
            print("File is empty")

    except FileNotFoundError:
        print("the file is not found")