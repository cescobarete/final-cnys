CREATE DATABASE IF NOT EXISTS CustomerDb;

USE CustomerDb;

drop table if exists Customer;
drop table if exists Store;
drop table if exists Link;

CREATE TABLE Customer (
    cID int,
    name varchar(100),
    PRIMARY KEY(cID)
);

CREATE TABLE Store (
    cID int,
    hID int,
    item varchar(100),
    category varchar(100),
    FOREIGN KEY(cID) REFERENCES Customer(cID),
    FOREIGN KEY(hID) REFERENCES Link(pID));
);

CREATE TABLE Link (
    hID int,
    hashtag varchar(100),
    PRIMARY KEY(hID)
);

insert into Customer values(1000, 'Christian E');
insert into Customer values(1001, 'Sarah M');
insert into Customer values(1002, 'Nick S');
insert into Customer values(1003, 'Yasir');

insert into Store values(1000, 1, 'Pajamas', 'Clothing');

insert into Link values(1, '#nochill');

CREATE USER ms_user_two@localhost IDENTIFIED BY 'manageuser';
GRANT SELECT, INSERT, UPDATE, DELETE ON CustomerDb.* TO ms_user_two@localhost;