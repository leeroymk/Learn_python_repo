def format_price(price) -> str:
    num: int = int(price)
    return f'Цена: {num} руб.'


res: str = format_price(56.24)
print(res)
