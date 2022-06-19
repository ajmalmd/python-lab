
course = {"Python", "PHP", "Java"}
print(course)
a = input('Enter item name to remove: ')
if a in course:
    course.discard(a)
print(course)