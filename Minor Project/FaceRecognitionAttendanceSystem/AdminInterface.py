# import tkinter as tk
# from tkinter import messagebox, filedialog
# from PIL import ImageTk, Image
# import os
# import shutil
# import firebase_admin
# from firebase_admin import credentials, db
#
#
# # Initialize Firebase
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': ""
# })
#
# # Admin login credentials
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "password"  # Set your desired admin password
#
#
# # Function to authenticate admin login
# def admin_login():
#     username = username_entry.get()
#     password = password_entry.get()
#
#     if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#         login_frame.pack_forget()  # Hide the login frame
#         show_admin_options()  # Show admin options
#     else:
#         messagebox.showerror("Login Failed", "Invalid username or password.")
#
#
# # Function to show the admin options (Add, Update, Delete)
# def show_admin_options():
#     admin_options_frame.pack(pady=20)
#
#
# # Function to add a new student
# def add_student():
#     admin_options_frame.pack_forget()  # Hide admin options
#     add_student_frame.pack(pady=20)  # Show add student form
#
#
# # Function to update an existing student
# def update_student():
#     admin_options_frame.pack_forget()  # Hide admin options
#     update_student_frame.pack(pady=20)  # Show update student form
#
#
# # Function to delete an existing student
# def delete_student():
#     admin_options_frame.pack_forget()  # Hide admin options
#     delete_student_frame.pack(pady=20)  # Show delete student form
#
#
# # Function to return to the admin options menu
# def go_back_to_options():
#     add_student_frame.pack_forget()
#     update_student_frame.pack_forget()
#     delete_student_frame.pack_forget()
#     admin_options_frame.pack(pady=20)
#
#
# # Function to save new student data to the Firebase database
# def save_new_student():
#     student_id = student_id_entry.get()
#     name = name_entry.get()
#     course = course_entry.get()
#     starting_year = starting_year_entry.get()
#     standing = standing_entry.get()
#     year = year_entry.get()
#
#     # Ensure all fields and image are filled/selected
#     if student_id and name and course and starting_year and standing and year and uploaded_image_path:
#         ref = db.reference('Students')
#
#         if ref.child(student_id).get() is not None:
#             messagebox.showerror("Error", "Student ID already exists.")
#         else:
#             data = {
#                 student_id: {
#                     "name": name,
#                     "course": course,
#                     "starting_year": starting_year,
#                     "total_attendance": 0,
#                     "standing": standing,
#                     "year": year,
#                     "last_attendance_time": "0000-00-00 00:00:00"  # Default
#                 }
#             }
#
#             ref.update(data)  # Add to database
#             messagebox.showinfo("Success", "Student added successfully.")
#
#             # Save student image
#             if not os.path.exists("Images"):
#                 os.makedirs("Images")
#             new_img_path = os.path.join("Images", f"{student_id}.jpg")
#             shutil.copy(uploaded_image_path, new_img_path)
#             messagebox.showinfo("Success", "Image uploaded successfully.")
#
#             go_back_to_options()
#     else:
#         messagebox.showerror("Error", "All fields and an image are required.")
#
#
# # Track image path
# uploaded_image_path = None
#
#
# # Function to upload the student image
# def upload_student_image():
#     global uploaded_image_path
#     img_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
#     if img_path:
#         uploaded_image_path = img_path
#         messagebox.showinfo("Success", "Image selected successfully.")
#
#
# # Function to reset fields
# def reset_fields():
#     student_id_entry.delete(0, tk.END)
#     name_entry.delete(0, tk.END)
#     course_entry.delete(0, tk.END)
#     starting_year_entry.delete(0, tk.END)
#     standing_entry.delete(0, tk.END)
#     year_entry.delete(0, tk.END)
#     global uploaded_image_path
#     uploaded_image_path = None
#
#
# # Function to load student data for updating
# def load_student_data_for_update():
#     student_id = update_student_id_entry.get()
#     ref = db.reference(f'Students/{student_id}')
#     student_data = ref.get()
#
#     if student_data:
#         name_entry_update.delete(0, tk.END)
#         name_entry_update.insert(0, student_data["name"])
#
#         course_entry_update.delete(0, tk.END)
#         course_entry_update.insert(0, student_data["course"])
#
#         starting_year_entry_update.delete(0, tk.END)
#         starting_year_entry_update.insert(0, student_data["starting_year"])
#
#         standing_entry_update.delete(0, tk.END)
#         standing_entry_update.insert(0, student_data["standing"])
#
#         year_entry_update.delete(0, tk.END)
#         year_entry_update.insert(0, student_data["year"])
#     else:
#         messagebox.showerror("Error", "Student ID not found.")
#
#
# # Function to update student data
# def update_student_data():
#     student_id = update_student_id_entry.get()
#     name = name_entry_update.get()
#     course = course_entry_update.get()
#     starting_year = starting_year_entry_update.get()
#     standing = standing_entry_update.get()
#     year = year_entry_update.get()
#
#     if student_id and name and course and starting_year and standing and year:
#         ref = db.reference(f'Students/{student_id}')
#
#         student_data = {
#             "name": name,
#             "course": course,
#             "starting_year": starting_year,
#             "standing": standing,
#             "year": year,
#             "last_attendance_time": "0000-00-00 00:00:00"  # Default
#         }
#
#         ref.update(student_data)  # Update database
#         messagebox.showinfo("Success", "Student updated successfully.")
#         go_back_to_options()
#     else:
#         messagebox.showerror("Error", "All fields are required.")
#
#
# # Function to delete student data and image
# def delete_student_data():
#     student_id = delete_student_id_entry.get()  # Get student ID from entry field
#     ref = db.reference(f'Students/{student_id}')
#     student_data = ref.get()
#
#     if student_data:
#         # Confirm deletion with the user
#         confirmation = messagebox.askyesno("Confirm Deletion",
#                                            f"Are you sure you want to delete {student_data['name']}?")
#         if confirmation:
#             # Delete student data from the Firebase database
#             ref.delete()
#
#             # Define the image path and check if the image exists
#             image_path = os.path.join("Images", f"{student_id}.jpg")
#             if os.path.exists(image_path):
#                 os.remove(image_path)  # Delete the image file
#                 messagebox.showinfo("Success", "Student data and image deleted successfully.")
#             else:
#                 messagebox.showinfo("Success", "Student data deleted successfully, but no image was found.")
#
#             go_back_to_options()  # Return to admin options
#     else:
#         # Display error if student ID does not exist in the database
#         messagebox.showerror("Error", "Student ID not found.")
#
#
# # Create the main window
# root = tk.Tk()
# root.title("Admin Login")
# root.geometry("400x300")
#
# # Admin login frame
# login_frame = tk.Frame(root)
# login_frame.pack(pady=20)
#
# username_label = tk.Label(login_frame, text="Username:")
# username_label.grid(row=0, column=0)
# username_entry = tk.Entry(login_frame)
# username_entry.grid(row=0, column=1)
#
# password_label = tk.Label(login_frame, text="Password:")
# password_label.grid(row=1, column=0)
# password_entry = tk.Entry(login_frame, show="*")
# password_entry.grid(row=1, column=1)
#
# login_button = tk.Button(login_frame, text="Login", command=admin_login)
# login_button.grid(row=2, columnspan=2)
#
# # Admin options frame
# admin_options_frame = tk.Frame(root)
#
# add_button = tk.Button(admin_options_frame, text="Add New Student", command=add_student)
# add_button.grid(row=0, columnspan=2)
#
# update_button = tk.Button(admin_options_frame, text="Update Existing Student", command=update_student)
# update_button.grid(row=1, columnspan=2)
#
# delete_button = tk.Button(admin_options_frame, text="Delete Existing Student", command=delete_student)
# delete_button.grid(row=2, columnspan=2)
#
# # Add student frame
# add_student_frame = tk.Frame(root)
#
# student_id_label = tk.Label(add_student_frame, text="Student ID:")
# student_id_label.grid(row=0, column=0)
# student_id_entry = tk.Entry(add_student_frame)
# student_id_entry.grid(row=0, column=1)
#
# name_label = tk.Label(add_student_frame, text="Name:")
# name_label.grid(row=1, column=0)
# name_entry = tk.Entry(add_student_frame)
# name_entry.grid(row=1, column=1)
#
# course_label = tk.Label(add_student_frame, text="Course:")
# course_label.grid(row=2, column=0)
# course_entry = tk.Entry(add_student_frame)
# course_entry.grid(row=2, column=1)
#
# starting_year_label = tk.Label(add_student_frame, text="Starting Year:")
# starting_year_label.grid(row=3, column=0)
# starting_year_entry = tk.Entry(add_student_frame)
# starting_year_entry.grid(row=3, column=1)
#
# standing_label = tk.Label(add_student_frame, text="Standing:")
# standing_label.grid(row=4, column=0)
# standing_entry = tk.Entry(add_student_frame)
# standing_entry.grid(row=4, column=1)
#
# year_label = tk.Label(add_student_frame, text="Year:")
# year_label.grid(row=5, column=0)
# year_entry = tk.Entry(add_student_frame)
# year_entry.grid(row=5, column=1)
#
# upload_image_button = tk.Button(add_student_frame, text="Upload Image", command=upload_student_image)
# upload_image_button.grid(row=6, columnspan=2, pady=(10, 10))
#
# # Placing Reset, Add Student, and Back buttons in the same row
# reset_button = tk.Button(add_student_frame, text="Reset", command=reset_fields)
# reset_button.grid(row=7, column=0, sticky='ew', padx=5)
#
# add_student_button = tk.Button(add_student_frame, text="Add Student", command=save_new_student)
# add_student_button.grid(row=7, column=1, sticky='ew', padx=5)
#
# back_button = tk.Button(add_student_frame, text="Back", command=go_back_to_options)
# back_button.grid(row=7, column=2, sticky='ew', padx=5)
#
# # Update student frame
# update_student_frame = tk.Frame(root)
#
# update_student_id_label = tk.Label(update_student_frame, text="Student ID:")
# update_student_id_label.grid(row=0, column=0)
# update_student_id_entry = tk.Entry(update_student_frame)
# update_student_id_entry.grid(row=0, column=1)
#
# load_button = tk.Button(update_student_frame, text="Load Data", command=load_student_data_for_update)
# load_button.grid(row=1, columnspan=2)
#
# name_label_update = tk.Label(update_student_frame, text="Name:")
# name_label_update.grid(row=2, column=0)
# name_entry_update = tk.Entry(update_student_frame)
# name_entry_update.grid(row=2, column=1)
#
# course_label_update = tk.Label(update_student_frame, text="Course:")
# course_label_update.grid(row=3, column=0)
# course_entry_update = tk.Entry(update_student_frame)
# course_entry_update.grid(row=3, column=1)
#
# starting_year_label_update = tk.Label(update_student_frame, text="Starting Year:")
# starting_year_label_update.grid(row=4, column=0)
# starting_year_entry_update = tk.Entry(update_student_frame)
# starting_year_entry_update.grid(row=4, column=1)
#
# standing_label_update = tk.Label(update_student_frame, text="Standing:")
# standing_label_update.grid(row=5, column=0)
# standing_entry_update = tk.Entry(update_student_frame)
# standing_entry_update.grid(row=5, column=1)
#
# year_label_update = tk.Label(update_student_frame, text="Year:")
# year_label_update.grid(row=6, column=0)
# year_entry_update = tk.Entry(update_student_frame)
# year_entry_update.grid(row=6, column=1)
#
# update_student_button = tk.Button(update_student_frame, text="Update Student", command=update_student_data)
# update_student_button.grid(row=7, columnspan=2)
#
# back_button_update = tk.Button(update_student_frame, text="Back", command=go_back_to_options)
# back_button_update.grid(row=8, columnspan=2)
#
# # Delete student frame
# delete_student_frame = tk.Frame(root)
#
# delete_student_id_label = tk.Label(delete_student_frame, text="Student ID:")
# delete_student_id_label.grid(row=0, column=0)
# delete_student_id_entry = tk.Entry(delete_student_frame)
# delete_student_id_entry.grid(row=0, column=1)
#
# delete_student_button = tk.Button(delete_student_frame, text="Delete Student", command=delete_student_data)
# delete_student_button.grid(row=1, columnspan=2)
#
# back_button_delete = tk.Button(delete_student_frame, text="Back", command=go_back_to_options)
# back_button_delete.grid(row=2, columnspan=2)
#
# # Run the main loop
# root.mainloop()






