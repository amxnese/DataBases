-- relation between two tables

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
);

CREATE TABLE grades (
    grade_id INT PRIMARY KEY,
    student_id INT,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- inserting data
INSERT INTO students (student_id, student_name)
VALUES (1, 'John'),
      (2, 'Jane');

INSERT INTO grades (grade_id, student_id, grade)
VALUES (1, 1, 'A'),
      (2, 2, 'B');

-- Now, when you query data from both tables, you can join them using the student_id column:
SELECT students.student_id, students.student_name, grades.grade
FROM students
JOIN grades ON students.student_id = grades.student_id;
