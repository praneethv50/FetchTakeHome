SELECT
    tp.BRAND,
    COUNT(tp.RECEIPT_ID) AS receipt_count
FROM
    TRANS_PRODUCTS1 tp
JOIN
    USERS_cleaned u ON tp.USER_ID = u.ID
WHERE
    (strftime('%Y', 'now') - strftime('%Y', u.BIRTH_DATE)) >= 21
	AND BRAND is not NULL
GROUP BY
    tp.BRAND
ORDER BY
    receipt_count DESC
LIMIT 5;
