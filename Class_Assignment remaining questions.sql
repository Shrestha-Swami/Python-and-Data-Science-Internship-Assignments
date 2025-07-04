-- What are the top 3 pages by number of views?
SELECT * FROM
(SELECT 
ph.page_name,
COUNT(*) AS views,
DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
FROM events e
JOIN page_hierarchy ph ON e.page_id = ph.page_id
WHERE e.event_type = 1
GROUP BY ph.page_name
) ranked
WHERE rank <= 3
ORDER BY rank;


-- What is the number of views and cart adds for each product category?
SELECT ph.product_category,
SUM(CASE WHEN e.event_type = 1 THEN 1 ELSE 0 END) AS page_views,
SUM(CASE WHEN e.event_type = 2 THEN 1 ELSE 0 END) AS cart_adds
FROM events e
JOIN page_hierarchy ph on e.page_id = ph.page_id
WHERE ph.product_category IS NOT NULL
GROUP BY ph.product_category;

-- What are the top 3 products by purchases?
SELECT *
FROM (
SELECT 
ph.page_name AS product_name, 
COUNT(*) AS purchase_count,
DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
FROM events e
JOIN page_hierarchy ph ON e.page_id = ph.page_id
WHERE e.event_type = 3 AND ph.product_id IS NOT NULL
GROUP BY ph.page_name
) ranked
WHERE rank <= 3
ORDER BY rank;

