CREATE DATABASE library_db;

USE library_db;
GO

CREATE TABLE [User] (
    UserID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(50),
    Phone VARCHAR(20)
);

CREATE TABLE Book (
    BookID INT PRIMARY KEY,
    Title VARCHAR(50),
    Author VARCHAR(50),
    Publisher VARCHAR(50),
    ISBN VARCHAR(20),
    CallNumber VARCHAR(30),
    Subject VARCHAR(50)
);

CREATE TABLE Catalog (
    CatalogID INT PRIMARY KEY,
    BookID INT FOREIGN KEY REFERENCES Book(BookID),
    Subject VARCHAR(50)
);

CREATE TABLE Reservation (
    ReservationID INT PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES [User](UserID),
    BookID INT FOREIGN KEY REFERENCES Book(BookID),
    ReservationDate DATE,
    Status VARCHAR(20)
);

CREATE TABLE Loan (
    LoanID INT PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES [User](UserID),
    BookID INT FOREIGN KEY REFERENCES Book(BookID),
    CheckoutDate DATE,
    DueDate DATE,
    ReturnDate DATE,
    Status VARCHAR(20)
);

CREATE TABLE Fine (
    FineID INT PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES [User](UserID),
    BookID INT FOREIGN KEY REFERENCES Book(BookID),
    Amount DECIMAL(10,2),
    Reason VARCHAR(50),
    PaymentStatus VARCHAR(20)
);

CREATE TABLE Waitlist (
    WaitlistID INT PRIMARY KEY,
    BookID INT FOREIGN KEY REFERENCES Book(BookID),
    UserID INT FOREIGN KEY REFERENCES [User](UserID)
);

CREATE TABLE [Transaction] (
    TransactionID INT PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES [User](UserID),
    BookID INT FOREIGN KEY REFERENCES Book(BookID),
    Type VARCHAR(20),
    DateTime DATETIME
);