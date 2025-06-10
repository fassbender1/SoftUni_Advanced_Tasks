def concatenate(*args, **kwargs):
    sentence = ''.join(args)

    for key, value in kwargs.items():
        sentence = sentence.replace(key, value)
    return sentence