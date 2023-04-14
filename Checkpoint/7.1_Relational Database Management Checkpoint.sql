-- Create Wine table
CREATE TABLE Wine (NumW INT PRIMARY KEY, Category VARCHAR(255), Year INT, Degree INT);

-- Create Producer table
CREATE TABLE Producer (NumP INT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), Region VARCHAR(255));

-- Create Harvest table
CREATE TABLE Harvest (HarvestID INT PRIMARY KEY IDENTITY(1,1), NumW INT, NumP INT, Quantity INT,
    FOREIGN KEY (NumW) REFERENCES Wine(NumW),
    FOREIGN KEY (NumP) REFERENCES Producer(NumP)
);

-- Query 2
SELECT NumP, FirstName, LastName, Region
FROM Producer;

-- Query 3
SELECT NumP, FirstName, LastName, Region
FROM Producer
ORDER BY FirstName ASC, LastName ASC;

-- Query 4
SELECT NumP, FirstName, LastName, Region
FROM Producer
WHERE Region = 'Sousse';

-- Query 5
SELECT SUM(Quantity) AS TotalQuantity
FROM Harvest
WHERE NumW IN (SELECT NumW FROM Wine WHERE Degree = 12);

-- Query 6
SELECT Wine.Category, SUM(Harvest.Quantity) AS CategoryQuantity
FROM Harvest
JOIN Wine On Harvest.NumW = Wine.NumW
GROUP BY Wine.Category;

-- Query 7
SELECT Producer.FirstName, SUM(Harvest.Quantity) AS TotalQuantity
FROM Producer
JOIN Harvest ON Producer.NumP = Harvest.NumP
WHERE Producer.Region = 'Sousse' AND Harvest.Quantity > 300
GROUP BY Producer.FirstName;

-- Query 8
SELECT Wine.NumW, Wine.Category, Wine.Year, Wine.Degree
FROM Wine
JOIN Harvest ON Wine.NumW = Harvest.NumW
JOIN Producer ON Harvest.NumP = Producer.NumP
WHERE Wine.Degree > 12 AND Producer.FirstName = 'Jacob';