import socket


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 3050))
        server.listen(6)
        print('Сервер запущен ip-127.0.0.1 port-5050 | http://127.0.0.1:3050')
        while True:
            print('Starting....')
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            # test requests
            #print(data)
            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Ошибка запуска сервера")
    
    
def load_page_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    responce = ''
    try:
        with open('templates' + path, 'rb') as file:
            responce = file.read()
        return HDRS.encode('utf-8') + responce
    except FileNotFoundError:
        return (HDRS_404 + '404 старница не найдена').encode('utf-8')


if __name__ == "__main__":
    start_server()