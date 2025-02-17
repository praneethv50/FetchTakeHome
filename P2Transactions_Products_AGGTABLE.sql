-- Create the new table by joining the TRANSACTIONS table with the aggregated data
CREATE TABLE TRANS_PRODUCTS1 AS
WITH agg AS (
    SELECT 
        BARCODE, 
        MAX(CATEGORY_1) AS CATEGORY_1,
        MAX(CATEGORY_2) AS CATEGORY_2,
        MAX(CATEGORY_3) AS CATEGORY_3,
        MAX(BRAND) AS BRAND
    FROM products_cleaned2
    GROUP BY BARCODE
)
SELECT
    t.*,
    agg.CATEGORY_1,
    agg.CATEGORY_2,
    agg.CATEGORY_3,
    agg.BRAND
FROM
    TRANSACTION_TAKEHOME t
    LEFT JOIN agg ON t.BARCODE = agg.BARCODE;
