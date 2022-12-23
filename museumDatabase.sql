/*
#Kenzie Fjestad UCID: 30140194
#Isaac Hus UCID: 30139733
#Elea Bahhadi UCID: 30150493
#Bruce Gillis UCID: 30143110
*/

DROP DATABASE IF EXISTS MUSEUMDATABASE;
CREATE DATABASE MUSEUMDATABASE; 
USE MUSEUMDATABASE;

DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS (
	id		varchar(30) not null,
    pass		varchar(30) not null,
    permision 		varchar(10) not null
);

INSERT INTO USERS (id, pass, permision)
VALUES
("1111", "admin", "admin"),
("2222", "dataentry", "dataentry"),
("3333", "enduser", "enduser"),
("4444", "blocked", "blocked")
;


DROP TABLE IF EXISTS COLLECTION;
CREATE TABLE COLLECTION (
	Name		varchar(50) not null,
    type		varchar(30) not null,
    descript	varchar(100) not null,
    Address		varchar(30) not null,
    Phone		varchar(30) not null,
    Contact		varchar(30) not null,
    primary key (name)
);

INSERT INTO COLLECTION (name, type, descript, Address, Phone, Contact)
VALUES
("Department of Paintings", "Paintings", "Department responsible for all paintings at the Louvre", "Louvre", "324234234", "John Francois"),
("Department of Oriental Antiquities", "Antiques", "Department responsible for sculptures in the Louvre", "Louvre", "32442442", "Betty Clive"),
("Department of Works of Art from the Middle Ages", "Middle Ages Artwork" , "Department respnsible for Works of Art from the Middle Ages in the Louvre", "Louvre", "325423242", "Chris Richard"),
("National Portrait Gallery", "Portraits", "Mainly portait paintings are part of this collection", "Netherland", "1212233443", "Bisaac Shush"),
("Museo Nacional Thyssen-Bornemisza", "German Items", "Items from Germany mainly", "Madrid", "45345343", "Phil Dunphy"),
("Victoria and Albert Museum", "Medieval Items", "Large Medieval collection", "London", "654645623", "John Smith"),
("Roger Fund", "British Items", "Collection of British Items", "London", "345343534", "Ben Roger")
;


DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	Name			varchar(30) not null,
    Main_style		varchar(30) not null,
    descript		varchar(100) not null,
    Epoch			varchar(30) not null,
    Origin_country	varchar(30) not null,
    Date_died		varchar(30) not null,
    Date_born		varchar(30) not null,
    primary key (name)
);

INSERT INTO ARTIST (Name, Main_style, descript, Epoch, Origin_country, Date_died, Date_born)
VALUES
("John II", "Landscape", "Pretty cute guy", "17th Century", "England", "1795", "1743"),
("Ludovico", "Portraits", "Good hang", "16th Century", "Italy", "1589", "1523"),
("Joseph Tailor", "Jewllery", "Object orientated", "18th Century", "England", "1717", "1678"),
("Hans Hilbein", "Portraits", "Grew up in a small German village", "16th Century", "Germany","1552", "1519"),
("Benedetto da Rovezzano", "Sculptures", "Studied in Rome", "16th Century", "Italy", "1554", "1474"),
("Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown")
;


DROP TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITION (
	name		varchar(30) not null,
    End_date	varchar(30) not null,
    Start_date	varchar(30) not null,
    primary key (name)
);

INSERT INTO EXHIBITION (name, End_date, Start_date)
VALUES
("King Henry VIII", "30/11/22", "30/08/22"),
("Paintings", "01/02/19", "01/05/19"),
("Sculptures", "21/05/13", "21/09/13");



DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
	id_no			varchar(10) not null,
    Title			varchar(30) not null,
    Origin			varchar(30) not null,
    Epoch			varchar(30) not null,
    Descript		varchar(100) not null,
    Year_created	varchar(30) not null,
    Artist_name 	varchar(30) not null,
    EName			varchar(30) not null,
    Style           varchar(30) not null,
	primary key (id_no),
    foreign key (Artist_name)	references ARTIST(Name),
    foreign key (EName) 		references EXHIBITION(Name)
);

