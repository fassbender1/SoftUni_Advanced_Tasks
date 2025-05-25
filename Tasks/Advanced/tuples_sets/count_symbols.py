text = input()
symbols = set()

for el in text:
    symbols.add(el)

for el in sorted(symbols):
    print(f"{el}: {text.count(el)} time/s")

#text = input()

#[print(f"{el}: {text.count(el)} time/s" for el in sorted(set(text))]
