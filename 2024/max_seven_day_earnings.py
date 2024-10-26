def max_seven_day_earnings(earnings):
    # Length of the earnings list
    n = len(earnings)

    # If there are fewer than 7 days, we can't have a full week of earnings
    if n < 7:
        return []

    # Initialize the maximum sum to a very small number
    max_start_index = 0

    # Calculate the sum of the first seven days
    current_sum = sum(earnings[:7])

    # Initialize max_sum with the sum of the first seven days
    max_sum = current_sum

    print(f"log1 -> {current_sum}")
    # Iterate over the list from the 8th element to the end
    for i in range(7, n):
        # Slide the window to the right by subtracting the element that is left behind and adding the new element
        print(f"log2 -> {current_sum}")
        print(f"log2.1 -> {earnings[i - 7]}")
        print(f"log2.2 -> {earnings[i]}")

        current_sum = current_sum - earnings[i - 7] + earnings[i]
        print(f"log3 -> {current_sum}")
        # Update max_sum and max_start_index if a new maximum is found
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = i - 6
            print(f"max_start_index -> {max_start_index}")

    # Return the sublist of seven consecutive days with the highest total earnings
    return earnings[max_start_index:max_start_index + 7]


# Example usage:
earnings = [100, 200, 300, 400, 500, 600, 700, 150, 250, 350, 450, 550, 650, 750]
print(max_seven_day_earnings(earnings))
