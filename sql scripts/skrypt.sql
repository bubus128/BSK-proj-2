use sklep;
drop table if exists Sprzedaz;
drop table if exists Produkt;
drop table if exists Pracownik;
drop table if exists Sklep;
CREATE TABLE Sklep (
  idSklep INT primary key NOT NULL,
  Lokalizcja VARCHAR(45) NOT NULL,
  Powierzchnia DECIMAL(10) NULL
  );

CREATE TABLE Produkt (
  idProdukt INT primary key NOT NULL,
  Nazwa VARCHAR(45) NULL,
  Cena DECIMAL(15) NULL
);

CREATE TABLE Pracownik (
  PESEL int primary key NOT NULL,
  Imie VARCHAR(45) NULL,
  Nazwisko VARCHAR(45) NOT NULL,
  Stanowisko VARCHAR(45) NULL,
  Telefon VARCHAR(9) NOT NULL,
  idSklep int Not NULL,
  foreign key(idSklep) references Sklep(idSklep)
);

CREATE TABLE Sprzedaz (
  idSprzedaz INT primary key NOT NULL,
  Pracownik_PESEL NVARCHAR(11) NOT NULL,
  Produkt_idProdukt INT NOT NULL,
  idProdukt int NOT NULL,
  sprzedawca int NOT NULL,
  foreign key(idProdukt) references Produkt(idProdukt),
  foreign key(sprzedawca) references Pracownik(PESEL)
 );
