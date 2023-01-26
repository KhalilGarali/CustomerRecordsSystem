import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 9999))
    #s.sendall(b"Hello, world")
    data = s.recv(1024).decode()
    print(data)
    option = input("Please select an option from the list above:\n--> ")
    while True:
        s.sendall(option.encode())
        if option == "1":
            answer = s.recv(2048).decode()
            print(answer)
            name = input()
            s.sendall(name.encode())
            answer = s.recv(2048).decode()
            print(answer)
        elif option == "2":
            answer = s.recv(2048).decode()
            print(answer)
            name = input("-->")
            s.sendall(name.encode())
            answer = s.recv(2048).decode()
            print(answer)
            age = input("-->")
            s.sendall(age.encode())
            answer = s.recv(2048).decode()
            print(answer)
            location = input("-->")
            s.sendall(location.encode())
            answer = s.recv(2048).decode()
            print(answer)
            number = input("-->")
            s.sendall(number.encode())
            answer = s.recv(2048).decode()
            print(answer)
        elif option == "3":
            answer = s.recv(2048).decode()
            print(answer)
            name = input("-->")
            s.sendall(name.encode())
            answer = s.recv(2048).decode()
            print(answer)
        elif option == "4":
            answer = s.recv(2048).decode()
            print(answer)
            name = input("-->")
            s.sendall(name.encode())
            answer = s.recv(2048).decode()
            print(answer)
            if answer != "Customer does not exists!":
                age = input("-->")
                s.sendall(age.encode())
                answer = s.recv(2048).decode()
                print(answer)
        elif option == "5":
            answer = s.recv(2048).decode()
            print(answer)
            name = input("-->")
            s.sendall(name.encode())
            answer = s.recv(2048).decode()
            print(answer)
            if answer != "Customer does not exists!":
                address = input("-->")
                s.sendall(address.encode())
                answer = s.recv(2048).decode()
                print(answer)
        elif option == "6":
            answer = s.recv(2048).decode()
            print(answer)
            name = input("-->")
            s.sendall(name.encode())
            answer = s.recv(2048).decode()
            print(answer)
            if answer != "Customer does not exists!":
                phone_number = input("-->")
                s.sendall(phone_number.encode())
                answer = s.recv(2048).decode()
                print(answer)
        elif option == "7":
            answer = s.recv(2048).decode()
            print(answer)
        elif option == "8":
            s.sendall(bytes("", "utf-8"))
            print("Good bye.")
            break
        option = input("Please select an option from the list above:\n--> ")








