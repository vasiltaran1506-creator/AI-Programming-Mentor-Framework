from pathlib import Path

def load_prices_text(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read() 

def _parse_prices(text: str) -> list[float]:
    if not text.strip():
        return []
    prices = []
    for part in text.split(","):    
        cleaned_part = part.strip()
        if not cleaned_part:
            raise ValueError("Price value can not be empty")
        price = float(cleaned_part)
        prices.append(price)
    return prices

def calculate_total_from_text(text: str) -> float:
    total = float(sum(_parse_prices(text)))
    return total

def main():
    path = Path(input("Enter path:\n"))
    text = load_prices_text(path)
    total = calculate_total_from_text(text)
    print(f"Total price: {total}")

if __name__ == "__main__":
    main()

