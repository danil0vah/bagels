import random

#основной цикл
def game(nums_val, sec_number):
    i = 0
    result = 0
    while(i <= int(nums_val *3)): # пока пользователь не введет правильное число
        usr = ''
        while len(usr) < nums_val or len(usr) > nums_val:
            usr = input("Введите число:\t")
            if len(usr) < nums_val:
                print('Вы ввели число меньшей разрядности!\n')
                continue
            elif len(usr) > nums_val:
                print('Вы ввели число большей разрядности!\n')
            else:
                break

        outp = ''
        for j in usr: # проверяем цифры на наличие
            if (j in sec_number and sec_number.index(j) == usr.index(j)):
                outp +="Fermi "
            elif j in sec_number:
                outp += "Pico "

        if not outp: print("Bagel") #если совпадающих цифр нет

        if outp == "Fermi "*nums_val: # если количество Fermi совпадает с разрядностью
            outp = "U got it!"
            result = 1
            break
           
        print(outp+"\n")

        i+=1

    return result
        


if __name__ == '__main__':

    print('''    ...Привет! Это игра - Bagels...
    Правила простые. Ты выбираешь, какой разрядности будет число.
    Затем я загадываю число выбранной тобою разрядности. А ты пытаешься его угадать.
    Ты вводишь число а я пишу тебе: 
    
    Pico - если ты угадал одну из цифр, но она не на правильном месте.
    (Pico Pico будет означать что ты угадал две цифры, но они не там где надо.)
    
    Fermi - если ты угадал число и оно на правильном месте.

    Bagels - если ты не угадал ничего.

    Число твоих попыток ограничено!
    Чем большей разрядности число, тем больше тебе дается попыток. 

     ...Нажми Enter чтобы начать...
    ''')
    input()

    while True: #основной цикл игры

        nums_val = int(input("Введите, какой разрядности будет число от 2 до 10:\t"))
        secret_num = str(random.randint(int("1"+"0"*(nums_val-1)), int("9"+"9"*(nums_val-1))))
        result = game(nums_val, secret_num)

        if result == 1:
            print("\nТы выиграл! Хочешь сыграть ещё раз?[Да/Нет]\t")
        else:
            print("\nТы проиграл... Хочешь сыграть ещё раз?[Да/Нет]\t")
        
        while True: # пока пользователь не введет правильный ответ

            cont = input()
            if "да" in cont.lower():
                break
            elif "нет" in cont.lower():
                break
            else:
                print('Я тебя не понял. Напиши ещё раз.\n')
                continue

        if "да" in cont.lower():
                continue
        elif "нет" in cont.lower():
            print('Прощай!')
            break
