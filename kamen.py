import random

options = ["камень", "ножницы", "бумага", "ящірка", "спок"]

print("Игра: Камень, ножницы, бумага, ящірка, спок")
print("Чтобы выйти, напиши: выход")

while True:
    player = input("\nВыбери: камень, ножницы бумага ящірка или спок : ").lower()

    if player == "выход":
        print("Спасибо за игру!")
        break

    if player not in options:
        print("читать умеешь? так правильно пиши.")
        continue

    computer = random.choice(options)
    print("Компьютер выбрал:", computer)

    if player == computer:
        print("Ничья!")
    # elif (
    #     (player == "камень" and computer == "ящірка") or
    #     (player == "ящірка" and computer == "бумага") or
    #     (player == "бумага" and computer == "спок") or
    #     (player == "спок" and computer == "ножницы") or
    #     (player == "ножницы" and computer == "ящірка") or
    #     (player == "ящірка" and computer == "спок") or
    #     (player == "спок" and computer == "камень") or
    #     (player == "камень" and computer == "ножницы") or
    #     (player == "ножницы" and computer == "бумага") or
    #     (player == "бумага" and computer == "камень")
    # ):
        wins = {
            "камень": ["ножницы", "ящірка"],
            "ножницы": ["бумага", "ящірка"],
            "бумага": ["камень", "спок"],
            "ящірка": ["бумага", "спок"],
            "спок": ["ножницы", "камень"]
        }
        print("Ты выиграл!")
    else:
        print("Компьютер выиграл!")