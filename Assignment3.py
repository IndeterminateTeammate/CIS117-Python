#Assignment 3
#Author: Sean Fay
#Date: 14 Sept 2026

#Loop Added for ease of testing and for asignment #4 colab homework
while True:
    highway_number = int(input("Enter an interstate highway number (1-999): "))

    # Check for invalid highway number and prompt user to continue or exit
    if highway_number <= 0 or highway_number > 999:
        print("Invalid highway number. Continue? (yes/no):")
        continue_input = input().strip().lower()
        if continue_input == "no":
            break

    # Primary highways (1 - 99)
    elif 1 <= highway_number <= 99:
        if highway_number % 2 == 0:
            print(f"Interstate {highway_number} runs east/west.")
        else:
            print(f"Interstate {highway_number} runs north/south.")

    # Auxiliary highways (100 - 999)
    else:
        primary = highway_number % 100 
        if primary % 2 == 0:
            direction = "east/west"
        else:
            direction = "north/south"
            
        print(f"Interstate {highway_number} is an auxiliary highway serving I-{primary}, which runs {direction}.")

        