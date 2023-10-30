SELECT * FROM user;
-- Basic layout for get SELECT * FROM tableName;
-- Basic layout for get1 SELECT * FROM tableName WHERE id=rowId
INSERT INTO user (firstName, lastName, username) VALUE ("Melissa", "Longenberger", "honeybee");
INSERT INTO user (firstName, lastName, username) VALUE ("Kevin", "Souhala", "kman"), ("Robert", "S", "theRobster"), ("Stephani", "M", "theAmzingStephanie"), ("Jane","Doe","janygirl"), ("Bob", "Ross", "happyTrees");
-- Basic layout for instert/adding INSERT INTO <tableName> (column01, column02) VALUE ("column01Data", "column02Data"); 
UPDATE user SET username="theAmazingStephanie" WHERE id=4;
UPDATE user SET firstName="Stephanie" WHERE id=4;
-- Basic layout for updating UPDATE tableName SET column01="column01NewData" WHERE id=rowId
INSERT INTO user (firstName, lastName, username) VALUE ("Melissa", "Longenberger", "honeybee");
DELETE FROM user WHERE id=7;
-- DELETE FROM user; Errors out the workbench
INSERT INTO user (firstName, lastName, username) VALUE ("Melissa", "Longenberger", "honeybee");
DELETE FROM user WHERE id=15;

SELECT * FROM fish;
INSERT INTO fish (species, count, gender, user_id) VALUE ("Guppy",5, "Male",1);
INSERT INTO fish (species, count, gender, user_id) VALUE ("Guppy",5, "Male",3), ("Guppy",10, "Female",1), ("Guppy",6, "Female",3), ("Guppy",5, "Female",2), ("Guppy",5, "Male",5),("Guppy",5, "Male",4),("Guppy",5, "Male",6);


-- SELECT * FROM table1 LEFT JOIN table2 on table1.id=table2.table1_id;
-- SELECT * FROM table1 LEFT JOIN table2 on table1.id=table2.table1_id WHERE table1.id=value;
SELECT * FROM user LEFT JOIN fish on user.id=fish.user_id;
SELECT * FROM user LEFT JOIN fish on user.id=fish.user_id WHERE user.id=3;
SELECT * FROM fishDatabase.user LEFT JOIN fishDatabase.fish on fishDatabase.user.id=fishDatabase.fish.user_id WHERE fishDatabase.user.id=3;