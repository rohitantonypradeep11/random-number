import random

# Function to generate a random number between a given range
def generate_random_number(start, end):
    return random.randint(start, end)

# Example usage:
start = 1
end = 100
random_number = generate_random_number(start, end)
print(f"Random number between {start} and {end}: {random_number}")
