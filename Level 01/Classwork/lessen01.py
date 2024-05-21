name = "Nika"
# name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "Nika" არის ცვლადისთვის მნიშვნელობა
surname = "Patishvili"

print(name)
# პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

# name = "Nika" ეს არის str(string) თიპის ცვლადი
# სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები

age = 12 # ეს არის int(integer) მთელი რიცხვი
height = 1.60 # ეს არის float ტიპის ცვლადი (ათწილადი)

knows_programming = True # True or False Boolean ტიპის ცვლადი

print(name + " " + surname)

# print(type(age)) # age გადაეცა type ფუნქციას, რომელმაც დააბრუნა მისი ტიპი
# და დაბრუნებული ნებისმიერი სიტყა დავპრინტეთ, რომელმაც გაგვაგებინა, რომ
# print(type(age))  - ის ტიპი არის int(integer) მთელი რიცხვი

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))

print(surname + " " + name)