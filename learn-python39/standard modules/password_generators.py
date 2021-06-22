"""

conditions for the password
1. length should be 8
2. at least 1 alph-lower case
3. at least 1 alph-upper
4. at least 1 digit
5. at least 1 special char from !@#$%^&*_

"""

import random
import string
char_lwr = string.ascii_lowercase
char_upr = string.ascii_uppercase
digit = string.digits
sp_char = '!@#$%^&**_[]'

st = char_lwr + char_upr + digit + sp_char
pas = ''.join(random.sample(st, 8))
print(pas)




