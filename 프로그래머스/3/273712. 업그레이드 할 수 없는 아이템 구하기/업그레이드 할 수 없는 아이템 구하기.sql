# 채점 결과
# 합계: 100.0 / 100.0
SELECT ITEM_ID, 
    ITEM_NAME,
    RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (
    SELECT DISTINCT PARENT_ITEM_ID
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID IS NOT NULL
)
ORDER BY 1 DESC