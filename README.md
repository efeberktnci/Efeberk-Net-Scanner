<img width="1596" height="757" alt="555" src="https://github.com/user-attachments/assets/883ac640-73db-42db-a7fa-852d103b3d24" />
# 🕵️‍♂️ CyberScanner: Full-Stack Network Vulnerability Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=flat&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=flat&logo=mysql)
![JavaScript](https://img.shields.io/badge/JavaScript-Matrix_UI-yellow?style=flat&logo=javascript)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat&logo=bootstrap)

## 📌 Overview
CyberScanner is a web-based, full-stack cybersecurity tool designed to perform rapid TCP port scanning on target IP addresses and hostnames. By leveraging Python's multi-threading capabilities and Socket programming, it significantly reduces scan times. 

The project features a responsive, **custom Matrix-themed user interface** built with HTML5 Canvas and JavaScript, and automatically logs all scan histories into a MySQL database for future security auditing.

## ✨ Key Features
* **🚀 High-Speed Scanning:** Utilizes Python's `threading` module to concurrently scan ports (1-1024), completing network requests in seconds.
* **🌐 Dynamic DNS Resolution:** Automatically converts target domain names (e.g., `scanme.nmap.org`) to their respective IPv4 addresses.
* **💾 Persistent Logging:** Seamlessly integrates with a MySQL database to record the target IP, identified open ports, and exact timestamps of every scan.
* **🎨 Hacker-Themed UI:** A sleek, immersive dark-mode web interface featuring an animated Matrix digital rain background using JavaScript `<canvas>`.

## 🛠️ Technology Stack
* **Frontend:** HTML5, CSS3, JavaScript (Canvas API), Bootstrap 5.3
* **Backend:** Python, Flask Framework
* **Networking:** Python `socket` module
* **Database:** MySQL, `mysql-connector-python`

## ⚙️ Installation & Setup

### 1. Database Setup (XAMPP/MySQL)
1. Start the **Apache** and **MySQL** services from your XAMPP Control Panel.
2. Open phpMyAdmin (`http://localhost/phpmyadmin`).
3. Execute the following SQL query to create the database and table:
   ```sql
   CREATE DATABASE port_scanner_db;
   USE port_scanner_db;

   CREATE TABLE scans (
       id INT AUTO_INCREMENT PRIMARY KEY,
       ip_address VARCHAR(100) NOT NULL,
       open_ports VARCHAR(255) NOT NULL,
       scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
2. Application Setup
Clone this repository to your local machine:

Bash

git clone [https://github.com/efeberktnci/CyberScanner.git](https://github.com/efeberktnci/CyberScanner.git)
Navigate to the project directory:

Bash

cd CyberScanner
Install the required Python dependencies:

Bash

python -m pip install flask mysql-connector-python
Run the Flask application:

Bash

python app.py
Open your web browser and navigate to http://127.0.0.1:5000 to start scanning!

⚠️ Disclaimer
For Educational and Authorized Testing Purposes Only. This tool is intended for network administration and security auditing. Do not use CyberScanner against networks, systems, or hostnames you do not own or do not have explicit permission to test. You can safely use scanme.nmap.org for testing purposes.
