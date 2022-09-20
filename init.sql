CREATE DATABASE secretstoragepoc;
CREATE DATABASE anup;
\connect secretstoragepoc;
CREATE TABLE "user" ( last_name varchar(80), first_name varchar(80), age int);
CREATE TABLE "crypto" ( name  varchar(300), gslb varchar(300), version varchar(300), certificate varchar(100000), key varchar(100000));