-- Aggregate sales by brand within the 'Dips & Salsa' category
SELECT
    tp.BRAND,
    printf('$%.2f', SUM(tp.FINAL_SALE)) AS total_sales
FROM
    TRANS_PRODUCTS1 tp
WHERE
    tp.CATEGORY_2 = 'Dips & Salsa' -- Assuming CATEGORY_2 denotes the subcategory
    AND tp.BRAND IS NOT NULL
GROUP BY
    tp.BRAND
ORDER BY
    SUM(tp.FINAL_SALE) DESC
LIMIT 1; -- Retrieve the top brand
