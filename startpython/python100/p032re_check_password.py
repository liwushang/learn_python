import re

"""
verify  password
1.Length of password at interval of [6,20]
2.Must contain an uppercase letter
3.Must contain a lowercase letter
3.Mush contain a number
4.Must contain a special character
"""

def check_password(password_in):
    if not 6 <= len (password_in) <= 20:
        return False,"the length of password must at interval of [6, 20]"
    if not re.findall(r"[A-Z]", password_in):
        return False, "Must contain an uppercase letter"
    if not re.findall(r"[a-z]", password_in):
        return False, "Must contain an lowercase letter"
    if not re.findall(r"[0-9]", password_in):
        return False, "Must contain number"
    if not re.findall(r"[^0-9a-zA-Z]", password_in):
        return False, "Must contain a special character"
    else:
        return True, None

result = check_password("abc123?A")
print(result)
