import sqlite3 as sq
import pandas as pn

def main():
    conn = sq.connect('personer.db')#connect to database
    c = conn.cursor()#create cursor
    data = pn.read_csv('randoms.csv')#read csv file
    data.to_sql('kunder', conn, if_exists='replace', index=False)#write to database
    conn.commit()#commit changes
    print(c.fetchall())#print all rows
    postnummer()#call postnummer function
    conn.close()#close connection

def postnummer():#function to create table and write to database
    conn = sq.connect('personer.db')#connect to database
    c = conn.cursor()#create cursor
    data = pn.read_excel('Postnummerregister-Excel.xlsx')#read excel file
    data.to_sql('postnummer', conn, if_exists='replace', index=False)#write to database
    print(c.fetchall())#print all rows
    conn.close()#close connection
 

if __name__ == '__main__':# call main function
    main()