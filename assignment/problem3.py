def reverse(number):
    rvnumber = str(number)[::-1]

    return rvnumber

def isPalindrome(number):
    rvnumber = reverse(number)

    return str(number)[::-1] == rvnumber
