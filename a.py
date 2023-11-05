import base64

def reverse_string(string):
    reversed_string = string.swapcase()[::-1]
    print(reversed_string)
    decoded_string = base64.b64decode(reversed_string)
    return decoded_string

input_string = "Hello World!"
result = reverse_string(input_string)
print(result)
