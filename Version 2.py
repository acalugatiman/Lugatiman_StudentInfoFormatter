first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

full_name = first_name + " " + last_name

proper_name = full_name.title()
name_code = full_name.upper()
section_name = section.upper()
proper_subject = favorite_subject.title()

character_count = len(proper_name)

print("\nFormatted Output:")
print("Name:", proper_name)
print("Name Code:", name_code)
print("Section:", section_name)
print("Favorite Subject:", favorite_subject)
print("Character Count:", character_count)