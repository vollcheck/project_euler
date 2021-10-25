def palindrome(n_digits: int):
    limit = 10 ** n_digits
    # naive implementation

    max_palindrome = 0

    for i in range(limit):
        for j in range(limit):
            if str(i * j) == str(i * j)[::-1]:
                max_palindrome = max(max_palindrome, i * j)

    return max_palindrome


palindrome(3)
