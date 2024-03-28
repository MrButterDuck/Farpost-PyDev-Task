#Просто набор данных для теста работоспособности запросов
import sqlite3

if __name__ == "__main__":
    auth = sqlite3.connect('authors.db')
    c1 = auth.cursor()

    c1.execute("INSERT OR IGNORE   INTO users (login, email) VALUES ('user1', 'user1@example.com')")
    c1.execute("INSERT OR IGNORE   INTO users (login, email) VALUES ('user2', 'user2@example.com')")
    c1.execute("INSERT OR IGNORE   INTO users (login, email) VALUES ('user3', 'user3@example.com')")
    c1.execute("INSERT INTO blog (owner_id, name, description) VALUES (1, 'Blog 1', 'Description of Blog 1')")
    c1.execute("INSERT INTO blog (owner_id, name, description) VALUES (2, 'Blog 2', 'Description of Blog 2')")
    c1.execute("INSERT INTO blog (owner_id, name, description) VALUES (3, 'Blog 3', 'Description of Blog 3')")
    c1.execute("INSERT INTO post (header, text, author_id, blog_id) VALUES ('Post 1', 'Text of Post 1', 1, 1)")
    c1.execute("INSERT INTO post (header, text, author_id, blog_id) VALUES ('Post 2', 'Text of Post 2', 2, 2)")
    c1.execute("INSERT INTO post (header, text, author_id, blog_id) VALUES ('Post 3', 'Text of Post 3', 3, 3)")
    c1.execute("INSERT INTO comments (owner_id, post_id, text) VALUES (1, 1, 'Comment text 1')")
    c1.execute("INSERT INTO comments (owner_id, post_id, text) VALUES (1, 2, 'Comment text 2')")
    c1.execute("INSERT INTO comments (owner_id, post_id, text) VALUES (1, 2, 'Comment text 3')")
    c1.execute("INSERT INTO comments (owner_id, post_id, text) VALUES (1, 2, 'Comment text 4')")
    c1.execute("INSERT INTO comments (owner_id, post_id, text) VALUES (1, 3, 'Comment text 5')")
    c1.execute("INSERT INTO comments (owner_id, post_id, text) VALUES (1, 3, 'Comment text 6')")
    c1.execute("INSERT INTO comments (owner_id, post_id, text) VALUES (3, 1, 'Comment text 7')")

    auth.commit()
    auth.close()

    logs = sqlite3.connect('logs.db')
    c2 = logs.cursor()

    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-03-25 08:00:00', 1, 1, 1)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-03-25 08:30:00', 1, 1, 1)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-03-25 09:00:00', 1, 1, 1)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-01-25 09:30:00', 1, 1, 5)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-01-25 10:00:00', 1, 1, 5)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-02-25 08:00:00', 1, 1, 5)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-02-25 08:30:00', 1, 1, 5)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-02-25 09:00:00', 1, 2, 3)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-01-25 09:30:00', 1, 2, 4)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-01-25 10:00:00', 1, 2, 3)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-01-25 10:00:00', 1, 3, 2)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-03-25 10:30:00', 2, 1, 1)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-03-25 11:00:00', 2, 1, 5)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-03-25 11:30:00', 2, 2, 4)")
    c2.execute("INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES ('2024-03-25 12:00:00', 2, 3, 2)")

    logs.commit()
    logs.close()
