{{ config(materialized='table') }}

SELECT 
    customer_id,
    COUNT(order_id) AS total_orders,   
    SUM(total_amount) AS total_spent  
FROM {{ source('raw', 'orders') }}
GROUP BY customer_id
