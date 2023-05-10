student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
max = student_scores[0]
for score in student_scores:
    if score > max:
        max = score
print(f"The highest score in the class is: {max}")