import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import os
import shutil
import firebase_admin
from firebase_admin import credentials, db


# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendsys-default-rtdb.firebaseio.com/"
})

# Admin login credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"  # Set your desired admin password


# Colors and styles
BG_COLOR = "#1E1E1E"  # Dark gray background for a professional, non-intrusive look
FG_COLOR = "#D4D4D4"  # Soft, light gray for primary text for easy readability
BUTTON_BG_COLOR = "#007ACC"  # Vibrant blue for buttons to stand out as actionable elements
BUTTON_TEXT_COLOR = "#FFFFFF"  # White text for buttons to contrast with the blue background
ENTRY_BG_COLOR = "#333333"  # Slightly lighter gray for entry fields to distinguish from main background
ENTRY_TEXT_COLOR = "#D4D4D4"  # Light gray for entry text to match main text color

# Function to authenticate admin login
def admin_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        login_frame.pack_forget()  # Hide the login frame
        show_admin_options()  # Show admin options
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


# Function to show the admin options (Add, Update, Delete)
def show_admin_options():
    admin_options_frame.pack(pady=20)


# Function to add a new student
def add_student():
    admin_options_frame.pack_forget()  # Hide admin options
    add_student_frame.pack(pady=20)  # Show add student form


# Function to update an existing student
def update_student():
    admin_options_frame.pack_forget()  # Hide admin options
    update_student_frame.pack(pady=20)  # Show update student form


