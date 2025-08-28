def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s2)


print(is_rotation("ABCD", "CDAB"))
# Find the longest substring without repeating characters
