input_str = "aaawwqqqqaa"
#o/p:a3w2q4a2

inp = str(input_str[0:3])
inp1 = str(input_str[3:5])
inp2 = str(input_str[5:9])
inp3 = str(input_str[9:11])

inp11 = str(input_str[0])
inp22 = str(input_str[3])
inp33 = str(input_str[5])
inp44 = str(input_str[9])

inp_string = str(len(inp)) 
inp_string1 = str(len(inp1))
inp_string2 = str(len(inp2))
inp_string3 = str(len(inp3))


str_conv = inp11 + inp_string + inp22 + inp_string1 + inp33 + inp_string2 + inp44 + inp_string3


print(str_conv)

