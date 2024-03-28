import sqlite3
import csv
from sys import argv, exit

if __name__ == "__main__":
    user_login = argv[1] if len(argv) > 1 else " ";
    conn1 = sqlite3.connect('authors.db')
    c1 = conn1.cursor()

    conn2 = sqlite3.connect('logs.db')
    c2 = conn2.cursor()

    c1.execute('''SELECT id FROM users WHERE users.login = ?''',(user_login,))
    user_id = c1.fetchall()
    if not(user_id):print("User wasn't found")
    else:
        c2.execute('''
                SELECT DATE(logs.datetime) AS log_date,
                COUNT(CASE WHEN logs.event_type_id = 1 THEN 1 END) AS login_count,
                COUNT(CASE WHEN logs.event_type_id = 5 THEN 1 END) AS logout_count,
                COUNT(CASE WHEN logs.space_type_id = 2 THEN 1 END) AS blog_count
                FROM logs
                WHERE logs.user_id = ?
                GROUP BY log_date''', (user_id[0][0],))
        general_data = c2.fetchall()
        c1.execute('''
                SELECT ?, post.header, users.login, COUNT(comments.id)
                FROM comments
                INNER JOIN post ON comments.post_id = post.id
                INNER JOIN users ON post.author_id = users.id
                WHERE comments.owner_id=?
                GROUP BY post.header''', (user_login, user_id[0][0]))
        comments_data = c1.fetchall()

        with open('comments.csv', 'w', newline='') as comments_csv:
            csv_writer = csv.writer(comments_csv)
            csv_writer.writerow(['User Login', 'Post Header', 'Author Login', 'Comment Count'])
            csv_writer.writerows(comments_data)

        with open('general.csv', 'w', newline='') as general_csv:
            csv_writer = csv.writer(general_csv)
            csv_writer.writerow(['Date', 'Login Count', 'Logout Count', 'Blog Action Count'])
            csv_writer.writerows(general_data)

    conn1.close()
    conn2.close()