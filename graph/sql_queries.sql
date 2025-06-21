-- This query (1) retrieves all session details for the student named 'Alice'
SELECT s.*
FROM sessions s
JOIN attendance a ON s.id = a.session_id
JOIN students st ON a.student_id = st.id
WHERE st.name = 'Alice';
-- This query (2) retrieves the top 3 students with the most sessions attended
SELECT st.name, COUNT(*) AS session_count
FROM attendance a
JOIN students st ON a.student_id = st.id
GROUP BY st.name
ORDER BY session_count DESC
LIMIT 3;
-- This query (3) retrieves the number of students who attended each session
SELECT s.id AS session_id, COUNT(DISTINCT a.student_id) AS student_count
FROM sessions s
LEFT JOIN attendance a ON s.id = a.session_id
GROUP BY s.id
ORDER BY student_count DESC;
-- This query (4) retrieves the total number of sessions for each module
SELECT m.name AS module, COUNT(DISTINCT a.student_id) AS unique_students
FROM attendance a
JOIN sessions s ON a.session_id = s.id
JOIN modules m ON s.module_id = m.id
GROUP BY m.name
ORDER BY unique_students DESC;
-- This query (5) retrieves the names of students who have never attended any session
SELECT st.name
FROM students st
LEFT JOIN attendance a ON st.id = a.student_id
WHERE a.session_id IS NULL;
-- This query (6) retrieves the sessions attended by the student named 'Alice' along with the module names
SELECT m.name AS module, s.id AS session_id
FROM students st
JOIN attendance a ON st.id = a.student_id
JOIN sessions s ON a.session_id = s.id
JOIN modules m ON s.module_id = m.id
WHERE st.name = 'Alice';




