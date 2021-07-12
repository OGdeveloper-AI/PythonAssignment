Will_Smith = ("Willard", "Carroll", "Smith", 1968, "The Pursuit of Happyness", 1.88, "Actor", "Philadelphia, Pennsylvania, United States")

#Tuple assignment
(name, surname, surname2, b_year, movie, height, profession, b_place) = Will_Smith


print(Will_Smith)

print(len(Will_Smith))

print(type(Will_Smith))

print(Will_Smith[1])

print(Will_Smith[-1])

print(Will_Smith[0:2])

y = list(Will_Smith)

y.append("Aladdin")

Will_Smith = tuple(y)

print(Will_Smith)

y = list(Will_Smith)

y.remove("Aladdin")

Will_Smith = tuple(y)

print(Will_Smith)
print(name)
print(b_year)
print(profession)





