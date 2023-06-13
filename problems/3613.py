import sys
input = sys.stdin.readline

def java2cpp(string):
    check = string[0]
    result = ''

    if check.isupper():
        return 'Error!'

    for s in string:
        if s.isupper():
            tmp = '_'+s.lower()
            result += tmp
        else:
            result += s.lower()

    return result

def cpp2java(string):
    result = ''

    if not string.islower() or '__' in string or string[0] == '_' or string[-1] == '_':
        return 'Error!'
    
    for idx, s in enumerate(string.split('_')): 
        if idx == 0:
            result += s
        else:
            result += s.capitalize()
    
    return result
       
if __name__ == '__main__':
    string = str(input().strip())
    
    if len(string) > 0:
        if '_' in string:
            print(cpp2java(string))
        else:
            print(java2cpp(string))
    else:
        print('Error!')