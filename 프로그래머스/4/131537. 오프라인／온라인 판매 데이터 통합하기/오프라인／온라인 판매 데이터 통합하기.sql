SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d'),
    PRODUCT_ID,
    USER_ID,
    SALES_AMOUNT 
FROM (
    SELECT SALES_DATE,
        PRODUCT_ID,
        USER_ID,
        SALES_AMOUNT 
    FROM ONLINE_SALE
    UNION ALL
    SELECT SALES_DATE,
        PRODUCT_ID,
        NULL AS USER_ID,
        SALES_AMOUNT 
    FROM OFFLINE_SALE
) SALES
WHERE SUBSTR(SALES_DATE, 1, 7) = '2022-03'
ORDER BY 1, 2, 3