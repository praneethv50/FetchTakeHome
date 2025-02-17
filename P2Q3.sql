WITH GenerationSales AS (
    SELECT
        u.ID,
        CASE
            WHEN u.BIRTH_DATE BETWEEN date('now', '-24 years') AND date('now', '-18 years') THEN 'Generation Z (18-24)'
            WHEN u.BIRTH_DATE BETWEEN date('now', '-40 years') AND date('now', '-25 years') THEN 'Millennials (25-40)'
            WHEN u.BIRTH_DATE BETWEEN date('now', '-56 years') AND date('now', '-41 years') THEN 'Generation X (41-56)'
            WHEN u.BIRTH_DATE BETWEEN date('now', '-74 years') AND date('now', '-57 years') THEN 'Baby Boomers (57-74)'
            ELSE 'Other'
        END AS Generation,
        tp.CATEGORY_1,
        tp.FINAL_SALE
    FROM
        users_cleaned u
    JOIN
        trans_products1 tp ON u.ID = tp.USER_ID
    WHERE
        tp.CATEGORY_1 = 'Health & Wellness'
),
TotalSalesByGeneration AS (
    SELECT
        Generation,
        SUM(FINAL_SALE) AS TotalSales
    FROM
        GenerationSales
    GROUP BY
        Generation
),
OverallSales AS (
    SELECT
        SUM(TotalSales) AS OverallTotalSales
    FROM
        TotalSalesByGeneration
)
SELECT
    tsbg.Generation,
    CASE
        WHEN tsbg.TotalSales >= 1000000 THEN printf('$%.2fM', tsbg.TotalSales / 1000000.0)
        WHEN tsbg.TotalSales >= 1000 THEN printf('$%.2fK', tsbg.TotalSales / 1000.0)
        ELSE printf('$%.2f', tsbg.TotalSales)
    END AS TotalSales,
    printf('%.2f%%', (tsbg.TotalSales * 100.0 / os.OverallTotalSales)) AS SalesPercentage
FROM
    TotalSalesByGeneration tsbg,
    OverallSales os
ORDER BY
    tsbg.TotalSales DESC;
