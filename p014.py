"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(input_int):
    if input_int % 2 == 0:
        return input_int/2
    else:
        return 3*input_int + 1


winning_number = 0
max_chain_length = 0      
for x in range(999999):
    num = x
    current_chain = [num]
    while num > 2:
        num = collatz(num)
        current_chain.append(num)
    
    current_chain_length = len(current_chain)
    if current_chain_length > max_chain_length:
        winning_number = x
        max_chain_length = current_chain_length

print(winning_number)
        
    
