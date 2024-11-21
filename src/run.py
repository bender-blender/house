from director import (
    CottageDirector,
    ApartamentDirector,
    ManorDirector)


cottage = CottageDirector()
res = cottage.build()
print(res)

print()

apartament = ApartamentDirector()
res = apartament.build()
print(res)

print()

manor = ManorDirector()
res = manor.build()
print(res)