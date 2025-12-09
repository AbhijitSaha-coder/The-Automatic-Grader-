Project :The Automatic Grader (Nested Lists)

This project implements a simple automatic grading system for multiple-choice tests using Python. A master answer key is provided, along with a nested list containing each student’s name and their submitted answers. The program loops through every student, compares their answers with the correct key, calculates their score, and prints a report-card style result (e.g., “John: 4/5 (80%)”).

This project is created by Abhijit Saha as part of my PSP (Problem Solving and Programming) practice.

⸻

📌 How It Works
	•	The master answer key is stored as a list:
  ['A', 'B', 'A', 'C', 'D']
  •	Students are stored in a nested list:
[["John", ['A', 'B', 'B', 'C', 'D']], 
 ["Jane", ['A', 'A', 'A', 'A', 'A']],
 ["Bob",  ['B', 'B', 'A', 'D', 'D']]]
	•	For each student:
	1.	Extract their name
	2.	Extract their answers
	3.	Loop through each answer
	4.	Compare it to the corresponding answer key
	5.	Count correct answers
	6.	Calculate score and percentage
	7.	Print a formatted result

⸻

📌 Stub Code
key = ['A', 'B', 'A', 'C', 'D']

students = [
    ["John", ['A', 'B', 'B', 'C', 'D']],
    ["Jane", ['A', 'A', 'A', 'A', 'A']],
    ["Bob",  ['B', 'B', 'A', 'D', 'D']]
]

for student in students:
    name = student[0]
    answers = student[1]
  
⸻

📌 Key Concepts Learned
	•	Working with nested lists
	•	Looping through multi-level data
	•	Index-based comparison
	•	Score calculation and percentages
	•	Clean and structured output formatting

⸻

📌 Example Results
	•	John: 4/5 (80%)
	•	Jane: 1/5 (20%)
	•	Bob: 0/5 (0%)
