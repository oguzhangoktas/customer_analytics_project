{{ config(materialized='table') }}

SELECT 
    customer_id, 
    first_name || ' ' || last_name AS full_name,
    LOWER(email) AS email,
    created_at
FROM {{ source('raw', 'customers') }}
