import Recognize
import tkinter as tk
import threading

# Define the default username and password
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "password123"


# Define the function to validate the user's input
def validate_login(username_entry, password_entry):
    # Get the user's input
    username = username_entry.get()
    password = password_entry.get()

    # Check if the input matches the default username and password
    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        # If it matches, run the main program and close the login window
        root.destroy()
        import main_gui
    else:
        # If it doesn't match, show an error message
        error_label.config(text="Invalid username or password")


def rfaces_call():
    Recognize.recognize_attendence()


def RecognizeFaces():
    t4 = threading.Thread(target=rfaces_call, daemon=True)
    t4.start()


# Create the main window
root = tk.Tk()
root.title("Login")
# Create a lable for New User
admin_label = tk.Label(root, text="Login to Register New User", font=("Arial", 14, "bold"), fg="red")
admin_label.pack()
admin_label.pack()
# Create the username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create the password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create the login button
login_button = tk.Button(root, text="Login", font=("Arial", 10, "bold"), bg="green", fg="white",
                         command=lambda: validate_login(username_entry, password_entry))
login_button.pack()

# Create the error label
error_label = tk.Label(root, fg="red")
error_label.pack()

# Create the "Already registered?" label and "Mark your Attendance" button
already_registered_label = tk.Label(root, text="Already registered?", font=("Times new Roman", 12, "bold"), fg="Blue")
already_registered_label.pack()
mark_attendance_button = tk.Button(root, text="Mark your Attendance", font=("Arial", 14, "bold"), fg="white",
                                   bg="black", command=RecognizeFaces)
mark_attendance_button.pack()

# Set the size of the window
root.geometry("600x300")

# Start the main event loop
root.mainloop()