INSERT INTO ART_OBJECT (id_no, Title, Origin, Epoch, Descript, Year_created, Artist_name, EName, Style)
VALUES
("1", "View of the Thames", "England", "18th Century", "Artwork revovered after WWII", "1764", "John II", "Paintings", "Realism"),
("2", "The Adoration of the Magi", "Italy","16th Century", "This painting belongs to a personal collector", "1500-1600", "Ludovico", "Paintings", "Expressionism"),
("3", "Statue", "Syria", "Roman Imperial", "Fragments on the sculpture", "-61-324", "Unknown", "Sculptures", "Photorealism"),
("4", "Bust", "Italy", "Roman Imperial", "Bust is of a high up official", "23-245", "Unknown", "Sculptures", "Photorealism"),
("5", "the Regent", "England", "18th Century", "Diamond", "1704", "Joseph Tailor", "King Henry VIII", "Object"),
("6", "Fan", "German", "18th Century", "Fancy hand Fan", "1785", "Unknown", "Paintings", "Expressionism"),
("7", "Henry VII", "Netherland", "16th Century", "Portrait of King Henry VII", "1505", "Unknown", "King Henry VIII", "Photorealism"),
("8", "Henry VIII", "German", "16th Century", "Portrait of King Henry VIII", "1537", "Hans Hilbein", "King Henry VIII", "Photorealism"),
("9", "Unidentified Saint", "Unknown", "16th Century", "Sculpture of a Saint, his identity is unknown", "1505", "Unknown", "Sculptures", "Expressionism"),
("10", "Angel Bearing Candlestick", "Italy", "16th Century", "Statue of an angel", "1526", "Benedetto da Rovezzano", "Sculptures", "Surrealism"),
("11", "Armor of King Henry VIII", "Italy", "16th Century", "Field armor made for King Henry VIII", "1544", "Unknown", "King Henry VIII", "Realism"),
("12", "Bowl from Burghley House", "England",  "16th Century", "Bowl main of Chinese porcelain", "1578", "Unknown", "King Henry VIII", "Realism")
;

DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE (
	sculpt_id		varchar(30) not null,
    Weight			varchar(30) not null,
    Height			varchar(30) not null,
    Material		varchar(30) not null,
    primary key (sculpt_id),
    foreign key (sculpt_id) references ART_OBJECT(id_no)
);

INSERT INTO SCULPTURE (sculpt_id, Weight, Height, Material)
VALUES
("3", "15", "34", "Marble"),
("4", "23", "63", "Bronze"),
("9", "18", "52", "Terracotta"),
("10", "141", "101", "Bronze")
;

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
	paint_id		varchar(10) not null,
    Drawn_on		varchar(30) not null,
    Paint_type		varchar(30) not null,
    primary key (paint_id),
    foreign key (paint_id) references ART_OBJECT(id_no)
);

INSERT INTO PAINTING (paint_id, Drawn_on, Paint_type)
VALUES
("1", "Cloth", "Paint"),
("2", "Wood", "Paint"),
("7", "Panel", "Oil"),
("8", "Canvas", "Oil");

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
	other_id		varchar(10) not null,
    Type			varchar(30) not null,
    primary key (other_id),
    foreign key (other_id) references ART_OBJECT(id_no)
);

INSERT INTO OTHER (other_id, type)
VALUES
("5", "Jewel"),
("6", "Fan"),
("11", "Armor"),
("12", "Dish")
;


DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANENT_COLLECTION (
	Cost			varchar(30) not null,
    Date_acquired	varchar(30) not null,
    Status			varchar(30) not null,
    id_no			varchar(10) not null,
    primary key (id_no),
    foreign key (id_no) references ART_OBJECT(id_no)
);

INSERT INTO PERMANENT_COLLECTION (Cost, Date_acquired, Status, id_no)
VALUES
("$960,000", "12/08/13", "On Display", "7"),
("$1,260,000", "16/10/15", "On Display", "8"),
("$660,000", "24/02/09", "Being Refurbished", "9"),
("$2,160,000", "23/06/21", "In Storage", "10"),
("$10,260,000", "09/11/07", "On Display", "11"),
("$1,380,000", "01/12/10", "In Storage", "12")
;

DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED (
	Date_returned		varchar(30) not null,
    Date_borrowed		varchar(30) not null,
    CName				varchar(50) not null,
    id_no				varchar(10) not null,
    primary key (id_no),
    foreign key (id_no) references ART_OBJECT(id_no),
    foreign key (CName) references COLLECTION (Name)
);

INSERT INTO BORROWED (Date_returned, Date_borrowed, CName, id_no)
VALUES
("18/05/24", "18/05/20", "Department of Paintings", "1"),
("23/09/23", "23/09/19", "Department of Paintings", "2"),
("06/12/17", "06/12/14", "Department of Oriental Antiquities", "3"),
("06/02/17", "06/02/14", "Department of Oriental Antiquities", "4"),
("26/11/21", "26/11/25", "Department of Works of Art from the Middle Ages", "5"),
("16/01/17", "16/01/14", "Department of Works of Art from the Middle Ages", "6")
;


