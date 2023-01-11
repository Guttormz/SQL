import sqlite3 as sq

import sys



def main():

    conn = sq.connect('personer.db')

    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS name (Fornavn TEXT, Etternavn TEXT, Epost TEXT, Telefon TEXT, Postnummer TEXT)')

    f = open("randoms.csv", "r")

    for line in f:

        c.execute('INSERT INTO name VALUES (?,?,?,?,?)', (line.split(',')))

    c.execute('DELETE FROM name WHERE Fornavn = "fname"')

    conn.commit()

    c.execute('SELECT * FROM name')

    conn.close()

main()