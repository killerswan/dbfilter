import csv
import sqlite3
from common import newpathrel


def db_conn():
    return sqlite3.connect(newpathrel('sample.sqlite3'))

def get_matching_rows(connection, text_pattern):
    '''
    Run a select statement searching for matches
    in any of three columns.

    Note the tuple which satisfies the ? fields
    should be a tuple even if there's only one ? field.
    There's syntax for using named fields instead of just '?':
    see here: https://www.sqlite.org/lang_expr.html.

    Also, where I have where clauses like "name glob ?",
    there are a variety of other ways to do
    that kind of pattern matching on a field:
    =, LIKE, GLOB, REGEXP, or MATCH.
    This just lets me use the * wildcard syntax.
    '''
    cur = connection.cursor()
    matching_rows = cur.execute('''
            select name, color, favorite_food_to_steal
            from monkeys
            where
                name glob ? or
                color glob ? or
                favorite_food_to_steal glob ?
            order by name
        ''', (text_pattern, text_pattern, text_pattern))

    return matching_rows


if __name__ == '__main__':
    conn = db_conn()

    with open('output.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')

        # write a header row
        writer.writerow([
                'name',
                'color',
                'favorite_food_to_steal'
            ])

        # write all the matches
        for row in get_matching_rows(conn, '*kevin*'):
            print row
            writer.writerow(row)

    

