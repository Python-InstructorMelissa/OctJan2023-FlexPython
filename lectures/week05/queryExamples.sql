-- Get all from a TABLE
SELECT *
FROM tableName;

-- Examples
SELECT *
FROM user;

-- This would only display the firstName column of the table queried
SELECT firstName
FROM user

-- Get 1 item from the table
-- The %()s is how we will state a parameter that will change in our flask code.  Inside the () will be the column name
SELECT *
FROM tableName
WHERE id = %(id)s;

SELECT *
FROM tableName
WHERE email = %(email)s;

-- Examples
SELECT *
FROM user
WHERE id = 1

SELECT firstName
FROM user
WHERE id = 1


-- Get all users who's first name starts with b
SELECT * FROM user WHERE firstName LIKE 'b%';

-- Create new row in TABLE
INSERT INTO tableName (columnName, columnName)
VALUES (%(columnNameValue)s, %(columnNameValue)s);

-- Examples 
INSERT INTO user (firstName, lastName, username)
VALUES ("Bob", "Barker", "PriceIsRight");
-- This will work unless you have not null checked for an columns not listed
insert into user (firstName, lastName) 
values ("Princess", "Frog")
-- This will not work as the column count does not match
insert into user (firstName, lastName) values ("Mia")
-- This works but the system doesn't know first from last so if firstName is listed first then the 1st value should be last name
insert into user (firstName, lastName) values ("Dew", "Mountain")
insert into user (username, lastName, firstName) values ("Mr T","Longenberger","Mr Tucker")
insert into user (firstName) values ("testing"), ("mcTesterson");


-- Update an entry in a table
UPDATE tableName
SET columnName = "%(columnNameValue)s"
WHERE id = %(id)s;

-- Examples
update user set username="froggyPrincess" where id=17;
update user set firstName="Mountain", lastName="Dew", username="Code Red" where id=18