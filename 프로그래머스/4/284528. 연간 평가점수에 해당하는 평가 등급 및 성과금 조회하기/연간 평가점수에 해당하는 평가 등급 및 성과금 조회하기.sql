# -- 코드를 작성해주세요
# WITH EMP_GRADE AS (
#     SELECT EMP_NO,
#         CASE
#             WHEN AVG(SCORE) > 96 THEN 'S'
#             WHEN AVG(SCORE) > 90 THEN 'A'
#             WHEN AVG(SCORE) > 80 THEN 'B' ELSE 'C'
#         END AS "GRADE"
#     FROM HR_GRADE
#     GROUP BY EMP_NO
# )
# SELECT HE.EMP_NO, 
#     HE.EMP_NAME,
#     EG.GRADE,
#     CASE
#         WHEN EG.GRADE = 'S' THEN HE.SAL * 0.2
#         WHEN EG.GRADE = 'A' THEN HE.SAL * 0.15
#         WHEN EG.GRADE = 'B' THEN HE.SAL * 0.1 ELSE 0
#     END AS "BONUS"
# FROM HR_EMPLOYEES HE,
#     EMP_GRADE EG
# WHERE HE.EMP_NO = EG.EMP_NO
# ORDER BY 1

SELECT A.EMP_NO, B.EMP_NAME, (CASE
             WHEN AVG(SCORE) >= 96 THEN 'S'
             WHEN AVG(SCORE) >= 90 THEN 'A'
             WHEN AVG(SCORE) >= 80 THEN 'B'
             ELSE 'C' END) AS GRADE, SAL * (CASE
             WHEN AVG(SCORE) >= 96 THEN 0.2
             WHEN AVG(SCORE) >= 90 THEN 0.15
             WHEN AVG(SCORE) >= 80 THEN 0.1
             ELSE 0 END) AS BONUS
FROM HR_GRADE A JOIN HR_EMPLOYEES B ON A.EMP_NO = B.EMP_NO
GROUP BY EMP_NO
ORDER BY A.EMP_NO