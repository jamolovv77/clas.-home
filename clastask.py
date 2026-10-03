# class Tamagotchi:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 50
#         self.happiness = 50
#         self.is_alive = True

#     def _check_alive(self):
#         if self.hunger >= 100 or self.happiness <= 0:
#             self.is_alive = False
#         if not self.is_alive:
#             print(f"{self.name} больше не с нами... 😢")
#         return self.is_alive

#     def feed(self):
#         if not self._check_alive():
#             return
#         self.hunger = max(0, self.hunger - 20)
#         self.happiness = max(0, self.happiness - 5)
#         print(f"{self.name} поел 🍖")


#     def play(self):
#         if not self._check_alive():
#             return
#         self.happiness = min(100, self.happiness + 20)
#         self.hunger = min(100, self.hunger + 15)
#         print(f"{self.name} поиграл 🎾")
#         self._check_alive()

#     def tick(self):
#         if not self._check_alive():
#             return
#         self.hunger = min(100, self.hunger + 10)
#         self.happiness = max(0, self.happiness - 10)
#         self._check_alive()

#     def status(self):
#         if not self._check_alive():
#             return
#         print(f"{self.name}: голод {self.hunger}, счастье {self.happiness}")



# # --- Играем! ---
# pet = Tamagotchi(input("Name of your pet: "))




# while True:
#     n=int(input("1)Status\n2)Play\n3)Feed\n4)Tick\n0)Kill pet\nChoose one: "))
#     match n:
#         case 1:
#             pet.status()
#         case 2:
#             pet.play()
#         case 3:
#             pet.feed()
#         case 4:
#             pet.tick()
#         case 0:
#             print("You kill own pet!")
#             break
#         case _:
#             print("Invalid input!!!")

# import random























# class Hero:
#     def __init__(self, name):
#         self.name =name
#         self.health =100
#         self.power =10

#     def attack(self,other):
#         other.health -=self.power

#     def is_alive(self):
#         return self.health > 0
# class Warrior(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 15
# class Mage(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 20

#     def attack(self, other):            # свой метод вместо родительского
#         if random.random() < 0.5:
#             print(f"{self.name} промахнулся! ✨")
#         else:
#             super().attack(other)     # попал — бьём как обычный герой
# class Healer(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 5

#     def heal(self):
#         self.health = min(100, self.health + 15)
#         print(f"{self.name} лечится 💚 (+15 HP)")
        
        
# def battle(hero1, hero2):
#     round_num = 1
#     while hero1.is_alive() and hero2.is_alive():
#         print(f"--- Раунд {round_num} ---")
#         hero1.attack(hero2)
#         if hero2.is_alive():          # зачем эта проверка — см. ниже
#             hero2.attack(hero1)
#         round_num += 1

#     if hero1.is_alive():
#         print(f"🏆 Победил {hero1.name}!")
#     else:
#         print(f"🏆 Победил {hero2.name}!")


# # battle(Warrior("Конан"), Mage("Гэндальф"))
# # battle(Mage("Гэндальф"), Healer("Айболит"))# работает без изменений battle!



# while True:
#     num = int(input("1)Battle\n2)Battle + Heler\n0)End game\nChoose one : "))
#     match n:
#         case 1:
#             battle(Warrior("Umarjon"), Mage("Abdulloh"))
#         case 2:
#             battle(Warrior("abdulloh"),Healer("Ehson"))
#         case 0:
#             print("The game end !")
#             break
#         case _:
#             print("invalid input !")
























class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} — {self.price} руб."

