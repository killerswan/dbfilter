import sqlite3
from common import newpathrel


def create_sample_db():
    # connect to or create a new database
    conn = sqlite3.connect(newpathrel('sample.sqlite3'))

    # get a cursor to it
    cur = conn.cursor()

    # create a table
    cur.execute('''
            create table monkeys
            (name text, color text, favorite_food_to_steal text)
        ''')

    # add data to the table
    data = [
            ('kevin', 'blonde', 'pancakes'),
            ('natalie', 'brown', 'beef hoof'),
            ('natalie and kevin', 'brown', 'hamburgers at Hut\'s'),
            ('kevin c', 'purple', 'cherry-nut ice cream, with red cherries'),
        ]
    cur.executemany('insert into monkeys values (?,?,?)', data)

    # save these changes
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_sample_db()
