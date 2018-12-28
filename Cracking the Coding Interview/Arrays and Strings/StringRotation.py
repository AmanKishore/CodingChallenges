'''
String Rotation:
    Check if s2 is a rotation of s1
'''

def is_substring(string, sub):
    return string.find(sub) != -1 # Finds the first index where sub starts


def string_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) != 0:
        return is_substring(s1 + s1, s2)
    return False