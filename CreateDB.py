import sqlite3

if __name__ == "__main__":
    authors_db = sqlite3.connect('authors.db')
    cursor_authors  = authors_db.cursor()
    cursor_authors.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            login TEXT NOT NULL UNIQUE 
        );                               
        CREATE TABLE IF NOT EXISTS blog (
            id INTEGER PRIMARY KEY,
            owner_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (owner_id) REFERENCES users (id) ON DELETE CASCADE
        );                   
        CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY,
            header TEXT NOT NULL,
            text TEXT,
            author_id INTEGER NOT NULL,
            blog_id INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES users (id) ON DELETE CASCADE,
            FOREIGN KEY (blog_id) REFERENCES blog (id) ON DELETE CASCADE
        );
                                
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY,
            owner_id INTEGER NOT NULL,
            post_id INTEGER NOT NULL,
            text TEXT,
            FOREIGN KEY (owner_id) REFERENCES users (id) ON DELETE CASCADE,
            FOREIGN KEY (post_id) REFERENCES post (id) ON DELETE CASCADE                     
        )                         
    ''')

    authors_db.commit()
    authors_db.close()

    logs_db = sqlite3.connect('logs.db')
    cursor_logs = logs_db.cursor()
    cursor_logs.executescript('''
        CREATE TABLE IF NOT EXISTS space_type (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );                               
        CREATE TABLE IF NOT EXISTS event_type (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );                    
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            datetime TEXT NOT NULL,
            user_id TEXT NOT NULL,
            space_type_id INTEGER NOT NULL,
            event_type_id INTEGER NOT NULL,
            FOREIGN KEY (space_type_id) REFERENCES space_type (id) ON DELETE RESTRICT,
            FOREIGN KEY (event_type_id) REFERENCES event_type (id) ON DELETE RESTRICT
        )                     
    ''')

    cursor_logs.executemany('INSERT INTO space_type (name) VALUES (?)', (('global',),('blog',),('post',)))

    cursor_logs.executemany('INSERT INTO event_type (name) VALUES (?)', (('login',),('comment',),('create_post',),('delete_post',),('logout',)))

    logs_db.commit()
    logs_db.close()
