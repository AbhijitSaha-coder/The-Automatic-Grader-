key =  ['A', 'B', 'A', 'C', 'D']  
students = [["John", ['A', 'B', 'B', 'C', 'D']],
["Jane", ['A', 'A', 'A', 'A', 'A']],
["Bob",  ['B', 'B', 'A', 'D', 'D']]]

for student in students:
    name = student[0]
    answers = student[1]
    score = 0
    for i in range(len(key)):
        if answers[i] == key[i]:
            score += 1
    print(f"{name} scored {score/len(key)*100}")  