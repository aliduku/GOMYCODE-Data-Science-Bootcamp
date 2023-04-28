USE library_db;
GO

--Users
INSERT INTO [User] (UserID, Name, Email, Phone)
VALUES 
(1, 'John Doe', 'john.doe@example.com', '555-1234'),
(2, 'Jane Smith', 'jane.smith@example.com', '555-5678'),
(3, 'Bob Johnson', 'bob.johnson@example.com', '555-9012'),
(4, 'Alice Williams', 'alice.williams@example.com', '555-3456'),
(5, 'Mike Brown', 'mike.brown@example.com', '555-7890'),
(6, 'Karen Davis', 'karen.davis@example.com', '555-2345'),
(7, 'Tom Lee', 'tom.lee@example.com', '555-6789'),
(8, 'Sara Wilson', 'sara.wilson@example.com', '555-0123'),
(9, 'Chris Green', 'chris.green@example.com', '555-4567'),
(10, 'Jessica Taylor', 'jessica.taylor@example.com', '555-8901'),
(11, 'David Martin', 'david.martin@example.com', '555-2345'),
(12, 'Emily Thompson', 'emily.thompson@example.com', '555-6789'),
(13, 'Kevin Lewis', 'kevin.lewis@example.com', '555-0123'),
(14, 'Nancy Hall', 'nancy.hall@example.com', '555-4567'),
(15, 'Mark Hernandez', 'mark.hernandez@example.com', '555-8901'),
(16, 'Ashley Young', 'ashley.young@example.com', '555-2345'),
(17, 'Ryan Wright', 'ryan.wright@example.com', '555-6789'),
(18, 'Maria Rodriguez', 'maria.rodriguez@example.com', '555-0123'),
(19, 'Erica Mitchell', 'erica.mitchell@example.com', '555-4567'),
(20, 'Trevor Scott', 'trevor.scott@example.com', '555-8901');

