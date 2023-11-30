
from app.config.mysqlconnection import connectToMySQL

class Task:
    
    db = 'zz_db_demo'

    @classmethod
    def add(cls, data):
        
        query = """
            INSERT INTO
                tasks
                
                (task) -- all of the column names we want to add data for
                
                VALUES
                (%(task)s)
        """
        return connectToMySQL(cls.db).query_db(query, data) # send query to database
