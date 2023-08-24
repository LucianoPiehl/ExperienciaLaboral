import tkinter as tk
import requests
import json

class App:
    def __init__(self, master):
        self.master = master
        master.title("Enviar solicitud POST con JSON")

        self.message_label = tk.Label(master, text="Mensaje:")
        self.message_label.pack()

        self.message_entry = tk.Entry(master)
        self.message_entry.pack()

        self.username_label = tk.Label(master, text="Nombre de usuario:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Contraseña:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.submit_button = tk.Button(master, text="Enviar", command=self.send_request)
        self.submit_button.pack()

    def send_request(self):
        message = self.message_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        url = "http://lucho321.pythonanywhere.com/instagram"
        data = {"message": message, "username": username, "password": password}
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)

        response_label = tk.Label(self.master, text=response.json()['message'])
        response_label.pack()

root = tk.Tk()
app = App(root)
root.mainloop()
