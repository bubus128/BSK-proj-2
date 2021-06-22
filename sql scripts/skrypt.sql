use sklep;
drop table if exists Sprzedaz;
drop table if exists Produkt;
drop table if exists Pracownik;
drop table if exists Sklep;
drop table if exists Rola;
CREATE TABLE Sklep (
  id INT primary key NOT NULL auto_increment,
  lokalizcja VARCHAR(45) NOT NULL,
  powierzchnia DECIMAL(10) NULL
  );
  
 CREATE TABLE Rola(
	id INT primary key NOT NULL auto_increment,
    nazwa varchar(20)
 );

CREATE TABLE Produkt (
  id INT primary key NOT NULL auto_increment,
  Nazwa VARCHAR(45) NULL,
  Cena DECIMAL(15) NULL
);

CREATE TABLE Pracownik (
  id INT primary key NOT NULL auto_increment,
  imie VARCHAR(45) NULL,
  rola int not null,
  sklep int Not NULL,
  haslo varchar(20) NOT NULL,
  foreign key(sklep) references Sklep(id),
  foreign key(rola) references Rola(id)
);

CREATE TABLE Sprzedaz (
  id INT primary key NOT NULL auto_increment,
  produkt int NOT NULL,
  sprzedawca INT NOT NULL,
  foreign key(produkt) references Produkt(id),
  foreign key(sprzedawca) references Pracownik(id)
 );
