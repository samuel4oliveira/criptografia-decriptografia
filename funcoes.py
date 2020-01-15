def xor(x, y):
    ans = ""
    for i in range(len(x)):
        if x[i] == "0" and y[i] == "1" or x[i] == "1" and y[i] == "0":
            ans += "1"
        else:
            ans += "0"
    return ans