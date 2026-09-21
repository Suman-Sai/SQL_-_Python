# 🛒 E-Commerce Data Analytics & SQL Capstone Project

## 📌 Project Overview
This project performs an end-to-end exploratory data analysis (EDA) and SQL-based performance reporting for an e-commerce platform. By integrating a relational MySQL database with Python (`pandas`, `seaborn`), we extracted transactional metrics, evaluated customer segmentation, and analyzed fulfillment pipelines.

---

## 🗄️ Database Architecture
The project analyzes 5 relational tables:
* **Customers:** Demographics, city/state details, registration date, customer tier (`Regular`, `VIP`).
* **Products:** Product catalog, categories, subcategories, unit cost, and unit price.
* **Orders:** Order timeline, delivery tracking, and shipping status.
* **Order Items:** Item-level purchase volume, prices, and discounts.
* **Payments:** Payment mode, transaction status, and amounts.

---

## 💡 Key Business Insights
1. **Fulfillment Efficiency:** Delivery schedules average 2–6 days for completed orders; processing orders maintain zero shipping timestamps as expected.
2. **Payment Dynamics:** Cash on Delivery and Credit Cards account for the highest volume of successful transactions.
3. **Revenue Drivers:** VIP customers contribute significantly to higher Average Order Value (AOV), proving loyalty strategies are effective.

---

## 🛠️ Tech Stack & Prerequisites
* **Database:** MySQL Server
* **Language:** Python 3.x
* **Libraries:** `pandas`, `mysql-connector-python`, `matplotlib`, `seaborn`

---
