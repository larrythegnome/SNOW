student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

scores = student_scores.copy()
for key, value in scores.items():
    if value >= 91:
        scores[key] = 'Outsatanding!'
    if value <= 90 and value >= 81:
        scores[key] = 'Exceeds Expectations'
    if value <= 80 and value >= 71:
        scores[key] = 'Accptable'
    if value <=70:
        scores[key] = 'Fail'
print(scores)

student_grades = {}

print(student_grades)