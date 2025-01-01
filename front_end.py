import tkinter as tk
from tkinter import messagebox
import requests
from tkinter import ttk
import subprocess
from PIL import Image, ImageTk
import io  # Add this import at the beginning
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

BASE_URL = "http://127.0.0.1:8000/patient/"
BASE_URL3 = "http://127.0.0.1:8000/services/"
DOCTOR_LIST_URL = "http://127.0.0.1:8000/doctor/list/"
APPOINTMENT_URL = "http://127.0.0.1:8000/appointment/"
DOCTOR_REVIEWS_URL = "http://127.0.0.1:8000/doctor/reviews/"
BASE_URL3 = "http://127.0.0.1:8000/services/"
AVAILABLE_TIME_URL = "http://127.0.0.1:8000/doctor/available_time/"


response = requests.get(AVAILABLE_TIME_URL)
response.raise_for_status()  # Check if the request was successful
available_times = response.json()

def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()
def fetch_doctors_data():
    try:
        response = requests.get(DOCTOR_LIST_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch doctors' data: {e}")
        return []



def show_login_page(root):
    clear_frame(root)

    login_frame = tk.Frame(root, bg="white", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(login_frame, text="Username", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    username_entry = tk.Entry(login_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1)
    username_entry.pack(pady=5)

    tk.Label(login_frame, text="Password", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    password_entry = tk.Entry(login_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1, show="*")
    password_entry.pack(pady=5)

    tk.Button(login_frame, text="Log in", font=("Arial", 14), bg="#4682B4", fg="white", padx=10, pady=5, relief="flat", 
              command=lambda: login_user(username_entry.get(), password_entry.get(), root)).pack(pady=10)

    create_account_label = tk.Label(login_frame, text="Create Account", font=("Arial", 10), fg="blue", bg="white", cursor="hand2")
    create_account_label.pack(pady=5)
    create_account_label.bind("<Button-1>", lambda e: show_register_page(root))

def show_register_page(root):
    clear_frame(root)

    register_frame = tk.Frame(root, bg="white", padx=20, pady=20)
    register_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(register_frame, text="Username", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    reg_username_entry = tk.Entry(register_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1)
    reg_username_entry.pack(pady=5)

    tk.Label(register_frame, text="First Name", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    reg_first_name_entry = tk.Entry(register_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1)
    reg_first_name_entry.pack(pady=5)

    tk.Label(register_frame, text="Last Name", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    reg_last_name_entry = tk.Entry(register_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1)
    reg_last_name_entry.pack(pady=5)

    tk.Label(register_frame, text="Email Address", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    reg_email_entry = tk.Entry(register_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1)
    reg_email_entry.pack(pady=5)

    tk.Label(register_frame, text="Password", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    reg_password_entry = tk.Entry(register_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1, show="*")
    reg_password_entry.pack(pady=5)

    tk.Label(register_frame, text="Confirm Password", font=("Arial", 12), bg="white").pack(anchor="w", pady=(5, 0))
    reg_confirm_password_entry = tk.Entry(register_frame, width=25, font=("Arial", 14), fg="gray", relief="solid", bd=1, show="*")
    reg_confirm_password_entry.pack(pady=5)

    tk.Button(register_frame, text="Register", font=("Arial", 14), bg="#4682B4", fg="white", padx=10, pady=5, relief="flat", 
              command=lambda: register_user(reg_username_entry, reg_first_name_entry, reg_last_name_entry, 
                                          reg_email_entry, reg_password_entry, reg_confirm_password_entry, root)).pack(pady=10)

    login_label = tk.Label(register_frame, text="Back to Login", font=("Arial", 10), fg="blue", bg="white", cursor="hand2")
    login_label.pack(pady=5)
    login_label.bind("<Button-1>", lambda e: show_login_page(root))

logged_in_user = None

def login_user(username, password, root):
    global logged_in_user 
    try:
        response = requests.post(BASE_URL + "login/", data={"username": username, "password": password})
      
        if response.status_code == 200:
            logged_in_user = response.json() 
            messagebox.showinfo("Login", "Login Successful!")
            show_main_page(root)
            
            
        else:
            messagebox.showerror("Login", "Invalid username or password!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")

def register_user(reg_username_entry, reg_first_name_entry, reg_last_name_entry, reg_email_entry, reg_password_entry, reg_confirm_password_entry, root):
    username = reg_username_entry.get()
    first_name = reg_first_name_entry.get()
    last_name = reg_last_name_entry.get()
    email = reg_email_entry.get()
    password = reg_password_entry.get()
    confirm_password = reg_confirm_password_entry.get()
    
    if not all([username, first_name, last_name, email, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    data = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "confirm_pssword": confirm_password
    }
    
    try:
        response = requests.post(BASE_URL + "register/", json=data)
        print("Request Data:", data)
        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())
        if response.status_code == 201:
            messagebox.showinfo("Success", "Registration successful!")
            show_login_page(root)
        else:
           # error_message = response.json().get("error", "Registration failed!")
            messagebox.showerror("Error", f"Registration failed: {response.json().get('error',response.text)}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")



def  appointment_page(content_frame):
    clear_frame(content_frame)

    tk.Label(content_frame, text="Appointment Status", font=("Arial", 30, "bold"), bg="white", fg="#4682B4").pack(pady=10)

    try:
        response = requests.get("http://127.0.0.1:8000/appointment/")
        if response.status_code == 200:
            appointment_data = response.json()

            # কার্ডের জন্য ফ্রেম
            cards_frame = tk.Frame(content_frame, bg="white")
            cards_frame.pack(pady=10, fill="both", expand=True)

            # কার্ড তৈরি
            for index, appointment in enumerate(appointment_data):
                card = tk.Frame(cards_frame, bg="#f0f8ff", relief="raised", bd=2, padx=15, pady=15)
                card.grid(row=index // 2, column=index % 2, padx=20, pady=20, sticky="nsew")

                # অ্যাপয়েন্টমেন্টের তথ্য
                tk.Label(card, text=f"ID: {appointment['id']}", font=("Arial", 12, "bold"), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(card, text=f"Type: {appointment['appointment_types']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(card, text=f"Status: {appointment['appointment_status']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(card, text=f"Symptom: {appointment['symptom']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(card, text=f"Doctor ID: {appointment['doctor']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(card, text=f"Time Slot: {appointment['time']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)

        else:
            tk.Label(content_frame, text="Failed to fetch appointment data.", font=("Arial", 12), bg="white", fg="red").pack(pady=10)
    except Exception as e:
        tk.Label(content_frame, text=f"Error connecting to server: {e}", font=("Arial", 12), bg="white", fg="red").pack(pady=10)

 


#-----------------------------------------------------------------------------------------main -----
def show_main_page(root):
    clear_frame(root)

    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(fill="both", expand=True)

    # Sidebar
    sidebar = tk.Frame(main_frame, bg="#4682B4", width=200)
    sidebar.pack(side="left", fill="y")

    tk.Button(sidebar, text="Home", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", 
              command=lambda: show_home_page(content_frame)).pack(fill="x", pady=5)
    tk.Button(sidebar, text="Blood Info", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", 
              command=lambda: show_blood_info_page(content_frame)).pack(fill="x", pady=5)
    
    # Test Book Button
    tk.Button(sidebar, text="Test Book", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", 
              command=lambda: show_test_book_page(content_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="Appointment", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", 
              command=lambda: appointment_page(content_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="Help Desk", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", 
              command=lambda: show_help_desk_page(content_frame)).pack(fill="x", pady=5)
    tk.Button(sidebar, text="About", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", 
              command=lambda: show_about_page(content_frame)).pack(fill="x", pady=5)

    # Content Frame
    content_frame = tk.Frame(main_frame, bg="white")
    content_frame.pack(side="left", fill="both", expand=True)

    show_home_page(content_frame)



#---------------------------------------------------------------------------------------------------#
# -------------------------------------------Home -------------------------------------------------

def show_home_page(content_frame):
    clear_frame(content_frame)

    global logged_in_user
    tk.Label(content_frame, text="Doctors' Information", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    doctors = fetch_doctors_data()  # Fetch doctors data from the API

    row_frame = tk.Frame(content_frame, bg="white")
    row_frame.pack(fill="both", expand=True, padx=20, pady=10)

    for i, doctor in enumerate(doctors):
        card = tk.Frame(row_frame, bg="#F0F0F0", relief="raised", bd=2, width=450, height=250)
        card.grid(row=i // 2, column=i % 2, padx=20, pady=20)
        card.pack_propagate(False)

        # Image Section
        img_frame = tk.Frame(card, bg="#F0F0F0", width=150)
        img_frame.pack(side="left", fill="y", padx=10, pady=10)

        try:
            img_url = doctor.get("image", None)
            if img_url:
                img = Image.open(requests.get(img_url, stream=True).raw)  # Open image directly from URL
                img = img.resize((120, 120), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(img_frame, image=photo, bg="#F0F0F0")
                img_label.image = photo
                img_label.pack(pady=10)
            else:
                tk.Label(img_frame, text="No Image", bg="#F0F0F0", font=("Arial", 10, "italic")).pack(pady=10)
        except Exception as e:
            tk.Label(img_frame, text="Image Load Failed", bg="#F0F0F0", font=("Arial", 10, "italic")).pack(pady=10)

        # Information Section
        info_frame = tk.Frame(card, bg="#F0F0F0")
        info_frame.pack(side="left", fill="both", expand=True, padx=10)

        name = doctor.get("name", "Unknown Doctor")
        tk.Label(info_frame, text=f"Dr. {name}", font=("Arial", 14, "bold"), bg="#F0F0F0").pack(anchor="w", pady=5)

        specialties = ', '.join([special if isinstance(special, str) else special.get('name', '') for special in doctor.get('specialization', [])])
        tk.Label(info_frame, text=f"Specialty: {specialties}", font=("Arial", 12), bg="#F0F0F0").pack(anchor="w")

        designations = ', '.join([designation if isinstance(designation, str) else designation.get('name', '') for designation in doctor.get('designation', [])])
        tk.Label(info_frame, text=f"Designation: {designations}", font=("Arial", 12), bg="#F0F0F0").pack(anchor="w")
        
        tk.Label(info_frame, text=f"Fee: ${doctor['fee']}", font=("Arial", 12), bg="#F0F0F0").pack(anchor="w")
        
        tk.Button(info_frame, text="View Profile", command=lambda d=doctor: show_doctor_profile(d, content_frame), bg="#4682B4", fg="white").pack(anchor="w", pady=10)

def show_doctor_profile(doctor, content_frame):
    clear_frame(content_frame)

    # Doctor Profile Header
    tk.Label(content_frame, text=f"Dr. {doctor['name']}'s Profile", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    # Doctor's Image and Information
    profile_frame = tk.Frame(content_frame, bg="white")
    profile_frame.pack(pady=20, fill="x")

    # Image Section
    img_url = doctor.get("image", None)
    if img_url:
        img = Image.open(requests.get(img_url, stream=True).raw)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(profile_frame, image=photo, bg="white")
        img_label.image = photo
        img_label.pack(side="left", padx=20)

    # Information Section
    info_frame = tk.Frame(profile_frame, bg="white")
    info_frame.pack(side="left", fill="both", expand=True)

    name = doctor.get("name", "Unknown Doctor")
    tk.Label(info_frame, text=f"Dr. {name}", font=("Arial", 14, "bold"), bg="#F0F0F0").pack(anchor="w", pady=5)

    # Specialization
    specialties = ', '.join([special if isinstance(special, str) else special.get('name', '') for special in doctor.get('specialization', [])])
    tk.Label(info_frame, text=f"Specialty: {specialties}", font=("Arial", 12), bg="#F0F0F0").pack(anchor="w")

    # Designation
    designations = ', '.join([designation if isinstance(designation, str) else designation.get('name', '') for designation in doctor.get('designation', [])])
    tk.Label(info_frame, text=f"Designation: {designations}", font=("Arial", 12), bg="#F0F0F0").pack(anchor="w")
        
    # Fee
    tk.Label(info_frame, text=f"Fee: ${doctor['fee']}", font=("Arial", 12), bg="#F0F0F0").pack(anchor="w")
        
    # Meet Link
    tk.Label(info_frame, text=f"Meet Link: {doctor['meet_link']}", font=("Arial", 12), bg="#F0F0F0").pack(anchor="w")

    # Reviews Section
    reviews_frame = tk.Frame(content_frame, bg="white")
    reviews_frame.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(reviews_frame, text="Doctor Reviews", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    # Fetch reviews for the specific doctor
    response = requests.get(DOCTOR_REVIEWS_URL)
    response.raise_for_status()
    all_reviews = response.json()
    filtered_reviews = [review for review in all_reviews if review['doctor'] == name]  # Filter by doctor ID
    print(filtered_reviews)
    if not filtered_reviews:
        tk.Label(reviews_frame, text="No reviews available.", font=("Arial", 14), bg="white").pack(pady=20)
        return

    # Display reviews
    for review in filtered_reviews:
        review_card = tk.Frame(reviews_frame, bg="#F0F0F0", relief="raised", bd=2, width=400, height=100)
        review_card.pack(side="left", padx=10, pady=10)
        review_card.pack_propagate(False)

        review_info = tk.Frame(review_card, bg="#F0F0F0")
        review_info.pack(fill="both", expand=True)

        # Display Patient's Name
        tk.Label(
            review_info,
            text=f"Patient: {review['reviewer']}",
            font=("Arial", 12, "bold"),
            bg="#F0F0F0"
        ).pack(anchor="w", pady=5)

        # Display Rating in Orange Color
        tk.Label(
            review_info,
            text=f"Rating: {review['rating']}",
            font=("Arial", 12, "bold"),
            fg="orange",
            bg="#F0F0F0"
        ).pack(anchor="w")

        # Display Review Body
        tk.Label(
            review_info,
            text=f"Comment: {review['body']}",
            font=("Arial", 12),
            bg="#F0F0F0"
        ).pack(anchor="w", pady=5)

    # Back Button to Return to Home Page (if needed)
    tk.Button(content_frame, text="Take Appointment", command=lambda: open_appointment_popup(doctor), bg="#4682B4", fg="white").pack(pady=20)

    #tk.Button(content_frame, text="Back to Home", command=show_home_page, bg="#4682B4", fg="white").pack(pady=20)


#-------------***************////////////////////////////////////////****\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def fetch_doctors_data():
    try:
        response = requests.get(DOCTOR_LIST_URL)
        response.raise_for_status()
        return response.json()  # Return the list of doctors from the API
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch doctors' data: {e}")
        return []

def get_time_id_by_name(time_name, available_times):
    """
    Find the time object with the given name and return its id.
    """
    time_object = next((time for time in available_times if time['name'] == time_name), None)
    if time_object:
        return time_object['id']
    else:
        return None
def open_appointment_popup(doc):
    popup = tk.Toplevel()
    popup.title("Take Appointment")
    popup.geometry("400x400")
    popup.grab_set()

    tk.Label(popup, text=f"Appointment for Dr. {doc['name']}", font=("Arial", 14, "bold")).pack(pady=10)

    # Appointment Type Selection
    tk.Label(popup, text="Select Appointment Type:", font=("Arial", 12)).pack(pady=5)
    appointment_type_var = tk.StringVar(value="Offline")
    appointment_type_options = ["Offline", "Online"]
    ttk.Combobox(popup, textvariable=appointment_type_var, values=appointment_type_options, state="readonly").pack(pady=5)

    # Symptom Entry
    tk.Label(popup, text="Symptom:", font=("Arial", 12)).pack(pady=5)
    symptom_entry = tk.Text(popup, height=4, width=30)
    symptom_entry.pack(pady=5)

    # Available Time Selection from fetched doctor data
    tk.Label(popup, text="Select Time:", font=("Arial", 12)).pack(pady=5)
    time_options = doc.get('available_time', [])
    time_var = tk.StringVar(value=time_options[0] if time_options else "No Time Available")
    ttk.Combobox(popup, textvariable=time_var, values=time_options, state="readonly").pack(pady=5)

    def confirm_appointment():
        # Appointment confirmation logic
        time_id = get_time_id_by_name(time_var.get(), available_times)
        if not time_id:
            messagebox.showerror("Error", "Invalid time selected!")
            return

        appointment_data = {
            "doctor": doc['id'],  # Use doctor ID instead of name
            "appointment_types": appointment_type_var.get(),
            "symptom": symptom_entry.get("1.0", "end-1c"),
            "time": time_id,  # Use time ID here
        }

        try:
            response = requests.post(APPOINTMENT_URL, json=appointment_data)
            if response.status_code == 201:
                messagebox.showinfo("Success", f"Appointment booked with Dr. {doc['name']} at {time_var.get()}")
                popup.destroy()
            else:
                messagebox.showerror("Error", f"Failed to book appointment: {response.json()}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to connect to server: {e}")

    tk.Button(popup, text="Confirm Appointment", command=confirm_appointment, bg="#4682B4", fg="white").pack(pady=20)


def show_help_desk_page(content_frame):
    clear_frame(content_frame)

    # পেজের ব্যাকগ্রাউন্ড
    content_frame.configure(bg="white")

    # পেজের শিরোনাম
    tk.Label(content_frame, text="Help Desk", font=("Arial", 20, "bold"), bg="white", fg="#4682B4").place(relx=0.5, rely=0.1, anchor="center")

    # নাম ইনপুট
    tk.Label(content_frame, text="Name:", font=("Arial", 12, "bold"), bg="white").place(relx=0.3, rely=0.2, anchor="e")
    name_entry = tk.Entry(content_frame, width=40, font=("Arial", 12), relief="solid", bd=1)
    name_entry.place(relx=0.35, rely=0.2, anchor="w")

    # সমস্যার বিবরণ
    tk.Label(content_frame, text="Problem Description:", font=("Arial", 12, "bold"), bg="white").place(relx=0.3, rely=0.3, anchor="e")
    problem_entry = tk.Text(content_frame, width=50, height=5, font=("Arial", 12), relief="solid", bd=1, wrap="word")
    problem_entry.place(relx=0.35, rely=0.3, anchor="nw")

    # ছবি আপলোড
    tk.Label(content_frame, text="Upload Image:", font=("Arial", 12, "bold"), bg="white").place(relx=0.3, rely=0.5, anchor="e")
    image_path = tk.StringVar()

    def browse_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        image_path.set(file_path)
        if file_path:
            tk.Label(content_frame, text="File Selected: " + file_path.split("/")[-1], font=("Arial", 10), bg="white", fg="green").place(relx=0.35, rely=0.55, anchor="w")

    browse_button = tk.Button(content_frame, text="Browse", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", command=browse_image)
    browse_button.place(relx=0.35, rely=0.5, anchor="w")

    # সাবমিট বাটন
    submit_button = tk.Button(content_frame, text="Submit", font=("Arial", 14, "bold"), bg="#4682B4", fg="white", relief="flat", 
                              command=lambda: submit_help_request(name_entry.get(), problem_entry.get("1.0", "end-1c"), image_path.get(), content_frame))
    submit_button.place(relx=0.5, rely=0.7, anchor="center")

    # নোট বা নির্দেশনা
    tk.Label(content_frame, text="* All fields are required", font=("Arial", 10, "italic"), bg="white", fg="red").place(relx=0.5, rely=0.8, anchor="center")



def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()

def show_blood_info_page(content_frame):
    clear_frame(content_frame)

    tk.Label(content_frame, text="Blood Bank", font=("Arial", 30, "bold"), bg="white", fg="#4682B4").pack(pady=10)

    try:
        response = requests.get(BASE_URL3 + "blood/")
        if response.status_code == 200:
            blood_data = response.json()
            
            # কার্ডের জন্য ফ্রেম
            cards_frame = tk.Frame(content_frame, bg="white")
            cards_frame.pack(pady=10, fill="both", expand=True)

            # কার্ড তৈরি
            for index, donor in enumerate(blood_data):
                card = tk.Frame(cards_frame, bg="#f0f8ff", relief="raised", bd=2, padx=15, pady=15)
                card.grid(row=index // 2, column=index % 2, padx=20, pady=20, sticky="nsew")

                # ডোনারের তথ্য
                info_frame = tk.Frame(card, bg="#f0f8ff")
                info_frame.pack(side="left", fill="both", expand=True)

                tk.Label(info_frame, text=f"Name: {donor['name']}", font=("Arial", 12, "bold"), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(info_frame, text=f"Email: {donor['email']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(info_frame, text=f"Phone: {donor['phone']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(info_frame, text=f"Blood Group: {donor['bloodgroup']}", font=("Arial", 12, "bold"), fg="red", bg="#f0f8ff").pack(anchor="w", pady=2)

                # ইমেজ ফ্রেম
                image_frame = tk.Frame(card, bg="#f0f8ff")
                image_frame.pack(side="right", padx=10)

                try:
                    img_data = requests.get(donor['image']).content
                    img = Image.open(io.BytesIO(img_data))
                    img.thumbnail((100, 100))
                    photo = ImageTk.PhotoImage(img)
                    img_label = tk.Label(image_frame, image=photo, bg="#f0f8ff")
                    img_label.image = photo  # গারবেজ কালেকশন এড়ানোর জন্য রেফারেন্স রাখা
                    img_label.pack()
                except Exception as e:
                    tk.Label(image_frame, text="[Image not available]", font=("Arial", 10), bg="#f0f8ff", fg="gray").pack()
        else:
            tk.Label(content_frame, text="Failed to fetch blood information.", font=("Arial", 12), bg="white", fg="red").pack(pady=10)
    except Exception as e:
        tk.Label(content_frame, text="Error connecting to server.", font=("Arial", 12), bg="white", fg="red").pack(pady=10)



def submit_help_request(name, description, image_path, popup):
    if not name or not description:
        messagebox.showerror("Error", "Name and description are required!")
        return

    data = {"name": name, "description": description}
    files = {"image": open(image_path, "rb")} if image_path else None

    try:
        response = requests.post(BASE_URL3 + "help/", data=data, files=files)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Help request submitted successfully!")
            popup.destroy()
        else:
            messagebox.showerror("Error", "Failed to submit help request.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")
def show_message(title, message):
    messagebox.showinfo(title, message)

def show_about_page(content_frame):
    clear_frame(content_frame)

    BG_COLOR = "#f9fafc"
    HEADER_COLOR = "#0078D7"
    BOX_COLOR = "#E1ECF7"
    TEXT_COLOR = "#333333"
    FONT_TITLE = ("Arial", 16, "bold")
    FONT_BOX = ("Arial", 12, "bold")
    FONT_FOOTER = ("Arial", 10)

    # Create content section
    content_frame = tk.Frame(content_frame, bg=BG_COLOR)
    content_frame.pack(pady=(30, 0))

    # About Us Title
    title_label = tk.Label(content_frame, text="About Us", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_TITLE, pady=10)
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Mission, Vision, and other buttons
    mission_button = tk.Button(content_frame, text="Mission", bg=BOX_COLOR, fg=TEXT_COLOR, font=FONT_BOX, width=20, height=1,
                               command=lambda: show_message( "Mission",
            "Our mission is to deliver exceptional healthcare services with compassion, innovation, and integrity. "
            "We are committed to promoting the well-being of our patients by providing comprehensive and personalized care. "
            "Through a patient-first approach, we strive to meet the diverse medical needs of individuals and families, "
            "ensuring their health and happiness are at the core of everything we do."))
    mission_button.grid(row=1, column=0, padx=20, pady=10)

    vision_button = tk.Button(content_frame, text="Vision", bg=BOX_COLOR, fg=TEXT_COLOR, font=FONT_BOX, width=20, height=1,
                              command=lambda: show_message( "Vision",
            "Our vision is to be a leading healthcare institution recognized for excellence, innovation, and a deep commitment to the communities we serve. "
            "We aim to set new benchmarks in patient care by embracing cutting-edge medical advancements and fostering a culture of continuous improvement. "
            "Our ultimate goal is to create a healthier world where everyone has access to quality medical care and support."))
    vision_button.grid(row=2, column=0, padx=20, pady=10)

    specialists_button = tk.Button(content_frame, text="Specialists", bg=BOX_COLOR, fg=TEXT_COLOR, font=FONT_BOX, width=20, height=1,
                                   command=lambda: show_message( "Specialists",
            "Our hospital is proud to have a team of highly qualified and experienced specialists across various fields, "
            "including cardiology, oncology, orthopedics, pediatrics, neurology, and more. "
            "These experts bring advanced knowledge, skill, and dedication to their respective areas, ensuring our patients receive the best possible treatment. "
            "Equipped with state-of-the-art technology and a commitment to excellence, our specialists"
              "work collaboratively to deliver accurate diagnoses and effective therapies tailored to each patient’s needs."))
    specialists_button.grid(row=3, column=0, padx=20, pady=10)

    serving_button = tk.Button(content_frame, text="Serving Patients", bg=BOX_COLOR, fg=TEXT_COLOR, font=FONT_BOX, width=20, height=1,
                               command=lambda: show_message("Serving Patients",
            "At the heart of our services is a commitment to providing compassionate, patient-centered care. "
            "We understand that every patient is unique, and we prioritize creating a comfortable and supportive environment where they feel heard and valued. "
            "From preventive care to complex treatments, we go above and beyond to ensure optimal outcomes and foster trust. "
            "Our dedicated staff works tirelessly to make every patient’s healthcare journey smooth, efficient, and empowering."))

def show_profile_page(content_frame):
    clear_frame(content_frame)

    global logged_in_user
    tk.Label(content_frame, text="Profile Page", font=("Arial", 16), bg="white").pack(pady=10)

    if logged_in_user:
        tk.Label(content_frame, text=f"User Id: {logged_in_user['user_id']}", font=("Arial", 12), bg="white").pack(pady=5)
        tk.Label(content_frame, text=f"Username: {logged_in_user['username']}", font=("Arial", 12), bg="white").pack(pady=5)
        
        
#------------------------- ‍show test book -------------------------------------------
def show_test_book_page(content_frame):
    clear_frame(content_frame)

    tk.Label(content_frame, text="Test Book", font=("Arial", 30, "bold"), bg="white", fg="#4682B4").pack(pady=10)

    try:
        response = requests.get(BASE_URL3 + "test/")
        if response.status_code == 200:
            test_data = response.json()

            # Create a frame for the cards
            cards_frame = tk.Frame(content_frame, bg="white")
            cards_frame.pack(pady=10, fill="both", expand=True)

            # Create cards for each test
            for index, test in enumerate(test_data):
                card = tk.Frame(cards_frame, bg="#f0f8ff", relief="raised", bd=2, padx=15, pady=15)
                card.grid(row=index // 2, column=index % 2, padx=20, pady=20, sticky="nsew")

                # Display test information
                tk.Label(card, text=f"Test: {test['name']}", font=("Arial", 12, "bold"), bg="#f0f8ff").pack(anchor="w", pady=2)
                tk.Label(card, text=f"Cost: {test['cost']}", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w", pady=2)

                # Display test image (if available)
                try:
                    img_data = requests.get(test['image']).content
                    img = Image.open(io.BytesIO(img_data))
                    img.thumbnail((100, 100))
                    photo = ImageTk.PhotoImage(img)
                    img_label = tk.Label(card, image=photo, bg="#f0f8ff")
                    img_label.image = photo  # Keep reference to avoid garbage collection
                    img_label.pack()
                except Exception as e:
                    tk.Label(card, text="[Image not available]", font=("Arial", 10), bg="#f0f8ff", fg="gray").pack()

                # Book Now Button
                book_button = tk.Button(card, text="Book Now", font=("Arial", 12), bg="#4682B4", fg="white", relief="flat", 
                                        command=lambda test_id=test['id']: open_book_popup(test_id, content_frame))
                book_button.pack(pady=5)
        else:
            tk.Label(content_frame, text="Failed to fetch test data.", font=("Arial", 12), bg="white", fg="red").pack(pady=10)
    except Exception as e:
        tk.Label(content_frame, text=f"Error connecting to server: {e}", font=("Arial", 12), bg="white", fg="red").pack(pady=10)
        
def open_book_popup(test_id, content_frame):
    # Create a new window (pop-up)
    popup = tk.Toplevel(content_frame)
    popup.title("Book Test")
    popup.geometry("400x300")

    tk.Label(popup, text="Name:", font=("Arial", 12)).pack(pady=5)
    name_entry = tk.Entry(popup, font=("Arial", 12))
    name_entry.pack(pady=5)

    tk.Label(popup, text="Phone:", font=("Arial", 12)).pack(pady=5)
    phone_entry = tk.Entry(popup, font=("Arial", 12))
    phone_entry.pack(pady=5)

    tk.Label(popup, text="Email:", font=("Arial", 12)).pack(pady=5)
    email_entry = tk.Entry(popup, font=("Arial", 12))
    email_entry.pack(pady=5)

    # Submit Button
    def submit_booking():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields are required!")
            return

        data = {
            "test": test_id,
            "name": name,
            "phone": phone,
            "email": email,
        }
        print(data)
        try:
            response = requests.post("http://127.0.0.1:8000/services/testbook/", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Test booked successfully!")
                popup.destroy()
            else:
                print(f"Response Status: {response.status_code}")
                print(f"Response Text: {response.text}")
                messagebox.showerror("Error", f"Failed to book the test: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to server: {e}")

    tk.Button(popup, text="Submit", font=("Arial", 14), bg="#4682B4", fg="white", relief="flat", command=submit_booking).pack(pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("900x600")
    root.configure(bg="#87CEEB")
    show_login_page(root)
    
    root.mainloop()
