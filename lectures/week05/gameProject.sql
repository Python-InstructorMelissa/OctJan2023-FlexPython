SELECT * FROM gameProject.player;
SELECT * FROM gameProject.game;
SELECT * FROM gameProject.gameScore;
SELECT * FROM gameProject.gameTalk;
SELECT * FROM gameProject.gameTalk_has_reply;
SELECT * FROM gameProject.reply;
SELECT * FROM gameProject.wordBank;
SELECT * FROM gameProject.wordType;
INSERT INTO gameProject.player (firstName, lastName, gamerName)
VALUES ("Melissa", "Longenberger", "HoneyBee24");
INSERT INTO gameProject.player (firstName, lastName, gamerName)
VALUES ("Jane", "Doe", "janeyGirl");
INSERT INTO gameProject.player (firstName, lastName, gamerName)
VALUES ("Boooooob", "Ross", "HappyTrees");
INSERT INTO gameProject.player (firstName, lastName, gamerName)
VALUES ("Test", "Testerson", "TestyTesterson");

UPDATE gameProject.player 
SET firstName="Bob"
WHERE id=3;

DELETE FROM gameProject.player
WHERE id = 4;

INSERT INTO gameProject.game (name, description)
VALUES ("Rock Paper Scissors Lizard Spock", "A TV show adaptation of the traditional RPS game");

INSERT INTO gameProject.gameScore (player01Score, player02Score, game_id, player01_id, player02_id, winningPlayer_id)
VALUES (1,0,1,3,2,3);

-- Get all from 1st table, join second table on 1st tables column that = 2nd tables column;
-- Get all from 1st table, join second table on 1st tables column that = 2nd tables column where 1st tables id = ?;
SELECT * FROM gameProject.gameScore 
LEFT JOIN gameProject.game ON gameProject.gameScore.game_id = gameProject.game.id;