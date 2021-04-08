CREATE DATABASE IF NOT EXISTS CustomerDb;

USE CustomerDb;

drop table if exists Customer;
drop table if exists Store;
drop table if exists Link;

CREATE TABLE Customer (
    cID int,

);

CREATE TABLE Store (
    cID int,
    hID int,
    item varcahr(100),
    category varchar(100),

);

CREATE TABLE Link (
    hID int,
    hashtag varchar(100),

);

CREATE USER ms_user@localhost IDENTIFIED BY 'manageuser';
GRANT SELECT, INSERT, UPDATE, DELETE ON ManageEmp.* TO ms_user@localhost;