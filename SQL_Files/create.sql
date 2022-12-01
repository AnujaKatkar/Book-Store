DROP TABLE IF EXISTS authors CASCADE;
DROP TABLE IF EXISTS countries CASCADE;
DROP TABLE IF EXISTS publications CASCADE;
DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS orderdetails CASCADE;

CREATE TABLE Authors(
	AuthorID SERIAL PRIMARY KEY,
	AuthorName varchar(25) NOT NULL
);

CREATE TABLE Countries(
	CountryID SERIAL,
	CountryName varchar(60) NOT NULL,
	PRIMARY key (countryID)
);

CREATE TABLE Publications(
	PublicationID SERIAL PRIMARY KEY,
	PublicationName varchar(25) NOT NULL,
	CountryID int NOT NULL,
	FOREIGN KEY (CountryID) REFERENCES Countries ON DELETE SET NULL
);

CREATE TABLE Books(
	BookID SERIAL PRIMARY KEY,
	AuthorID int NOT NULL,
	PublicationID int NOT NULL,
	Title varchar(20) NOT NULL,
	Genre varchar(15) NOT NULL,
	PublicationYear int NOT NULL,
	Price real NOT NULL,
	FOREIGN KEY (AuthorID) REFERENCES authors ON DELETE SET NULL,
	FOREIGN KEY (PublicationID) REFERENCES Publications ON DELETE SET NULL
);

CREATE TABLE Customers(
	CustomerID SERIAL PRIMARY KEY,
	CustomerName varchar(25) NOT NULL,
	Address varchar(80) NOT NULL,
	PhoneNumber varchar(22) NOT NULL,
	PostalCode int NOT NULL
);

CREATE TABLE Orders(
	OrderID SERIAL PRIMARY KEY,
	CustomerID int,
	OrderDate date NOT NULL,
	Total real NOT NULL,
	FOREIGN KEY (CustomerID) REFERENCES Customers ON DELETE CASCADE
);

CREATE TABLE OrderDetails(
	OrderID int NOT NULL,
	BookID int NOT NULL,
	Price int NOT NULL,
	PRIMARY KEY(OrderID, BookID),
	FOREIGN KEY (OrderID) REFERENCES Orders ON DELETE CASCADE,
	FOREIGN KEY(BookID) REFERENCES Books ON DELETE CASCADE
);