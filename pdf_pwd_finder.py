import itertools, io, pdfplumber

done = False
with open('a.pdf', 'rb') as f:
    content = io.BytesIO(f.read())

count = 0
length = 8

def pw_guess(l):
    res = itertools.combinations_with_replacement('0123', l)
    # res = itertools.count(0)
    print('length:', l)
    for guess in res:
        yield guess


while True:
    # Make generator object
    guess_generator = pw_guess(length)
    for guess in guess_generator:
        if (count % 10000 == 0):
            print(count, length)
        count += 1
        try:
            # pdf = pdfplumber.open(r'a.pdf')#, password = guess)
            pdf = pdfplumber.open(content, password=guess)
            print("Password acquired: " + str(guess))
            done = True
            break
        except Exception as e:
            pass
            # print('e')
            # print(guess)
    if done:
        break
    length += 1
    count = 0
