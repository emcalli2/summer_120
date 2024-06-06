def max_key_by_val(data):
    max = None
    max_key = ""
    for key,value in data.items():
        if max == None or value > max:
            max = value
            max_key = key
    return max_key