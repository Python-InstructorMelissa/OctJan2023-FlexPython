from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Game:
    db = 'week13Baseball'
    def __init__(self, data):
        self.id = data['id']
        self.team1 = data['team1']
        self.team2 = data['team2']
        self.final_score = data['final_score']
        self.game_info = data['game_info']
        self.game_date = data['game_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM game;'
        results = connectToMySQL(cls.db).query_db(query)
        games = []
        for row in results:
            games.append(cls(row))
        return games

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM game WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO game (team1, team2, final_score, game_info, game_date, user_id) VALUES (%(team1)s, %(team2)s, %(final_score)s, %(game_info)s, %(game_date)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE game SET team1 = %(team1)s, team2 = %(team2)s, final_score=%(final_score)s, game_info=%(game_info)s, game_date=%(game_date)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM game WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validation(game):
        is_valid = True
        if len(game['team1']) < 2:
            is_valid = False
            flash("We need to know the team name.")
        if len(game['team2']) < 2:
            is_valid = False
            flash("We need to know the team name.")
        return is_valid