import socket


def read_data(fname):
    d = {}
    with open(fname) as fi:
        for li in fi:
            (n, a, loc, num) = li.split("|")
            d[str(n)] = [a, loc, num]
    return d


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 9999))
    while True:
        s.listen()
        conn, address = s.accept()
        with conn:
            print(f"Connection from {address} has been established.")
            conn.send(bytes("Python DB menu\n"
                            "\n1. Find customer\n"
                            "2. Add customer\n"
                            "3. Delete customer\n"
                            "4. Update customer age\n"
                            "5. Update customer address\n"
                            "6. Update customer phone\n"
                            "7. Print report\n"
                            "8. Exit\n", "utf-8"))
                            #"\nSelect: "))

            while True:
                data = conn.recv(1024).decode()
                #print("from connected user: " + str(data))
                if str(data) == "1":
                    conn.send(bytes("Customer name:", "utf-8"))
                    customer_name = conn.recv(1024).decode()
                    key_list = read_data("data.txt").keys()
                    if key_list.__contains__(customer_name):
                        value_list = read_data("data.txt")[customer_name]
                        info = "Server response: "
                        info += customer_name + "|" + value_list[0] + "|" + value_list[1] + "|" + value_list[2]
                        conn.send(info.encode())
                    else:
                        conn.send(bytes(f"Server response: {customer_name} not found in database", "utf-8"))
                elif str(data) == "2":
                    info = "Name of customer you would like to add: "
                    conn.send(info.encode())
                    customer_name = conn.recv(1024).decode()
                    info = "Age of customer you would like to add: "
                    conn.send(info.encode())
                    customer_age = conn.recv(1024).decode()
                    info = "Address of customer you would like to add: "
                    conn.send(info.encode())
                    customer_address = conn.recv(1024).decode()
                    info = "Phone number of customer you would like to add: "
                    conn.send(info.encode())
                    customer_number = conn.recv(1024).decode()
                    key_list = read_data("data.txt").keys()
                    if key_list.__contains__(customer_name):
                        conn.send(bytes("Customer already exists!", "utf-8"))
                    else:
                        read_data("data.txt")[customer_name] = [customer_age, customer_address, customer_number]
                        with open("data.txt", "a") as f:
                            f.write(customer_name + "|" + customer_age + "|" + customer_address + "|" + customer_number + "\n")
                        conn.send(bytes("Customer added!", "utf-8"))
                        #print(read_data("data.txt")[customer_name])
                        #print(read_data("data.txt"))
                elif str(data) == "3":
                    info = "Name of customer you would like to delete: "
                    conn.send(info.encode())
                    customer_name = conn.recv(1024).decode()
                    key_list = read_data("data.txt").keys()
                    if key_list.__contains__(customer_name):
                        with open("data.txt", "r") as f:
                            lines = f.readlines()
                        with open("data.txt", "w") as f:
                            for line in lines:
                                x = line.strip("\n").split("|")
                                if x[0] != customer_name:
                                    f.write(line)
                        conn.send(bytes("Customer deleted successfully!", "utf-8"))
                        #print(read_data("data.txt"))
                    else:
                        conn.send(bytes("Customer does not exists!", "utf-8"))
                elif str(data) == "4":
                    info = "Name of customer you would like to update (age): "
                    conn.send(info.encode())
                    customer_name = conn.recv(1024).decode()
                    key_list = read_data("data.txt").keys()
                    if key_list.__contains__(customer_name):
                        info = f"New age of {customer_name}: "
                        conn.send(info.encode())
                        new_age = conn.recv(1024).decode()
                        with open("data.txt", "r") as f:
                            lines = f.readlines()
                        with open("data.txt", "w") as f:
                            for line in lines:
                                x = line.strip("\n").split("|")
                                if x[0] != customer_name:
                                    f.write(line)
                                else:
                                    x[1] = new_age
                                    f.write(x[0] + "|" + x[1] + "|" + x[2] + "|" + x[3] + "\n")
                        #print(read_data("data.txt"))
                        info = "Age successfully updated "
                        conn.send(info.encode())
                    else:
                        conn.send(bytes("Customer does not exists!", "utf-8"))
                elif str(data) == "5":
                    info = "Name of customer you would like to update (address): "
                    conn.send(info.encode())
                    customer_name = conn.recv(1024).decode()
                    key_list = read_data("data.txt").keys()
                    if key_list.__contains__(customer_name):
                        info = f"New address of {customer_name}: "
                        conn.send(info.encode())
                        new_address = conn.recv(1024).decode()
                        with open("data.txt", "r") as f:
                            lines = f.readlines()
                        with open("data.txt", "w") as f:
                            for line in lines:
                                x = line.strip("\n").split("|")
                                if x[0] != customer_name:
                                    f.write(line)
                                else:
                                    x[2] = new_address
                                    f.write(x[0] + "|" + x[1] + "|" + x[2] + "|" + x[3] + "\n")
                        #print(read_data("data.txt"))
                        info = "Address successfully updated "
                        conn.send(info.encode())
                    else:
                        conn.send(bytes("Customer does not exists!", "utf-8"))

                elif str(data) == "6":
                    info = "Name of customer you would like to update (number): "
                    conn.send(info.encode())
                    customer_name = conn.recv(1024).decode()
                    key_list = read_data("data.txt").keys()
                    if key_list.__contains__(customer_name):
                        info = f"New phone number of {customer_name}: "
                        conn.send(info.encode())
                        new_number = conn.recv(1024).decode()
                        with open("data.txt", "r") as f:
                            lines = f.readlines()
                        with open("data.txt", "w") as f:
                            for line in lines:
                                x = line.strip("\n").split("|")
                                if x[0] != customer_name:
                                    f.write(line)
                                else:
                                    x[3] = new_number
                                    f.write(x[0] + "|" + x[1] + "|" + x[2] + "|" + x[3] + "\n")
                        #print(read_data("data.txt"))
                        info = "Phone number successfully updated "
                        conn.send(info.encode())
                    else:
                        conn.send(bytes("Customer does not exists!", "utf-8"))
                elif str(data) == "7":
                        mystr = "** Python DB contents **\n"
                        keylist = list(read_data("data.txt").keys())
                        sorted_list = sorted(keylist, key=str.casefold)
                        for keys in sorted_list:
                            value_list = read_data("data.txt")[keys]
                            #print(keys + "|" + value_list[0] + "|" + value_list[1] + "|" + value_list[2])
                            mystr += keys + "|" + value_list[0] + "|" + value_list[1] + "|" + value_list[2]
                        conn.send(mystr.encode())
                elif str(data) == "8":
                    response = conn.recv(1024).decode()
                    break



