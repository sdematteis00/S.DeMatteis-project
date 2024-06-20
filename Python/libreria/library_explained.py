from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter.messagebox

        
class LibraryManagementSystem:
    #This class represents the main window of the library management system application.

    def __init__(self, root):
        self.root = root

        # Set window title and geometry
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
    
        # Set colors
        root_bg_color = "#ecf0f1"
        self.root.config(bg=root_bg_color)
        text_color = "#2c3e50"
        
        # ======================================== variables ==========================================
        
        # Declare StringVar variables to store the values of various fields in the system,
        # such as member type, PRN number, ID, first name, last name, address, mobile number, book ID, book title, etc.
        self.membertype_var = StringVar()  # Member type variable
        self.prnno_var = StringVar()  # PRN number variable
        self.id_var = StringVar()  # ID variable
        self.firstname_var = StringVar()  # First name variable
        self.lastname_var = StringVar()  # Last name variable
        self.adress1_var = StringVar()  # Address 1 variable
        self.adress2_var = StringVar()  # Address 2 variable
        self.postcode_var = StringVar()  # Postcode variable
        self.mobile_var = StringVar()  # Mobile number variable
        self.bookid_var = StringVar()  # Book ID variable
        self.booktitle_var = StringVar()  # Book title variable
        self.author_var = StringVar()  # Author variable
        self.borrowdate_var = StringVar()  # Borrow date variable
        self.duedate_var = StringVar()  # Due date variable
        self.loanperiod_var = StringVar()  # Loan period variable
        self.latereturnfine_var = StringVar()  # Late return fine variable
        self.overduedate_var = StringVar()  # Overdue date variable
        self.actualprice_var = StringVar()  # Actual price variable
        
        # ======================================== Title =================================================
        # Create a label for the application title
        lbltitle = Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            bg=root_bg_color,
            fg=text_color,
            bd=20,
            relief=RIDGE,
            font=("times new roman", 30, "bold"),
            padx=2,
            pady=6,
        )
        lbltitle.pack(side=TOP, fill=X)  # Pack the label at the top, expanding horizontally

        # Create a frame to hold other widgets
        frame = Frame(
            self.root,
            bd=12,
            relief=RIDGE,
            padx=20,
            bg=root_bg_color
        )
        frame.place(x=0, y=130, width=1530, height=400)  # Place the frame

        
        # ======================================== Data Frame Left ==========================================
        
        DataFrameLeft = LabelFrame(
            frame,
            text="LIBRARY MEMBER INFO",
            bg="#2c3e50",
            fg="#ffffff",
            bd=12,
            padx=20,
            relief=RIDGE,
            font=("times new roman", 17, "bold")
        )
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        lblMember= Label(
            DataFrameLeft, 
            text="Member Type:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblMember.grid(row=0, column=0, sticky=W)
        
        comboMember = ttk.Combobox(
            DataFrameLeft, 
            font=("arial", 12, "bold"), 
            textvariable=self.membertype_var,
            width = 27, 
            state = "readonly")
        comboMember["value"] = ("Admin", "Student", "Lecturer")
        comboMember.grid(row=0, column=1)
        
        lblPRN_No= Label(
            DataFrameLeft, 
            text="PRN No:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2
            )
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.prnno_var, width = 29)
        txtPRN_No.grid(row=1, column=1)
        
        lblid= Label(
            DataFrameLeft, 
            text="ID No:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"),    
            padx=2, 
            pady=4
            )
        lblid.grid(row=2, column=0, sticky=W)
        txtid = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.id_var, width = 29)
        txtid.grid(row=2, column=1)
        
        lblFirstName = Label(
            DataFrameLeft, 
            text="First Name:",
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width = 29)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName = Label(
            DataFrameLeft, 
            text="Last Name:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var, width = 29)
        txtLastName.grid(row=4, column=1)
        
        lblAddress1 = Label(
            DataFrameLeft, 
            text="Adress1:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"),
            padx=2, 
            pady=6
            )
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAdress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.adress1_var,  width = 29)
        txtAdress1.grid(row=5, column=1)
        
        lblAddress2 = Label(
            DataFrameLeft, 
            text="Adress2:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAdress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.adress2_var, width = 29)
        txtAdress2.grid(row=6, column=1)
        
        lblPostCode = Label(
            DataFrameLeft, 
            text="Post Code:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.postcode_var, width = 29)
        txtPostCode.grid(row=7, column=1)
        
        lblMobile = Label(
            DataFrameLeft, 
            text="Mobile:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width = 29)
        txtMobile.grid(row=8, column=1)
        
        lblBookID = Label(
            DataFrameLeft, 
            text="Book ID:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.bookid_var, width = 29)
        txtBookID.grid(row=0, column=3)
        
        lblBookTitle = Label(
            DataFrameLeft, 
            text="Book Title:",
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.booktitle_var, width = 29)
        txtBookTitle.grid(row=1, column=3)
        
        lblAuthor = Label(
            DataFrameLeft, 
            text="Author:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.author_var, width = 29)
        txtAuthor.grid(row=2, column=3)
        
        lblBorrowDate = Label(
            DataFrameLeft, 
            text="Borrow Date:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblBorrowDate.grid(row=3, column=2, sticky=W)
        txtBorrowDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.borrowdate_var, width = 29)
        txtBorrowDate.grid(row=3, column=3)
        
        lblDueDate = Label(
            DataFrameLeft, 
            text="Due Date:", 
            bg= "#2c3e50", fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblDueDate.grid(row=4, column=2, sticky=W)
        txtDueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.duedate_var, width = 29)
        txtDueDate.grid(row=4, column=3)
    
        lblLoanPeriod = Label(
            DataFrameLeft, 
            text="Loan Period:", 
            bg= "#2c3e50", fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblLoanPeriod.grid(row=5, column=2, sticky=W)
        txtLoanPeriod = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.loanperiod_var, width = 29)
        txtLoanPeriod.grid(row=5, column=3)
        
        lblLateReturnFine = Label(
            DataFrameLeft, 
            text="Late Return Fine:", 
            bg= "#2c3e50", fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLaternReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.latereturnfine_var, width = 29)
        txtLaternReturnFine.grid(row=6, column=3)
        
        lblOverdueDate = Label(
            DataFrameLeft, 
            text="Overdue Date:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblOverdueDate.grid(row=7, column=2, sticky=W)
        txtOverdueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.overduedate_var, width = 29)
        txtOverdueDate.grid(row=7, column=3)
        
        lblActualPrice = Label(
            DataFrameLeft, 
            text="Actual Price:", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            font=("arial", 12, "bold"), 
            padx=2, 
            pady=6
            )
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.actualprice_var, width = 29)
        txtActualPrice.grid(row=8, column=3)
        
        
        # ======================================== Data Frame Right  ==========================================
        
        DataFrameRight = LabelFrame(
            frame, 
            text="BOOK INFO", 
            bg= "#2c3e50", 
            fg="#ffffff", 
            bd=12, 
            padx=20, 
            relief=RIDGE, 
            font=("times new roman", 17, "bold"))
        DataFrameRight.place(x= 910, y=5, width = 540, height = 350)
        
        self.txtBox = Text(DataFrameRight,  font=("arial", 12, "bold"), width = 32, height = 16, padx = 2, pady = 6)
        self.txtBox.grid(row=0, column=2)
        
        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        booklist = ["Dune", "The Left Hand of Darkness", "The Chronicles of Narnia", 
                   "The Name of the Wind", "A Song of Ice and Fire", "And Then There Were None", 
                   "Murder on the Orient Express", "The Perfect Murder", "The Name of the Rose", "The Pillars of the Earth", 
                   "The Hobbit", "The Return of the King", "1984", "Pride and Prejudice", "Moby Dick", "The Great Gatsby", "The Hunger Games"
                   ]
        booklist.sort()
        def SelectBook(event=""):
            """
            Selects a book from the listbox and sets the corresponding book information in the text boxes.

            Args:
                event (str): The event that triggered the function.

            Returns:
                None
            """
            # Get the selected book from the listbox
            value = str(listBox.get(listBox.curselection()))

            # Dictionary of book data
            book_data = {
                "The Return of the King": ("BKID001", "The Return of the King", "J. R. R. Tolkien", "EUR 4", 15),
                "Dune": ("BKID002", "Dune", "Frank Herbert", "EUR 5", 15),
                "The Left Hand of Darkness": ("BKID003", "The Left Hand of Darkness", "Ursula K. Le Guin", "EUR 3", 15),
                "The Chronicles of Narnia": ("BKID004", "The Chronicles of Narnia", "C. S. Lewis", "EUR 4", 15),
                "The Name of the Wind": ("BKID005", "The Name of the Wind", "Patrick Rothfuss", "EUR 8", 15),
                "A Song of Ice and Fire": ("BKID006", "A Song of Ice and Fire", "George R. R. Martin", "EUR 10", 15),
                "And Then There Were None": ("BKID007", "And Then There Were None", "Agatha Christie", "EUR 6", 15),
                "Murder on the Orient Express": ("BKID008", "Murder on the Orient Express", "Agatha Christie", "EUR 4", 15),
                "The Perfect Murder": ("BKID009", "The Perfect Murder", "Agatha Christie", "EUR 3", 15),
                "The Name of the Rose": ("BKID010", "The Name of the Rose", "Umberto Eco", "EUR 4", 15),
                "The Pillars of the Earth": ("BKID011", "The Pillars of the Earth", "Ken Follett", "EUR 6", 15),
                "The Hobbit": ("BKID012", "The Hobbit", "J.R.R. Tolkien", "EUR 8", 15),
                "Pride and Prejudice": ("BKID013", "Pride and Prejudice", "Jane Austen", "EUR 6", 15),
                "MobyDick": ("BKID014", "Moby Dick", "Herman Melville", "EUR 6", 15),
                "1984": ("BKID015", "1984", "George Orwell", "EUR 5", 15),
                "The Great Gatsby": ("BKID016", "The Great Gatsby", "F. Scott Fitzgerald", "EUR 6", 15),
                "The Hunger Games": ("BKID017", "The Hunger Games", "Suzanne Collins", "EUR 6", 15)
            }

            # Check if the selected book exists in the dictionary
            if value in book_data:
                # Set the book information in the text boxes
                bookid, booktitle, author, actualprice, loanperiod = book_data[value]
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.bookid_var.set(bookid)
                self.booktitle_var.set(booktitle)
                self.author_var.set(author)
                self.actualprice_var.set(actualprice)
                self.borrowdate_var.set(d1)
                self.duedate_var.set(d3)
                self.loanperiod_var.set(loanperiod)
                self.latereturnfine_var.set("EUR {}".format(loanperiod - 1))
                self.overduedate_var.set("None")
            else:
                print("Book not found")
            

        
        listBox = Listbox(
            DataFrameRight, 
            font=("arial", 12, "bold"),
            width = 20, 
            height = 16)
        listBox.bind('<<ListboxSelect>>', SelectBook)
        listBox.grid(row=0, column=0, padx = 4, rowspan=20)
        listScrollbar.config(command=listBox.yview)
        
        for item in booklist:
            listBox.insert(END, item)
        
        # ======================================== Buttons Frame ==========================================
        
        FrameButton = Frame(
            self.root, 
            bd = 12, 
            relief=RIDGE, 
            padx = 20, 
            bg=root_bg_color
            )
        FrameButton.place(x=0, y=530, width = 1530, height = 70)
        
        btnAddData = Button(
            FrameButton, 
            command=self.add_data,
            text="Add Data", 
            font=("arial", 12, "bold"), 
            width = 23,  
            bg = "#3498db", 
            fg = "#ffffff")
        btnAddData.grid(row=0, column=0)
        
        btnAddData= Button(
            FrameButton, 
            command=self.showData,
            text="Show Data", 
            font=("arial", 12, "bold"), 
            width = 23,  
            bg = "#3498db", 
            fg = "#ffffff")
        btnAddData.grid(row=0, column=1)
        
        btnUpdate = Button(
            FrameButton, 
            text="Update",
            command= self.update_data, 
            font=("arial", 12, "bold"), 
            width = 23,  
            bg = "#3498db", 
            fg = "#ffffff")
        btnUpdate.grid(row=0, column=2)
        
        btnDelete = Button(
            FrameButton, 
            text="Delete",
            command=self.delete, 
            font=("arial", 12, "bold"), 
            width = 23,  
            bg = "#3498db", 
            fg = "#ffffff")
        btnDelete.grid(row=0, column=3)
        
        btnResest = Button(
            FrameButton, 
            text="Reset",
            command=self.reset, 
            font=("arial", 12, "bold"), 
            width = 23,  
            bg = "#3498db", 
            fg = "#ffffff")
        btnResest.grid(row=0, column=4)
        
        btnExit = Button(
            FrameButton, 
            text="Exit", 
            command=self.iExit,
            font=("arial", 12, "bold"), 
            width = 23,  
            bg = "#3498db", 
            fg = "#ffffff")
        btnExit.grid(row=0, column=5)
        
        # ======================================== Information Frame ==========================================
        
        # Frame that contains the table with the library details
        FrameDetails = Frame(self.root, bd = 12, relief=RIDGE, padx = 20, bg=root_bg_color)
        FrameDetails.place(x=0, y=590, width = 1530, height = 210)
        
        # Frame that contains the table
        TableFrame = Frame(FrameDetails, bd = 6, relief=RIDGE, bg="#2c3e50")
        TableFrame.place(x=0, y=2, width = 1460, height = 190)
        
        # Horizontal scrollbar for the table
        xscrollbar = Scrollbar(TableFrame, orient=HORIZONTAL)
        # Vertical scrollbar for the table
        yscrollbar = Scrollbar(TableFrame, orient=VERTICAL)
        
        # Treeview widget that displays the library details
        self.libraryTable = ttk.Treeview(TableFrame, columns=("membertype", "prnno", "title", "firstname", 
                                                              "lastname", "address1", "address2", "postcode", 
                                                              "mobile", "bookid", "booktitle", "author", 
                                                              "borrowdate", "duedate", "loanperiod", "latereturnfine",
                                                              "overduedate", "actualprice"), xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        
        # Pack the scrollbars
        xscrollbar.pack(side= BOTTOM, fill=X)
        yscrollbar.pack(side= RIGHT, fill=Y)
        
        # Configure the scrollbars to scroll the table
        xscrollbar.config(command=self.libraryTable.xview)
        yscrollbar.config(command=self.libraryTable.yview)
        
        # Set the headers for each column
        self.libraryTable.heading("membertype", text="Member Type")
        self.libraryTable.heading("prnno", text="PRN No")
        self.libraryTable.heading("title", text="Title")
        self.libraryTable.heading("firstname", text="First Name")
        self.libraryTable.heading("lastname", text="Last Name")
        self.libraryTable.heading("address1", text="Address 1")
        self.libraryTable.heading("address2", text="Address 2")
        self.libraryTable.heading("postcode", text="Post Code")
        self.libraryTable.heading("mobile", text="Mobile")
        self.libraryTable.heading("bookid", text="Book ID")
        self.libraryTable.heading("booktitle", text="Book Title")
        self.libraryTable.heading("author", text="Author")
        self.libraryTable.heading("borrowdate", text="Borrow Date")
        self.libraryTable.heading("duedate", text="Due Date")
        self.libraryTable.heading("loanperiod", text="Loan Period")
        self.libraryTable.heading("latereturnfine", text="Late Return Fine")
        self.libraryTable.heading("overduedate", text="Over Due Date")
        self.libraryTable.heading("actualprice", text="Actual Price")
        
        # Show the headers
        self.libraryTable["show"] = "headings"
        
        # Pack the table and make it fill the frame
        self.libraryTable.pack(fill=BOTH, expand=1)
        
        # Set the width of each column
        for column in self.libraryTable['columns']:
            self.libraryTable.column(column, width=100)
    
        # Fetch the data from the database and display it in the table
        self.fatch_data()
        
        # Bind the event to get the cursor position when the user releases the mouse button
        self.libraryTable.bind('<ButtonRelease-1>', self.get_cursor)
    
    def add_data(self):  
        """
        Adds a new member to the library database.
        """
        
        # Prepare the SQL statement with placeholders
        sql = """
        INSERT INTO library (membertype, prnno, id, firstname, lastname, address1, address2, postcode, mobile, bookid, booktitle, author, borrowdate, duedate, loanperiod, latereturnfine, overduedate, actualprice)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Prepare the data to insert
        data = (self.membertype_var.get(),
                self.prnno_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.adress1_var.get(),
                self.adress2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.borrowdate_var.get(),
                self.duedate_var.get(),
                self.loanperiod_var.get(),
                self.latereturnfine_var.get(),
                self.overduedate_var.get(),
                self.actualprice_var.get())
        
        # Connect to the database and execute the query
        # The context manager automatically handles closing the connection
        with mysql.connector.connect(host="localhost", user="root", password="root", database="mydata") as conn:
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            
        # Refresh the table
        self.fatch_data()
        
        # Show a success message
        messagebox.showinfo("Success", "Member has been inserted")
        
    def update_data(self):
        """
        Updates the member's data in the library database.

        This function retrieves the member's data from the form fields, constructs an update query
        using the prepared statement syntax, and executes the query on the database.
        After successful update, the table is refreshed and a success message is shown.

        Raises:
            Exception: If the update query fails to execute.
        """
        prnno = self.prnno_var.get()
        if not prnno:
            # PRN No is required for updating the data
            messagebox.showerror("Error", "PRN No is required to update the data")
            return

        # Prepare the data to update
        data = {
            "membertype": self.membertype_var.get(),
            "id": self.id_var.get(),
            "firstname": self.firstname_var.get(),
            "lastname": self.lastname_var.get(),
            "address1": self.adress1_var.get(),
            "address2": self.adress2_var.get(),
            "postcode": self.postcode_var.get(),
            "mobile": self.mobile_var.get(),
            "bookid": self.bookid_var.get(),
            "booktitle": self.booktitle_var.get(),
            "author": self.author_var.get(),
            "borrowdate": self.borrowdate_var.get(),
            "duedate": self.duedate_var.get(),
            "loanperiod": self.loanperiod_var.get(),
            "latereturnfine": self.latereturnfine_var.get(),
            "overduedate": self.overduedate_var.get(),
            "actualprice": self.actualprice_var.get()
        }

        # Connect to the database and execute the query
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        try:
            # Construct the update query using the prepared statement syntax
            update_query = ", ".join(f"{key} = %({key})s" for key in data)
            my_cursor.execute(f"UPDATE library SET {update_query} WHERE prnno = %(prnno)s", {**data, "prnno": prnno})
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "Member has been updated")
        except Exception as e:
            # Show an error message if the update query fails to execute
            messagebox.showerror("Error", f"Failed to update the member: {str(e)}")
            conn.rollback()
        
    def fatch_data(self):
        """
        Fetches all data from the 'library' table and updates the libraryTable with the fetched data.
        """
        # Define the SQL query to fetch all data from the 'library' table.
        query = "SELECT * FROM library"

        # Establish a connection to the database and create a cursor object.
        with mysql.connector.connect(host="localhost", user="root", password="root", database="mydata") as conn:
            my_cursor = conn.cursor()

            # Execute the SQL query.
            my_cursor.execute(query)

            # Fetch all rows returned by the query.
            rows = my_cursor.fetchall()

            # Clear the libraryTable before inserting the fetched data.
            self.libraryTable.delete(*self.libraryTable.get_children())

            # Insert the fetched data into the libraryTable.
            for row in rows:
                self.libraryTable.insert("", END, values=row)
        
    def get_cursor(self, event=""):
        """
        Fetches the data at the currently selected row in the libraryTable and sets the corresponding variables.
        
        Args:
            event (str): The event that triggered the function call. Default is an empty string.
        """
        # Get the row index of the currently selected row in the libraryTable.
        cursor_row = self.libraryTable.focus()
        
        # Get the values of the selected row.
        values = self.libraryTable.item(cursor_row)["values"]
        
        # Set the variables with the corresponding values.
        self.membertype_var.set(values[0])  # Set the membertype_var with the value at index 0.
        self.prnno_var.set(values[1])  # Set the prnno_var with the value at index 1.
        self.id_var.set(values[2])  # Set the id_var with the value at index 2.
        self.firstname_var.set(values[3])  # Set the firstname_var with the value at index 3.
        self.lastname_var.set(values[4])  # Set the lastname_var with the value at index 4.
        self.adress1_var.set(values[5])  # Set the adress1_var with the value at index 5.
        self.adress2_var.set(values[6])  # Set the adress2_var with the value at index 6.
        self.postcode_var.set(values[7])  # Set the postcode_var with the value at index 7.
        self.mobile_var.set(values[8])  # Set the mobile_var with the value at index 8.
        self.bookid_var.set(values[9])  # Set the bookid_var with the value at index 9.
        self.booktitle_var.set(values[10])  # Set the booktitle_var with the value at index 10.
        self.author_var.set(values[11])  # Set the author_var with the value at index 11.
        self.borrowdate_var.set(values[12])  # Set the borrowdate_var with the value at index 12.
        self.duedate_var.set(values[13])  # Set the duedate_var with the value at index 13.
        self.loanperiod_var.set(values[14])  # Set the loanperiod_var with the value at index 14.
        self.latereturnfine_var.set(values[15])  # Set the latereturnfine_var with the value at index 15.
        self.overduedate_var.set(values[16])  # Set the overduedate_var with the value at index 16.
        self.actualprice_var.set(values[17])  # Set the actualprice_var with the value at index 17.
    
    def showData(self):
        """
        Displays the data in the Text widget.
        
        This function iterates over a list of tuples containing the label and the corresponding variable.
        It inserts the label and the value of the variable into the Text widget.
        """
        
        # List of tuples containing the label and the corresponding variable.
        data = (
            ("Member Type:", self.membertype_var),
            ("PRN No:", self.prnno_var),
            ("ID:", self.id_var),
            ("First Name:", self.firstname_var),
            ("Last Name:", self.lastname_var),
            ("Address 1:", self.adress1_var),
            ("Address 2:", self.adress2_var),
            ("Postcode:", self.postcode_var),
            ("Mobile:", self.mobile_var),
            ("Book ID:", self.bookid_var),
            ("Book Title:", self.booktitle_var),
            ("Author:", self.author_var),
            ("Borrow Date:", self.borrowdate_var),
            ("Due Date:", self.duedate_var),
            ("Loan Period:", self.loanperiod_var),
            ("Late Return Fine:", self.latereturnfine_var),
            ("Over Due Date:", self.overduedate_var),
            ("Actual Price:", self.actualprice_var)
        )
        for label, var in data:
            self.txtBox.insert(END, f"{label}\t\t{var.get()}\n")
        
    def reset(self):
        """
        Resets all the variables and clears the text box.
        """
        # Loop through all the variables and set their values to an empty string.
        for var in (
            self.membertype_var,
            self.prnno_var,
            self.id_var,
            self.firstname_var,
            self.lastname_var,
            self.adress1_var,
            self.adress2_var,
            self.postcode_var,
            self.mobile_var,
            self.bookid_var,
            self.booktitle_var,
            self.author_var,
            self.borrowdate_var,
            self.duedate_var,
            self.loanperiod_var,
            self.latereturnfine_var,
            self.overduedate_var,
            self.actualprice_var,
        ):
            var.set("")  # Set the value of the variable to an empty string.
        
        # Clear the text box.
        self.txtBox.delete("1.0", END)
        
    def iExit(self):
        """
        Displays a message box asking the user if they want to exit the application.
        If the user clicks "Yes", the application is closed.
        """
        # Display a message box with a question asking the user if they want to exit.
        # Returns 1 if the user clicks "Yes", otherwise returns 0.
        if tkinter.messagebox.askyesno("Library Management System", "Do you want to exit"):
            # If the user clicks "Yes", destroy the root window to close the application.
            self.root.destroy()
            return
          
    def delete(self):
        """
        Deletes a member from the library database based on the selected prnno and id.
        """
        # Get the values of prnno and id from the variables.
        prnno = self.prnno_var.get()
        id_ = self.id_var.get()

        # If either prnno or id is empty, show an error message and return.
        if not prnno or not id_:
            tkinter.messagebox.showerror("Error", "Please select member to delete")
            return

        # Connect to the database and delete the member with the specified prnno and id.
        with mysql.connector.connect(host="localhost", user="root", password="root", database="mydata") as conn:
            # Set autocommit to True to commit changes immediately.
            conn.autocommit = True

            # Create a cursor object to execute SQL statements.
            cursor = conn.cursor()

            # Execute the delete statement with placeholders for prnno and id.
            cursor.execute("DELETE FROM library WHERE prnno = %s AND id = %s", (prnno, id_))

            # Show a success message after deletion.
            tkinter.messagebox.showinfo("Success", "Member deleted successfully")
  

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
