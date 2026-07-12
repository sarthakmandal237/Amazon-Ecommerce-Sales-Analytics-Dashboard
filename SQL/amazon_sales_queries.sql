-- CREATE DATABASE amazon_sales;
USE amazon_sales;


-- Q1. Display all records from the sales table.
SELECT * 
FROM sales;

-- Q2. Find the total number of orders.
SELECT COUNT(*) AS Total_Orders
FROM sales;

-- Q3. Find the total revenue generated.
SELECT SUM(total_revenue) AS Total_Revenue
FROM sales;

-- Q4. Find the average revenue per order.
SELECT AVG(total_revenue) AS Average_Revenue
FROM sales;

-- Q5. Find the total quantity of products sold.
SELECT SUM(quantity_sold) AS Total_Quantity_Sold
FROM sales;

-- Q6. Find the total revenue for each product category.
SELECT product_category,
SUM(total_revenue) AS Total_Revenue
FROM sales
GROUP BY product_category;

-- Q7. Find the total quantity sold for each product category.
SELECT product_category,
SUM(quantity_sold) AS Quantity_Sold
FROM sales
GROUP BY product_category;

-- Q8. Find the total revenue generated from each customer region.
SELECT customer_region,
SUM(total_revenue) AS Total_Revenue
FROM sales
GROUP BY customer_region;

-- Q9. Find the average customer rating for each product category.
SELECT product_category,
AVG(rating) AS Average_Rating
FROM sales
GROUP BY product_category;

-- Q10. Count the number of orders for each payment method.
SELECT payment_method,
COUNT(*) AS Total_Orders
FROM sales
GROUP BY payment_method;

-- Q11. Display the top 5 product categories based on total revenue.
SELECT product_category,
SUM(total_revenue) AS Total_Revenue
FROM sales
GROUP BY product_category
ORDER BY Total_Revenue DESC
LIMIT 5;

-- Q12. Display the top 5 customer regions based on total revenue.
SELECT customer_region,
SUM(total_revenue) AS Total_Revenue
FROM sales
GROUP BY customer_region
ORDER BY Total_Revenue DESC
LIMIT 5;

-- Q13. Display the top 10 highest-rated products.
SELECT product_id,
rating
FROM sales
ORDER BY rating DESC
LIMIT 10;

-- Q14. Display the top 10 products with the highest discount percentage.
SELECT product_id,
discount_percent
FROM sales
ORDER BY discount_percent DESC
LIMIT 10;

-- Q15. Display all orders with revenue greater than 1000.
SELECT order_id,
product_category,
total_revenue
FROM sales
WHERE total_revenue > 1000;

