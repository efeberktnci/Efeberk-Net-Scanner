
from flask import Flask, render_template, request
import socket
import threading
import mysql.connector

app = Flask(__name__)

# İşte MySQL Veritabanı Bağlantımız Burada!
db_config = {
    'host': 'localhost',
    'user': 'root',       # XAMPP varsayılan kullanıcı adı
    'password': '',       # XAMPP varsayılan şifre (boş)
    'database': 'port_scanner_db'
}

def scan_port(ip, port, open_ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

@app.route('/', methods=['GET', 'POST'])
def index():
    open_ports = []
    target_ip = ""
    message = ""

    if request.method == 'POST':
        target = request.form['target']
        try:
            target_ip = socket.gethostbyname(target)
            threads = []

            # Tarama işlemi (1'den 1024'e kadar)
            for port in range(1, 1025):
                t = threading.Thread(target=scan_port, args=(target_ip, port, open_ports))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            # Bulunan sonuçları MySQL Veritabanına kaydetme kısmı
            if open_ports:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                ports_str = ", ".join(map(str, sorted(open_ports)))
                cursor.execute("INSERT INTO scans (ip_address, open_ports) VALUES (%s, %s)", (target_ip, ports_str))
                conn.commit()
                cursor.close()
                conn.close()
                message = "Tarama tamamlandı ve veritabanına kaydedildi!"
            else:
                message = "Açık port bulunamadı."

        except socket.gaierror:
            message = "Geçersiz bir adres girdiniz."

    return render_template('index.html', target_ip=target_ip, open_ports=sorted(open_ports), message=message)

if __name__ == '__main__':
    app.run(debug=True)