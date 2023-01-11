#Imports sqlite3 module, and changes the name needed to use it from sqlite3 to sq
import sqlite3 as sq

#Creates a new function called main
def main():
    
    #Connects to the database named "personer.db".
    conn = sq.connect('personer.db')
    
    #Makes it possible to edit what you have connected "conn" to.
    c = conn.cursor()
    
    #Executes a code that will make 5 new colummns named Fornavn, Etternavn, Epost, Telefon and Postnummer as text files.
    c.execute('CREATE TABLE IF NOT EXISTS name (Fornavn TEXT, Etternavn TEXT, Epost TEXT, Telefon TEXT, Postnummer TEXT)')
    
    #Opens the randoms document for reading.
    f = open("randoms.csv", "r")
    
    #For each line in the document, it starts the code in the line under
    for line in f:
        
        #Starts a code that inserts the text from the "randoms" document into the database. And for each time there is a "," it jumps to the next colummn.
        c.execute('INSERT INTO name VALUES (?,?,?,?,?)', (line.split(',')))
        
    #Deletes the row in the database where Fornavn is named "fname".
    c.execute('DELETE FROM name WHERE Fornavn = "fname"')
    
    #Saves information done to the database
    conn.commit()
    
    #Stops the cursor from working, so can't edit database anymore
    conn.close()

#Runs the function called main
main()
