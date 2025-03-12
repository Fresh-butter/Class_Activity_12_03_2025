def is_narcissistic(n): # changed name of the function from is_narc to is_narcissistic and added a colon 
    """Check if a number is narc."""
    num_str = str(n) # changed from == to =
    num_digits = len(num_str) # changed from == to =
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) #changed from *** to **
    
    return sum_of_powers == n

def print_narcissistic_numbers(start, end): # changed function definition from print_narcis_numbers(start end) to print_narcissistic_numbers(start, end): 
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #added a colon
        if is_narcissistic(num): #added a colon
            print(num)

print_narcissistic_numbers(1000, 5000) # changed function call from print_narc_numbers(1000, 5000) to print_narcissistic_numbers(1000, 5000)
"""Submit your response here: https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u """
