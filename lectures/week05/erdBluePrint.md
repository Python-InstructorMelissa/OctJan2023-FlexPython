# Class Project ERD
## RPSLS & MadLibs

### User Class
- id
- firstName
- lastName
- gamerName
- createdAt
- updatedAt

### Game
- id
- name
- description
- createdAt
- updatedAt

### GameScores
- id
- game_id
- player01_id
- player02_id
- player01Score
- player02Score
- winningPlayer_id
- datePlayed
- createdAt
- updatedAt


### wordType
- id
- wordType
- createdAt
- updatedAt


### Word Bank
- id
- word
- wordType_id
- createdAt
- updatedAt
