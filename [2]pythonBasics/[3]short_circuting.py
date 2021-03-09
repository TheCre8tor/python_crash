# SHORT CIRCUTING

# OR SHORT CIRCUTING
is_citizen = False
is_licensed = False

print(is_citizen or is_licensed or 'You are not a citizen of this country')

# AND SHORT-CIRCUTING
is_citizen = True
is_licensed = True

print(is_citizen and is_licensed and 'You are welcome back home. Hurray!!!')