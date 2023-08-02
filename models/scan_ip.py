import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            sock.close()
            return port
        sock.close()
    except Exception as e:
        pass
    return None


def scan_ip(ip, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Формируем список задач для сканирования портов
        tasks = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]

        # Обрабатываем завершенные задачи и собираем результаты
        for future in tasks:
            result = future.result()
            if result is not None:
                open_ports.append(result)

    if open_ports:
        return f"IP {ip} is alive. Open ports: {open_ports}"
    else:
        return f"IP {ip} is dead."
