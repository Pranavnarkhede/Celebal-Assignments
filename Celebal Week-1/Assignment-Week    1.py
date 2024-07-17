# Name =>  Pranav Narkhede
# Assignment 1 => Week 1



def patterns(n):
    # Lower Triangular
    print("Lower Triangular:")
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    # Upper Triangular
    print("\nUpper Triangular:")
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    # Pyramid
    print("\nPyramid:")
    for i in range(n):
        for j in range(2*n-1):
            if j >= n-i-1 and j <= n+i-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


n = int(input("Enter the number of rows: "))
patterns(n)



# Output

# Enter the number of rows: 5
# Lower Triangular:
# *
# * *
# * * *
# * * * *
# * * * * *

# Upper Triangular:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# Pyramid:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

