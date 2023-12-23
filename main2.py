ism = input("Ismingizni kiriting:  ").title()

dustlar = [ ]

print(f"Salom {ism}. Eng yaqin 3ta do'stingizni ismini kiriting:")

dust_1 = input("Birinchi dust:  ").title()
dust_2 = input("Ikkinchi dust:  ").title()
dust_3 = input("Uchinchi dust:  ").title()

dustlar.append(dust_1)
dustlar.append(dust_2)
dustlar.append(dust_3)

dustlar.sort()

print(f"Sizning dustlaringizni ruyxati:  {dustlar}")

yaqin_dust = int(input(f"""Eng yaqin dustingizni tanlang: 
{dustlar[0]} dustingizni tanlamoqchi bulsangiz 1ni kiriting,
{dustlar[1]} dustingizni tanlamoqchi bulsangiz 2ni kiriting,
{dustlar[2]} dustingizni tanlamoqchi bulsangiz 3ni kiriting
>>>   """))

best_friend = dustlar.pop(yaqin_dust-1)

print(f'Yaqin dustingiz: {best_friend}')

delete_friend = input("Qaysi do'stingizni ruyxatdan o'chirmoqchisiz:  ").title()

dustlar.remove(delete_friend)

yangi_dust = input("Yangi dustingizni ismini kiriting:  ").title()

dustlar.append(yangi_dust)

dustlar.sort()

print(f"{ism} sizning hozirgi dustlaringiz ruyxati: {dustlar}. Eng yaqin dustingiz: {best_friend}")

