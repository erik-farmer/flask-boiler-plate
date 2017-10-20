CREATE USER flask_demo_user LOGIN;

CREATE DATABASE flask_demo_db
  WITH OWNER  flask_demo_user;

\c flask_demo_db;

SET ROLE flask_demo_user;

CREATE TABLE foos(
  id INT PRIMARY KEY,
  name VARCHAR,
  created_at DATE NOT NULL DEFAULT CURRENT_DATE
);
