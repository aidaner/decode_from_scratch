encoded = ''
count = ''
def start_decode_from_scratch(encoded1):
    global encoded
    global count
    encoded = encoded1
    count = 0

def decode_from_scratch():
    global encoded
    global count
    value = ""
    code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', ' ']
    while True:
        try:
            idx = encoded[count] + (encoded[count + 1])
        except:
            return value
            break
        count = count + 2
        if int(idx) < 1:
            return value
            break
        idx = int(idx)
        value = value + str(code[idx])
        
        

        


def encode_from_scratch(to_encode):
    code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', ' ']
    count = 0
    global encoded
    for x in to_encode:
        encoded = encoded + str(code.index(to_encode[count]))
        count = count + 1
    encoded = encoded + "00"
    return encoded

def clear_from_scratch():
    global encoded
    encoded = ''