class Cart:
    def __init__(self):
        self.items = []    # новая корзина всегда пустая
    def add(self, product, quantity=1):
        for _ in range(quantity):
            self.items.append(product)
    def total(self):
        return sum(item.price for item in self.items)
    def total(self):
        result = 0
        for item in self.items:      # берём каждый товар из списка
            result += item.price     # и прибавляем его цену
        return result
    def remove(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return                # нашли и удалили — сразу выходим!
        print(f"Товара «{name}» нет в корзине")
    def checkout(self):
        print("===== ЧЕК =====")
        for item in self.items:
            print(item)               # сработает наш __str__!
        print("---------------")
        print(f"ИТОГО: {self.total()} руб.")


num = Cart()

while True:
    print("\n   MAGAZINE      ")
    num1 = input(f"1) Add products\n2) Delite product\n3) Show check\n0) Logout\nChoose one : ")


    match num1:
        case "1":
            name =input("The name of the product: ")
            if not name:
                print("The name must not be empty")
                continue



            try:
                num2=int(input("Price(Somoni): "))
                num3=input("PCS (SHTUK): ")
                num4=int(num3) if num3 else 1
                if num2 < 0 or num4 < 1:
                    print("The must not be negative  and the pcs will be upper from 0")
                    continue
            except ValueError:
                print("The price and the pcs will be only digit")
                continue

            num.add(Product(name, num2), num4)
            print(f"I will add in basket: {name} — {num4} шт.")

        case "2":
            name=input("The name of product for delete: ").strip()
            num.remove(name)

        case "3":
            num.checkout()
        case "0":
            print("Good bye!")
            break

        case _:
            print("Invalid input")
















# class Book:
#     def __init__(self, title, author):
#         self.title=title
#         self.author=author
#         self.is_available=True   # новая книга свободна

# class Reader:
#     def __init__(self, name):
#         self.name=name
#         self.books=[]      # на руках пока ничего
        
# class Library:
#     def __init__(self):
#         self.catalog=[]

#     def add_book(self, book):
#         self.catalog.append(book)

#     def _find(self, title):
#         for book in self.catalog:
#             if book.title==title:
#                 return book
#         return None

#     def lend(self, book_title, reader):
#         book = self._find(book_title)

#         if book is None:
#             print("Такой книги нет")
#         elif not book.is_available:
#             print("Книга занята")
#         elif len(reader.books)>=3:
#             print("Верните сначала что-нибудь")
#         else:
#             book.is_available=False
#             reader.books.append(book)
#             print(f"{reader.name} взял «{book.title}»")
    
#     def take_back(self, book_title, reader):
#         for book in reader.books:
#             if book.title==book_title:
#                 book.is_available = True
#                 reader.books.remove(book)
#                 print(f"{reader.name} вернул «{book.title}»")
#                 return
#         print(f"У {reader.name} нет этой книги")

#     def show_available(self):
#         print("Свободные книги:")
#         for book in self.catalog:
#             if book.is_available:
#                 print(f"{book.title}—{book.author}")


# lib = Library()
# lib.add_book(Book("Мастер и Маргарита", "Булгаков"))
# lib.add_book(Book("1984", "Оруэлл"))
# lib.add_book(Book("Гарри Поттер", "Роулинг"))
# lib.add_book(Book("Три товарища", "Ремарк"))


# while True:
# 	print("\n     Library ")
# 	n=input("1) Add book\n2) Get book\n3) Giveback the book\n4) Shov the books\n5) My books\n0) Logout\nChouse one: ")
# 	match n:
# 		case "1":
# 			title = input("The name of the book: ").strip()
# 			author = input("Author: ").strip()
# 			if not title or not author:
# 				print("The name or the Author must not be empty.")
# 			else:
# 				library.add_book(Book(title, author))

# 		case "2":
# 			title = input("The name of the book for getting ").strip()
# 			library.lend(title, reader)

# 		case "3":
# 			title = input("The name of the book for givingback ").strip()
# 			library.take_back(title, reader)

# 		case "4":
# 			library.show_available()

# 		case "5":
# 			print(f"Book for readder {reader.name}:")
# 			if not reader.books:
# 				print("I dont have any books.")
# 			for book in reader.books:
# 				print(f"  {book.title} — {book.author}")

# 		case "0":
# 			print("Good buy!")
# 			break

# 		case _:
# 			print("Invalid input.")


