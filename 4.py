import random

def generate_numbers_starting_with_4(count):
    possible_numbers = []
    
    possible_numbers.append(4)
    
    for i in range(40, 50):
        possible_numbers.append(i)
    
    for i in range(400, 500):
        possible_numbers.append(i)
    
    result = []
    for i in range(count):
        result.append(random.choice(possible_numbers))
    
    return result

numbers = generate_numbers_starting_with_4(44)

print("Generated 44 random numbers (0-1000) starting with 4:")
print("=" * 48)

for i, num in enumerate(numbers, 1):
    print(f"{i:2d}: {num}")

print(f"\nAll numbers: {numbers}")