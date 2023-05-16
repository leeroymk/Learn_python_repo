def get_summ(one, two, delimiter='&') -> str:
    return str(one) + delimiter + str(two)


res: str = get_summ('Learn', 'python')

print(res)
print(res.upper())
