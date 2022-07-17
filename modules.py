from decorators import fun,period

@fun
@period
def invite(name1,name2,string_change):
    print("Welcome", name1,"and",name2,"at",string_change)

invite("Ragul","Dravid")

@period
def inauguration(name1,name2,string_change):
    print("Hi friends welcome {} and {} come to party at".format(name1,name2),string_change)

inauguration("john","smith")
