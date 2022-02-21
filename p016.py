"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""



big_number = 2 ** 1000

big_number_str = str(big_number)

delimited_str = ",".join(big_number_str)

numbers_list = [int(n) for n in delimited_str.split(',')]

print(sum(numbers_list))
