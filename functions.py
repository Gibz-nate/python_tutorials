

def to_celsius(f):
    
    celsius = 5/9 * (f-32)
    return celsius
    # ?
## Don't touch below this line

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")
test(100)
test(88)
test(104)
test(112)

def hours_to_seconds(hours):
    conversion = hours * 3600
    return conversion
    # ?


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)