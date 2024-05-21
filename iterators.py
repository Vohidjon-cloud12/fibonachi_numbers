#Foydalanuvchi kiritgan natural songacha bolgan fibonachi sonlarini chiqaruvchi funksiya:
class Fibonachi:
    """Fibonachi sonlarini generatsiya qiluvchi iteratorni yaratadi"""

    def __init__(self, max_value):
        self.max_value = max_value

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

def fibonachi_up_to(n):
    """Foydalanuvchi kiritgan songacha bolfgan fibonachi sonlarini royhatga yigadi"""
    fib_iterator = Fibonachi(n)
    result = []
    for fib in fib_iterator:
        result.append(fib)
    return result

def main():
    """Menyu funksiyasi - foydalanuvchi bilan muloqot qiladi"""
    while True:
        user_input = input("Maksimal qiymatni kiriting (yoki 'stop' deb yozing): ").strip().lower()
        if user_input == 'stop':
            print("Dasturdan chiqildi.")
            break
        elif user_input.isdigit():
            max_value = int(user_input)
            fib_numbers = fibonachi_up_to(max_value)
            print(f"Fibonachi sonlari {max_value} gacha: {fib_numbers}")
        else:
            print("Iltimos, butun son yoki 'stop' deb kiriting.")

if __name__ == "__main__":
    main()
