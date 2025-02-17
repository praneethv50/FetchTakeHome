SELECT
    tp.BRAND,
    SUM(tp.FINAL_SALE) AS total_sales
FROM
    TRANS_PRODUCTS1 tp
JOIN
    USERS_cleaned u ON tp.USER_ID = u.ID
WHERE
    DATE('now') >= DATE(u.CREATED_DATE, '+6 months')
	AND BRAND IS NOT NULL
GROUP BY
    tp.BRAND
ORDER BY
    total_sales DESC
LIMIT 5;
