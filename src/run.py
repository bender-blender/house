from builders import (
    BuilderApartment,
    BuilderCottage)

from director import (
    DirectorApartament,
    DirectorCottage
)



apartment = BuilderApartment()
build = DirectorApartament(apartment)
print(build.construct_apartament())
print()

cottage = BuilderCottage()
build = DirectorCottage(cottage)
print(build.construct_cottage())
