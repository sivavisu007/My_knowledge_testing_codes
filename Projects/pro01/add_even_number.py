def evenAdd(num_list):
    
    even = 0

    for num in num_list:
        if num % 2 == 0:
            even += num
    
    return even

if __name__ == "__main__":
    try:
        with open("even_list.txt", "r") as file:
            
            num_list = list(map(int, file.read().split()))

        even_num = evenAdd(num_list)

        print(f"The sum of even number is: {even_num} ")

    except:
        print("The file does not exist or is not in the correct format.")