# Function to delete an existing student
def delete_student():
    admin_options_frame.pack_forget()  # Hide admin options
    delete_student_frame.pack(pady=20)  # Show delete student form


# Function to return to the admin options menu
def go_back_to_options():
    add_student_frame.pack_forget()
    update_student_frame.pack_forget()
    delete_student_frame.pack_forget()
    admin_options_frame.pack(pady=20)


# Function to save new student data to the Firebase database
def save_new_student():
    student_id = student_id_entry.get().strip()
    name = name_entry.get()
    course = course_entry.get()
    starting_year = starting_year_entry.get()
    standing = standing_entry.get()
    year = year_entry.get()

    # Ensure all fields and image are filled/selected
    if student_id and name and course and starting_year and standing and year and uploaded_image_path:
        ref = db.reference('Students')

        if ref.child(student_id).get() is not None:
            messagebox.showerror("Error", "Student ID already exists.")
        else:
            data = {
                student_id: {
                    "name": name,
                    "course": course,
                    "starting_year": starting_year,
                    "total_attendance": 0,
                    "standing": standing,
                    "year": year,
                    "last_attendance_time": "2024-01-01 00:00:00"  # Default
                }
            }

            ref.update(data)  # Add to database
            messagebox.showinfo("Success", "Student added successfully.")

            # Save student image
            if not os.path.exists("Images"):
                os.makedirs("Images")
            new_img_path = os.path.join("Images", f"{student_id}.jpg")
            shutil.copy(uploaded_image_path, new_img_path)
            messagebox.showinfo("Success", "Image uploaded successfully.")

            go_back_to_options()
    else:
        messagebox.showerror("Error", "All fields and an image are required.")


