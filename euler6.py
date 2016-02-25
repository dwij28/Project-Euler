def sum_of_squares(n): return n*(n+1)*(2*n+1)/6
def squares_of_sum(n): return (n*(n+1)/2)**2
print squares_of_sum(100) - sum_of_squares(100)