--Books
INSERT INTO Book (BookID, Title, Author, Publisher, ISBN, CallNumber, Subject)
VALUES
(1, 'To Kill a Mockingbird', 'Harper Lee', 'J. B. Lippincott & Co.', '978-0446310789', 'PS3562.E353 T6', 'Fiction'),
(2, 'Pride and Prejudice', 'Jane Austen', 'T. Egerton', '978-0486284736', 'PR4034.P7', 'Fiction'),
(3, '1984', 'George Orwell', 'Secker & Warburg', '978-0451524935', 'PR6029.R8 N49 1990', 'Fiction'),
(4, 'The Catcher in the Rye', 'J.D. Salinger', 'Little, Brown and Company', '978-0316769488', 'PS3537.A426 C3 1951', 'Fiction'),
(5, 'Brave New World', 'Aldous Huxley', 'Chatto & Windus', '978-0060850524', 'PR6015.U9 B65 2006', 'Fiction'),
(6, 'One Hundred Years of Solitude', 'Gabriel García Márquez', 'Harper & Row', '978-0060883287', 'PQ8180.17.A73 C513 2006', 'Fiction'),
(7, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Charles Scribner''s Sons', '978-0743273565', 'PS3511.I9 G7 2004', 'Fiction'),
(8, 'The Lord of the Rings', 'J.R.R. Tolkien', 'George Allen & Unwin', '978-0547928210', 'PR6039.O32 L6 2012', 'Fantasy'),
(9, 'Animal Farm', 'George Orwell', 'Secker & Warburg', '978-0451526342', 'PR6029.R8 A63 2003', 'Fiction'),
(10, 'Lord of the Flies', 'William Golding', 'Faber and Faber', '978-0399501487', 'PR6013.O35 L6 1999', 'Fiction'),
(11, 'The Hobbit', 'J.R.R. Tolkien', 'George Allen & Unwin', '978-0547928227', 'PR6039.O32 H6 2012', 'Fantasy'),
(12, 'The Diary of a Young Girl', 'Anne Frank', 'Contact Publishing', '978-0553296983', 'D810.J4 F73313 1995', 'Memoir'),
(13, 'The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 'Pan Books', '978-0345391803', 'PR6051.D3352 H58 1995', 'Science Fiction'),
(14, 'The Little Prince', 'Antoine de Saint-Exupéry', 'Reynal & Hitchcock', '978-0156012195', 'PZ8.S13 Li 2000', 'Children''s literature'),
(15, 'Slaughterhouse-Five', 'Kurt Vonnegut', 'Delacorte Press', '978-0440180296', 'PS3572.O5 S6 1991', 'Fiction'),
(16, 'The Picture of Dorian Gray', 'Oscar Wilde', 'Lippincott''s Monthly Magazine', '978-0486278070', 'PR5819.A1 2000', 'Fiction'),
(17, 'Wuthering Heights', 'Emily Bronte', 'Thomas Cautley Newby', '978-0141439556', 'PR4172.W8', 'Fiction'),
(18, 'Jane Eyre', 'Charlotte Bronte', 'Smith, Elder & Co.', '978-0141441146', 'PR4167.J3', 'Fiction'),
(19, 'The Adventures of Huckleberry Finn', 'Mark Twain', 'Chatto & Windus', '978-0486403499', 'PS1305.A1 1999', 'Fiction'),
(20, 'The Adventures of Tom Sawyer', 'Mark Twain', 'American Publishing Company', '978-0451526533', 'PS1306.A1 2002', 'Fiction'),
(21, 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'The Russian Messenger', '978-0140449242', 'PG3326.A6 2003', 'Fiction'),
(22, 'Crime and Punishment', 'Fyodor Dostoevsky', 'The Russian Messenger', '978-0140449136', 'PG3326.A6 2003', 'Fiction'),
(23, 'Anna Karenina', 'Leo Tolstoy', 'The Russian Messenger', '978-0143035008', 'PG3366.A6 2004', 'Fiction'),
(24, 'War and Peace', 'Leo Tolstoy', 'The Russian Messenger', '978-0140447934', 'PG3326.A6 2005', 'Fiction'),
(25, 'Gone with the Wind', 'Margaret Mitchell', 'Macmillan Publishers', '978-1451635621', 'PS3525.I972 G6 2011', 'Historical Fiction'),
(26, 'The Count of Monte Cristo', 'Alexandre Dumas', 'Le Journal des débats', '978-0140449266', 'PQ2226.A3 2003', 'Adventure Fiction'),
(27, 'Les Misérables', 'Victor Hugo', 'A. Lacroix, Verboeckhoven & Cie.', '978-0140444308', 'PQ2286.A2 N43 1992', 'Historical Fiction'),
(28, 'Don Quixote', 'Miguel de Cervantes', 'Francisco de Robles', '978-0060934347', 'PQ6324 .E5 2003', 'Satire'),
(29, 'The Sun Also Rises', 'Ernest Hemingway', 'Scribner''s', '978-0684800714', 'PS3515.E37 S8 1995', 'Fiction'),
(30, 'For Whom the Bell Tolls', 'Ernest Hemingway', 'Charles Scribner''s Sons', '978-0684803357', 'PS3515.E37 F6 1995', 'Fiction'),
(31, 'A Farewell to Arms', 'Ernest Hemingway', 'Charles Scribner''s Sons', '978-0684801469', 'PS3515.E37 F3 1995', 'Fiction'),
(32, 'The Fault in Our Stars', 'John Green', 'Dutton Books', '978-0525478812', 'PZ7.G8233 Fau 2012', 'Young Adult Fiction'),
(33, 'The Hunger Games', 'Suzanne Collins', 'Scholastic Press', '978-0439023481', 'PZ7.C6837 Hun 2008', 'Young Adult Fiction'),
(34, 'Catching Fire', 'Suzanne Collins', 'Scholastic Press', '978-0439023498', 'PZ7.C6837 Cat 2009', 'Young Adult Fiction'),
(35, 'Mockingjay', 'Suzanne Collins', 'Scholastic Press', '978-0439023511', 'PZ7.C6837 Moj 2010', 'Young Adult Fiction'),
(36, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Norstedts förlag', '978-0307269751', 'PT9876.22.A693 M3613 2008', 'Mystery/Thriller'),
(37, 'The Sun Also Rises', 'Ernest Hemingway', 'Scribner', '978-0743297332', 'PS3515.E37 S9 2006', 'Fiction'),
(38, 'The Grapes of Wrath', 'John Steinbeck', 'Viking Press', '978-0143039433', 'PS3537.T3234 G8 2006', 'Fiction'),
(39, 'The Color Purple', 'Alice Walker', 'Harcourt Brace Jovanovich', '978-0156031820', 'PS3573.A425 C6 2003', 'Fiction'),
(40, 'Their Eyes Were Watching God', 'Zora Neale Hurston', 'J. B. Lippincott', '978-0061120060', 'PS3515.U789 T48 2006', 'Fiction');

--Catalogs
INSERT INTO Catalog (CatalogID, BookID, Subject)
SELECT ROW_NUMBER() OVER (ORDER BY Subject) AS CatalogID, BookID, Subject
FROM Book;


--Reservations
INSERT INTO Reservation (ReservationID, UserID, BookID, ReservationDate, Status)
VALUES
(1, 2, 5, '2023-05-01', 'Confirmed'),
(2, 5, 12, '2023-05-02', 'Confirmed'),
(3, 7, 17, '2023-05-03', 'Confirmed'),
(4, 11, 8, '2023-05-04', 'Pending'),
(5, 14, 22, '2023-05-05', 'Pending'),
(6, 16, 31, '2023-05-06', 'Pending'),
(7, 19, 35, '2023-05-07', 'Pending'),
(8, 1, 39, '2023-05-08', 'Pending'),
(9, 4, 2, '2023-05-09', 'Pending'),
(10, 8, 14, '2023-05-10', 'Pending');

--Loans
INSERT INTO Loan (LoanID, UserID, BookID, CheckoutDate, DueDate, ReturnDate, Status)
VALUES
(1, 2, 9, '2023-05-01', '2023-05-15', NULL, 'Checked Out'),
(2, 5, 25, '2023-05-02', '2023-05-16', NULL, 'Checked Out'),
(3, 7, 33, '2023-05-03', '2023-05-17', NULL, 'Checked Out'),
(4, 11, 3, '2023-05-04', '2023-05-18', NULL, 'Checked Out'),
(5, 14, 16, '2023-05-05', '2023-05-19', NULL, 'Checked Out'),
(6, 16, 29, '2023-05-06', '2023-05-20', NULL, 'Checked Out'),
(7, 19, 36, '2023-05-07', '2023-05-21', NULL, 'Checked Out'),
(8, 1, 38, '2023-05-08', '2023-05-22', NULL, 'Checked Out'),
(9, 4, 7, '2023-05-09', '2023-05-23', NULL, 'Checked Out'),
(10, 8, 21, '2023-05-10', '2023-05-24', NULL, 'Checked Out');

--Fines
INSERT INTO Fine (FineID, UserID, BookID, Amount, Reason, PaymentStatus) VALUES
(1, 8, 21, 12.50, 'Late return', 'Unpaid'),
(2, 14, 34, 7.20, 'Damage', 'Paid'),
(3, 3, 18, 5.00, 'Lost book', 'Unpaid'),
(4, 6, 29, 3.80, 'Late return', 'Paid'),
(5, 12, 2, 6.25, 'Damage', 'Unpaid'),
(6, 19, 15, 9.00, 'Late return', 'Paid'),
(7, 10, 6, 15.00, 'Lost book', 'Unpaid'),
(8, 17, 33, 8.75, 'Late return', 'Unpaid'),
(9, 2, 7, 4.50, 'Damage', 'Paid'),
(10, 11, 26, 10.25, 'Late return', 'Unpaid');


--Waitlists
INSERT INTO Waitlist (WaitlistID, BookID, UserID) VALUES
(1, 10, 6),
(2, 34, 15),
(3, 27, 4),
(4, 11, 1),
(5, 2, 9),
(6, 19, 5),
(7, 25, 8),
(8, 32, 12),
(9, 36, 18),
(10, 40, 3);

--Transactions
INSERT INTO [Transaction] (TransactionID, UserID, BookID, Type, DateTime) VALUES
(1, 5, 13, 'CHECKOUT', '2023-04-26 15:00:00'),
(2, 16, 20, 'CHECKOUT', '2023-04-27 10:30:00'),
(3, 7, 35, 'RETURN', '2023-04-24 14:15:00'),
(4, 12, 14, 'CHECKOUT', '2023-04-23 11:45:00'),
(5, 2, 7, 'CHECKOUT', '2023-04-25 09:00:00'),
(6, 9, 38, 'RETURN', '2023-04-22 16:30:00'),
(7, 3, 1, 'CHECKOUT', '2023-04-20 12:00:00'),
(8, 18, 23, 'CHECKOUT', '2023-04-19 08:45:00'),
(9, 1, 5, 'RETURN', '2023-04-21 13:00:00'),
(10, 14, 18, 'CHECKOUT', '2023-04-18 17:00:00');