# Track image path
uploaded_image_path = None


# Function to upload the student image
def upload_student_image():
    global uploaded_image_path
    img_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if img_path:
        uploaded_image_path = img_path
        messagebox.showinfo("Success", "Image selected successfully.")


# Function to reset fields
def reset_fields():
    student_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    starting_year_entry.delete(0, tk.END)
    standing_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    global uploaded_image_path
    uploaded_image_path = None


# Function to load student data for updating
def load_student_data_for_update():
    student_id = update_student_id_entry.get().strip()
    ref = db.reference(f'Students/{student_id}')
    student_data = ref.get()

    if student_data:
        name_entry_update.delete(0, tk.END)
        name_entry_update.insert(0, student_data["name"])

        course_entry_update.delete(0, tk.END)
        course_entry_update.insert(0, student_data["course"])

        starting_year_entry_update.delete(0, tk.END)
        starting_year_entry_update.insert(0, student_data["starting_year"])

        standing_entry_update.delete(0, tk.END)
        standing_entry_update.insert(0, student_data["standing"])

        year_entry_update.delete(0, tk.END)
        year_entry_update.insert(0, student_data["year"])
    else:
        messagebox.showerror("Error", "Student ID not found.")


# Function to update student data
def update_student_data():
    student_id = update_student_id_entry.get().strip()
    name = name_entry_update.get()
    course = course_entry_update.get()
    starting_year = starting_year_entry_update.get()
    standing = standing_entry_update.get()
    year = year_entry_update.get()

    if student_id and name and course and starting_year and standing and year:
        ref = db.reference(f'Students/{student_id}')

        student_data = {
            "name": name,
            "course": course,
            "starting_year": starting_year,
            "standing": standing,
            "year": year,
            "last_attendance_time": "2024-01-01 00:00:00"  # Default
        }

        ref.update(student_data)  # Update database
        messagebox.showinfo("Success", "Student updated successfully.")
        go_back_to_options()
    else:
        messagebox.showerror("Error", "All fields are required.")


