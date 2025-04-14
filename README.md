# Inventory-Management-System
The project is designed to be simple, readable, and easily extendable. It can be used in command-line interfaces and can also be expanded into a GUI or web application in the future.
# 🔹 Project: Inventory Management System  

## 🎯 **Objective:**  
The goal of this project is to create a system that helps manage inventory efficiently. The system will allow users to:  
1. **Add products** with their quantity and price.  
2. **Sell products**, reducing their quantities in stock.  
3. **View the current inventory** in the order of product addition.  
4. **Track and display the top-selling products.**  

---

## **🔹 Features:**  
- Users can **add new products** or update the quantity of existing ones.  
- Users can **sell products**, ensuring stock updates correctly.  
- Users can **view all available products**, with their price and quantity, while maintaining the order they were first added.  
- Users can **see the most sold products**, helping them track demand.  

---

## **🔹 Technologies Used:**  
- **Ordered Dictionary (`OrderedDict`)** → Maintains the order in which products were added.  
- **Counter (`Counter`)** → Keeps track of the number of times each product has been sold.  
- **Default Dictionary (`defaultdict`)** → Handles default values for product quantities, preventing errors.  

---

## **🔹 Workflow:**  
1. **Adding Products**  
   - Users can add products by providing a name, price, and quantity.  
   - If the product already exists, its quantity is updated.  
   - The first added price remains unchanged.  

2. **Selling Products**  
   - Users can sell available products, and the system automatically updates the stock.  
   - If the requested quantity exceeds available stock, a warning is displayed.  
   - Sold products are recorded to track sales trends.  

3. **Displaying Inventory**  
   - Users can view a list of all available products along with their quantities and prices.  
   - Products are displayed in the order they were first added.  

4. **Tracking Top-Selling Products**  
   - The system ranks and displays the most sold products.  
   - This helps in understanding which products are in high demand.  

---

## **🔹 Possible Enhancements:**  
- **Database Integration:** Store inventory data permanently in a database.  
- **User Authentication:** Introduce different roles (e.g., Admin, Salesperson) with access control.  
- **Graphical Interface:** Implement a simple GUI using `Tkinter` or a web version using `Flask/Django`.  
- **Product Categories:** Classify products into categories for better organization.  
- **Stock Alerts:** Notify users when a product is running low in stock.  

---

## **🔹 How to Use the System:**  
1. **Start the system** and add products with their details.  
2. **Sell products**, and the system will automatically update the inventory.  
3. **Check inventory status** to see available products and their quantities.  
4. **View sales reports** to identify top-selling items.  

---

## **🔹 Challenge Extension:**  
- Can you add a feature that allows exporting inventory data to a CSV file?  
- How about integrating an AI-powered sales prediction model?  

**This project provides a structured way to manage inventory efficiently and can be further expanded with more advanced features!**  

