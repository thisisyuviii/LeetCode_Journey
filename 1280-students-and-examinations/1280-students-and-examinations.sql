# Write your MySQL query statement below
SELECT s1.student_id ,
  s1.student_name ,
  s3.subject_name ,
  COUNT(s2.student_id) AS attended_exams
FROM Students s1 
CROSS JOIN Subjects s3
LEFT JOIN Examinations s2
ON s1.student_id = s2.student_id
AND s3.subject_name=s2.subject_name
GROUP BY s1.student_id,s1.student_name,s3.subject_name
ORDER BY s1.student_id,s1.student_name,s3.subject_name