# Function to delete student data and image
def delete_student_data():
    student_id = delete_student_id_entry.get().strip()  # Get student ID from entry field
    ref = db.reference(f'Students/{student_id}')
    student_data = ref.get()

    if student_data:
        # Confirm deletion with the user
        confirmation = messagebox.askyesno("Confirm Deletion",
                                           f"Are you sure you want to delete {student_data['name']}?")
        if confirmation:
            # Delete student data from the Firebase database
            ref.delete()

            # Define the image path and check if the image exists
            image_path = os.path.join("Images", f"{student_id}.jpg")
            if os.path.exists(image_path):
                os.remove(image_path)  # Delete the image file
                messagebox.showinfo("Success", "Student data and image deleted successfully.")
            else:
                messagebox.showinfo("Success", "Student data deleted successfully, but no image was found.")

            go_back_to_options()  # Return to admin options
    else:
        # Display error if student ID does not exist in the database
        messagebox.showerror("Error", "Student ID not found.")


# Helper function to configure widgets' styles
def configure_widget(widget):
    widget.configure(bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0)
    widget.grid(pady=5, padx=5)


# Create the main window
root = tk.Tk()
root.title("Admin Login")
root.geometry("400x500")
root.configure(bg=BG_COLOR)

# Admin login frame
login_frame = tk.Frame(root, bg=BG_COLOR)
login_frame.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:", fg=FG_COLOR, bg=BG_COLOR)
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:", fg=FG_COLOR, bg=BG_COLOR)
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*", bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=admin_login, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
login_button.grid(row=2, columnspan=2)

# Admin options frame
admin_options_frame = tk.Frame(root, bg=BG_COLOR)

