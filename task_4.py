values = ['0', '1', '""', '"hello"', '[]','[1, 2, 3]', 'None', 'True', 'False', "False"]

print("Truthy and Falsely Values")
print("-" * 30)
for value in values:
    if value:
        print(f"{repr(value):13} → Truthy")
    else:
        (f"{repr(value):13} → Falsely")
        
print(f"The value of values are: {values}")