add_button = tk.Button(admin_options_frame, text="Add New Student", command=add_student, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
add_button.grid(row=0, columnspan=2, pady=10)

update_button = tk.Button(admin_options_frame, text="Update Existing Student", command=update_student, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
update_button.grid(row=1, columnspan=2, pady=10)

delete_button = tk.Button(admin_options_frame, text="Delete Student", command=delete_student, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
delete_button.grid(row=2, columnspan=2, pady=10)

# Add Student Frame
add_student_frame = tk.Frame(root, bg=BG_COLOR)

# Student ID
student_id_label = tk.Label(add_student_frame, text="Student ID:", fg=FG_COLOR, bg=BG_COLOR)
student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
student_id_entry = tk.Entry(add_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
student_id_entry.grid(row=0, column=1, padx=10, pady=5)

# Name
name_label = tk.Label(add_student_frame, text="Name:", fg=FG_COLOR, bg=BG_COLOR)
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(add_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# Course
course_label = tk.Label(add_student_frame, text="Course:", fg=FG_COLOR, bg=BG_COLOR)
course_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
course_entry = tk.Entry(add_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
course_entry.grid(row=2, column=1, padx=10, pady=5)

# Starting Year
starting_year_label = tk.Label(add_student_frame, text="Starting Year:", fg=FG_COLOR, bg=BG_COLOR)
starting_year_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
starting_year_entry = tk.Entry(add_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
starting_year_entry.grid(row=3, column=1, padx=10, pady=5)

# Standing
standing_label = tk.Label(add_student_frame, text="Standing:", fg=FG_COLOR, bg=BG_COLOR)
standing_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
standing_entry = tk.Entry(add_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
standing_entry.grid(row=4, column=1, padx=10, pady=5)

# Year
year_label = tk.Label(add_student_frame, text="Year:", fg=FG_COLOR, bg=BG_COLOR)
year_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
year_entry = tk.Entry(add_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
year_entry.grid(row=5, column=1, padx=10, pady=5)

# Upload Image Button
upload_image_button = tk.Button(add_student_frame, text="Upload Image", command=upload_student_image, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
upload_image_button.grid(row=6, columnspan=2, pady=10)

# Reset Fields Button
reset_button = tk.Button(add_student_frame, text="Reset", command=reset_fields, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
reset_button.grid(row=7, column=0, sticky='ew', padx=5, pady=(10, 5))

# Add Student Button
add_student_button = tk.Button(add_student_frame, text="Add Student", command=save_new_student, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
add_student_button.grid(row=7, column=1, sticky='ew', padx=5, pady=(10, 5))

# Back Button
back_button = tk.Button(add_student_frame, text="Back", command=go_back_to_options, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
back_button.grid(row=8, columnspan=2, pady=10)


# Update Student Frame
update_student_frame = tk.Frame(root, bg=BG_COLOR)

update_student_id_label = tk.Label(update_student_frame, text="Student ID to Update:", fg=FG_COLOR, bg=BG_COLOR)
update_student_id_label.grid(row=0, column=0)
update_student_id_entry = tk.Entry(update_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
update_student_id_entry.grid(row=0, column=1)

load_data_button = tk.Button(update_student_frame, text="Load Data", command=load_student_data_for_update, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
load_data_button.grid(row=1, columnspan=2, pady=10)

name_label_update = tk.Label(update_student_frame, text="Name:", fg=FG_COLOR, bg=BG_COLOR)
name_label_update.grid(row=2, column=0)
name_entry_update = tk.Entry(update_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
name_entry_update.grid(row=2, column=1)

course_label_update = tk.Label(update_student_frame, text="Course:", fg=FG_COLOR, bg=BG_COLOR)
course_label_update.grid(row=3, column=0)
course_entry_update = tk.Entry(update_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
course_entry_update.grid(row=3, column=1)

starting_year_label_update = tk.Label(update_student_frame, text="Starting Year:", fg=FG_COLOR, bg=BG_COLOR)
starting_year_label_update.grid(row=4, column=0)
starting_year_entry_update = tk.Entry(update_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
starting_year_entry_update.grid(row=4, column=1)

standing_label_update = tk.Label(update_student_frame, text="Standing:", fg=FG_COLOR, bg=BG_COLOR)
standing_label_update.grid(row=5, column=0)
standing_entry_update = tk.Entry(update_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
standing_entry_update.grid(row=5, column=1)

year_label_update = tk.Label(update_student_frame, text="Year:", fg=FG_COLOR, bg=BG_COLOR)
year_label_update.grid(row=6, column=0)
year_entry_update = tk.Entry(update_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
year_entry_update.grid(row=6, column=1)

update_button = tk.Button(update_student_frame, text="Update", command=update_student_data, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
update_button.grid(row=7, columnspan=2, pady=10)

back_button_update = tk.Button(update_student_frame, text="Back", command=go_back_to_options, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
back_button_update.grid(row=8, columnspan=2, pady=5)

# Delete Student Frame
delete_student_frame = tk.Frame(root, bg=BG_COLOR)

delete_student_id_label = tk.Label(delete_student_frame, text="Student ID to Delete:", fg=FG_COLOR, bg=BG_COLOR)
delete_student_id_label.grid(row=0, column=0)
delete_student_id_entry = tk.Entry(delete_student_frame, bg=ENTRY_BG_COLOR, fg=ENTRY_TEXT_COLOR)
delete_student_id_entry.grid(row=0, column=1)

delete_button = tk.Button(delete_student_frame, text="Delete", command=delete_student_data, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
delete_button.grid(row=1, columnspan=2, pady=10)

back_button_delete = tk.Button(delete_student_frame, text="Back", command=go_back_to_options, bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
back_button_delete.grid(row=2, columnspan=2, pady=5)

# Start the application
root.mainloop()

