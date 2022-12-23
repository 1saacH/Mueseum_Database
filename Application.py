#Kenzie Fjestad UCID: 30140194
#Isaac Hus UCID: 30139733
#Elea Bahhadi UCID: 30150493
#Bruce Gillis UCID: 30143110

import mysql.connector as connector

print("connector is initilised at the top of the file, if the connection doesnt work,")
print("it probably means that the 'host' feild in the connector is not the same as your local sql instance.")
print(" Just go into the file and change the value. Its on line #8 of 'Application.py'.")
print()
mysql_password = input("Enter your mysql password to initialise connection: ")
con = connector.connect(user = 'root', password = mysql_password, host = '127.0.0.1', database = 'museumdatabase')


"""
This file handles the python side of the museum application. The sql initilisation is in the 'museumDatabase.sql' file
Run that file in a mysql workbench first before running this one. You might also have to update the 'host' as stated above. 

Your password will be requested before the program starts.
"""

def admin_menu():
    # DONE - fixed sql query, this function is complete
    while True:
        print()
        print('ADMIN MENU')
        print()
        print('what would you like to do?')
        print()
        print('1 -> add user')
        print('2 -> edit users')
        print('3 -> block user')
        print('4 -> enter database query')
        print('5 -> exit')
        print()
        choice = int(input("Choice(1,2,3,4,5): "))
        if choice == 1:
            print("Provide an ID, password and permision to add.")

            # input and check id
            while True:
                new_id = input('ID: ')
                if (len(new_id) != 4) or (not(new_id.isalnum())):
                    print('id must be a 4 digit number')
                    continue
                break

            # input and check password
            while True:
                new_password = input('Password: ')
                if (len(new_password) >= 20):
                    print('Password too long.')
                    continue
                break

            # input and check perm
            perms = ['admin', 'dataentry', 'enduser', 'blocked']
            while True:
                new_perm = input('Permision: ')
                if new_perm not in perms:
                    print('invalid permision')
                    print('Valid -> admin, dataentry, enduser, blocked')
                    continue
                break
            
            #make query
            entry = (new_id,new_password,new_perm)
            query = "INSERT INTO users (id, pass, permision) VALUES ( %s, %s, %s)"
            cs = con.cursor()
            cs.execute(query,entry)
            con.commit()
            cs.close()
            print("Added user successfuly.")
            
            
        elif choice == 2:
            #get inputs for updating user based on ID, have to set both perm and pass when updating, can be same as before though
            id = input('Provide an ID to edit: ')
            up_password = input('Provide a new password: ')
            perms = ['admin', 'dataentry', 'enduser', 'blocked']
            while True:
                up_perm = input('Permision: ')
                if up_perm not in perms:
                    print('invalid permision')
                    print('Valid -> admin, dataentry, enduser, blocked')
                    continue
                break
            text = "UPDATE users SET pass = %s, permision = %s WHERE id = %s"
            in_set = (up_password, up_perm, id)

            #make query
            curs = con.cursor()
            curs.execute(text,in_set)
            con.commit()
            curs.close()
            print("Update successful.")

        elif choice == 3:
            bl_id = input('Select ID to block: ')
            bl_text = "UPDATE users SET permision = 'blocked' WHERE id =%s"
            bl_in = [bl_id]
            #query
            cur = con.cursor()
            cur.execute(bl_text,bl_in)
            con.commit()
            cur.close()
            print('Block successful.')

        elif choice == 4:
            #select what type to determin if a 'commit' or print is nessesary
            print('What do you plan on doing:')
            print(' (1) Update or insert query')
            print(' (2) Select query')
            in_out = int(input('Choice(1,2): '))
            user_input = input('Enter your whole SQL query: ')

            # open cursor and exicute query
            crs = con.cursor(buffered = True)
            crs.execute(user_input)
            if in_out == 1:
                con.commit()
            
            #print query output
            if in_out == 2:
                for row in crs:
                    print()
                    for value in row:
                        print(value + " ", end = "")
            crs.close()
            print("Query successful.")

        elif choice == 5:
            print("Returning to main menu.")
            print()
            return
        else:
            print("not valid input")
            continue


        pass

def DE_menu():
    #NEEDS DOING
    # - fill in choices with appropriate code to do what it promises in the printed menu
    while True:
        print()
        print('ENTRY MENU')
        print()
        print('what would you like to do?')
        print()
        print('1 -> Lookup info')
        print('2 -> Insert data')
        print('3 -> Update data')
        print('4 -> Delete data')
        print('5 -> exit')
        print()

        choice = int(input("Choice 1,2,3,4,5: "))

        #id_no, Title, Origin, Epoch, Descript, Year_created, Artist_name, EName
        if choice == 1:
            print("By what criteria would you like to search?")
            print("1 -> Item ID number")
            print("2 -> Title of Piece")
            print("3 -> Origin")
            print("4 -> Epoch")
            print("5 -> Year Created")
            print("6 -> Artist Name")
            print("7 -> Exhibition Name")
            print("8 -> Style")
            print("9 -> back")
            search_choice = int(input("Choice 1, 2, 3, 4, 5, 6, 7, 8: "))

            while True:
                # search by id
                if search_choice == 1:
                    id_no = input("Item's ID number: ")
                    id_no = [id_no]

                    text = "SELECT * FROM ART_OBJECT WHERE id_no = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(id_no))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]

                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1

                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                #search by title
                elif search_choice == 2:
                    title = input("Item's Piece Title: ")
                    title = [title]

                    text = "SELECT * FROM ART_OBJECT WHERE Title = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(title))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]
                    
                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1

                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                #search by origin
                elif search_choice == 3:
                    origin = input("Item's Origin: ")
                    origin = [origin]

                    text = "SELECT * FROM ART_OBJECT WHERE origin = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(origin))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]
                    
                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1
                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                #search by epoch
                elif search_choice == 4:
                    epoch = input("Item's Epoch: ")
                    epoch = [epoch]

                    text = "SELECT * FROM ART_OBJECT WHERE epoch = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(epoch))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]
                    
                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1

                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                #search by year
                elif search_choice == 5:
                    year = input("Item's Year of Origin: ")
                    year = [year]

                    text = "SELECT * FROM ART_OBJECT WHERE year_created = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(year))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]
                    
                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1

                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                #search by artist
                elif search_choice == 6:
                    artist = input("Item's Artist: ")
                    artist = [artist]

                    text = "SELECT * FROM ART_OBJECT WHERE artist_name = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(artist))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]
                    
                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1

                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                #search by exhibition
                elif search_choice == 7:
                    exhi = input("Item's Exhibition: ")
                    exhi = [exhi]

                    text = "SELECT * FROM ART_OBJECT WHERE EName = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(exhi))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]
                    
                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1

                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                elif search_choice == 8:
                    style = input("Item's Style: ")
                    style = [style]

                    text = "SELECT * FROM ART_OBJECT WHERE Style = %s"

                    cur = con.cursor(buffered=True)
                    cur.execute(text,(style))
                    
                    thing_list = ["ID: ", "Title: ", "Origin: ", "Epoch: ", "Description: ", "Year Created: ", "Artist: ", "Exhibition Name: ", "Style: "]
                    
                    for row in cur:
                        print()
                        i = 0
                        for value in row:
                            print(thing_list[i] + value + "\n", end = "")
                            i += 1

                    cur.close()
                    input("\nPress Enter to Continue")
                    break
                elif search_choice == 9:
                    choice = 0
                    break
                else:
                    print("invalid input")

        elif choice == 2:
            co = con.cursor()
            insert_choice = input("Are you adding a piece by an artist that is already part of the database?(y/n): ")
            if insert_choice == "n":
                insert_artist = input("Artist name: ")
                insert_main_style = input("Main style: ")
                insert_artist_descr = input("Artist description: ")
                insert_artist_epoch = input("Artist Epoch: ")
                insert_artist_country = input("Artist Country: ")
                insert_artist_death = input("Date of Death: ")
                insert_artist_born = input("Date of Birth: ")

                insert_artist_text = "INSERT INTO artist VALUES (%s, %s, %s, %s, %s, %s, %s)"

                insert_artist_set = (insert_artist, insert_main_style, insert_artist_descr, insert_artist_epoch, insert_artist_country, insert_artist_death, insert_artist_born)

                co.execute(insert_artist_text, insert_artist_set)
            else: 
                insert_artist = input("Artist: ")

            insert_choice = input("Are you adding a piece that is part of an exhibition in the database?(y/n): ")
            if insert_choice == "n":
                insert_exh_name = input("Name of the Exhibition: ")
                insert_exh_start = input("Start date of exhibition: ")
                insert_exh_end = input("End date of the exhibition: ")

                insert_exh_text = "INSERT INTO exhibition VALUES (%s, %s, %s)"

                insert_exh_set = (insert_exh_name, insert_exh_start, insert_exh_end)

                co.execute(insert_exh_text, insert_exh_set)

            else:
                insert_exh_name = input("Name of the Exhibition: ")


            insert_id_no = input("ID number: ")
            insert_title = input("Title: ")
            insert_origin = input("Place of Origin: ")
            insert_epoch = input("Epoch: ")
            insert_descri = input("Description: ")
            insert_year = input("Year Created: ")
            insert_style = input("Style: ")

            insert_text = "INSERT INTO art_object VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            insert_set = (insert_id_no, insert_title, insert_origin, insert_epoch, insert_descri, insert_year, insert_artist, insert_exh_name, insert_style)

            co.execute(insert_text, insert_set)

            insert_type = input("What type of piece (Painting, Sculpture, Other): ")

            #insert into painting table
            if insert_type.lower() == "painting":
                insert_paint_drawn = input("Material the Painting is on: ")
                insert_paint_type = input("Type of paint used: ")

                insert_paint_text = "INSERT INTO painting VALUES (%s, %s, %s)"

                insert_paint_set = (insert_id_no, insert_paint_drawn, insert_paint_type)

                co.execute(insert_paint_text, insert_paint_set)

            #insert into sculpture table
            elif insert_type.lower() == "sculpture":
                insert_sculp_weight = input("Weight of the Scultpture: ")
                insert_sculp_height = input("Height of the Sculpture: ")
                insert_sculp_mater = input("Material of the Sculpture: ")
                
                insert_sculp_text = "INSERT INTO sculpture VALUES (%s, %s, %s, %s)"

                insert_sculp_set = (insert_id_no, insert_sculp_weight, insert_sculp_height, insert_sculp_mater)

                co.execute(insert_sculp_text, insert_sculp_set)

            #insert into other table
            elif insert_type.lower() == "other":
                insert_other_type = input("The type of the item: ")

                insert_other_text = "INSERT INTO other VALUES (%s, %s)"

                insert_other_set = (insert_id_no, insert_other_type)

                co.execute(insert_other_text, insert_other_set)

            #incorrect input
            else:
                print("invalid input")

            insert_ours = input("Is the item borrowed?(y/n): ")

            if insert_ours == "y":
                insert_exh = input("Is the Item part a collection already in the database?(y/n): ")
                #insert entry into collection
                if (insert_exh == "n"):
                    insert_col_name = input("Name of the Collection: ")
                    insert_col_type = input("Type of Collection: ")
                    insert_col_desc = input("Collection Description: ")
                    insert_col_address = input("Collection Address: ")
                    insert_col_phone = input("Collection phone: ")
                    insert_col_contact = input("Collection Contact: ")

                    insert_col_text = "INSERT INTO collection VALUES (%s, %s, %s, %s, %s, %s)"

                    insert_col_set = (insert_col_name, insert_col_type, insert_col_desc, insert_col_address, insert_col_phone, insert_col_contact)

                    co.execute(insert_col_text, insert_col_set)

                elif insert_exh == "y":
                    insert_col_name = input("Name of the Collection: ")
                else:
                    print("invalid input")

                insert_bor_ret = input("Date item returned: ")
                insert_bor_got = input("Date item borrowed: ")

                insert_bor_text = "INSERT INTO borrowed VALUES (%s, %s, %s, %s)"

                insert_bor_set = (insert_bor_ret, insert_bor_got, insert_col_name, insert_id_no)

                co.execute(insert_bor_text, insert_bor_set)

            elif insert_ours == "n":
                insert_ours_cost = input("Cost of Item: ")
                insert_ours_acquired = input("Date Acquired: ")
                insert_ours_status = input("Current Status: ")

                insert_ours_text = "INSERT INTO permanent_collection VALUES (%s, %s, %s, %s)"

                insert_ours_set = (insert_ours_cost, insert_ours_acquired, insert_ours_status, insert_id_no)

                co.execute(insert_ours_text, insert_ours_set)

            else:
                print("invalid input")


            con.commit()
            co.close()
            
        elif choice == 3:
            update_id = input("Enter ID number of the art object you are editing: ")
            change_col = input("What about this art object are you updating: ")
            info = input("The new data should be: ")

            update_text = "UPDATE art_object SET " + change_col + " = %s WHERE id_no =%s"

            #query(change the variable name)
            f = con.cursor()
            f.execute(update_text,(info, update_id))
            con.commit()
            f.close()
        elif choice == 4:
            #NOTE: This Delete function is broken and crashes when it is executed. Unfortunatly we struggled with trigger statements which they are required to get this working properly
            id_to_drop = input("What's the id of the art piece you would like to drop: ")
            id_to_drop = [id_to_drop]
            text = "DELETE FROM ART_OBJECT WHERE id_no = %s"

            f = con.cursor()
            f.execute(text,(id_to_drop))
            con.commit()
            f.close()
        elif choice == 5:
            break
        else:
            print("Bad Input")


def end_menu():
    #DONE - done if else tree and print/query things
    while True:
        print()
        print('USER MENU')
        print()
        print('what would you like to do?')
        print()
        print('1 -> Art Pieces')
        print('2 -> Exhibitions')
        print('3 -> Collections')
        print('4 -> exit')
        print()

        choice = int(input("Choice 1,2,3,4: "))

        if choice == 1:
            #art pieces menu
            while True:
                print()
                print("Art Pieces Menu:")
                print()
                print('what would you like to do?')
                print()
                print("1 -> See all pieces")
                print("2 -> Paintings")
                print("3 -> Sculptures")
                print("4 -> Other")
                print("5 -> back")
                print()

                inner_choice = int(input("Choice 1,2,3,4,5: "))
                if inner_choice == 1:
                    # query data
                    cursr = con.cursor(buffered = True)
                    query = "SELECT * FROM art_object"
                    cursr.execute(query)

                    #print data
                    print("ID\t\tTitle\t\tOrigin\t\tEpoch\t\tDescript\t\tYear created\t\tArtist_name\t\tExhibition")
                    print("------------------------------------------------------------------------------------------------------------------------------------------")
                    for row in cursr:
                        print()
                        for value in row:
                            print(value + "\t\t", end = "")
                    cursr.close()
                elif inner_choice == 2:
                    # query data
                    cursr = con.cursor(buffered = True)
                    query = "SELECT * FROM art_object WHERE id_no IN (SELECT paint_id FROM painting)"
                    cursr.execute(query)

                    #print data
                    print("ID\t\tTitle\t\tOrigin\t\tEpoch\t\tDescript\t\tYear created\t\tArtist_name\t\tExhibition")
                    print("------------------------------------------------------------------------------------------------------------------------------------------")
                    for row in cursr:
                        print()
                        for value in row:
                            print(value + "\t\t", end = "")
                    cursr.close()
                elif inner_choice == 3:
                    # query data
                    cursr = con.cursor(buffered = True)
                    query = "SELECT * FROM art_object WHERE id_no IN (SELECT sculpt_id FROM sculpture)"
                    cursr.execute(query)

                    #print data
                    print("ID\t\tTitle\t\tOrigin\t\tEpoch\t\tDescript\t\tYear created\t\tArtist_name\t\tExhibition")
                    print("------------------------------------------------------------------------------------------------------------------------------------------")
                    for row in cursr:
                        print()
                        for value in row:
                            print(value + "\t\t", end = "")
                    cursr.close()
                elif inner_choice == 4:
                    # query data
                    cursr = con.cursor(buffered = True)
                    query = "SELECT * FROM art_object WHERE id_no IN (SELECT other_id FROM other)"
                    cursr.execute(query)

                    #print data
                    print("ID\t\tTitle\t\tOrigin\t\tEpoch\t\tDescript\t\tYear created\t\tArtist_name\t\tExhibition")
                    print("------------------------------------------------------------------------------------")
                    for row in cursr:
                        print()
                        for value in row:
                            print(value + "\t\t", end = "")
                    cursr.close()
                elif inner_choice == 5:
                    choice = 0
                    break
                else:
                    print("Bad Input")

        elif choice == 2:
            # Exibitions menu
            while True:
                print()
                print("Exibitions Menu:")
                print()
                print('what would you like to do?')
                print()
                print("1 -> See all Exhibitions")
                print("2 -> back")
                print()

                inner_choice = int(input("Choice 1,2: "))
                if inner_choice == 1:
                    # query data
                    cursr = con.cursor(buffered = True)
                    query = "SELECT * FROM exhibition"
                    cursr.execute(query)

                    #print data
                    print("Exhibition    End date    Start date")
                    print("-----------------------------------")
                    for row in cursr:
                        print()
                        for value in row:
                            print(value + "\t", end = "")
                    cursr.close()

                elif inner_choice == 2:
                    choice = 0
                    break
                else:
                    print("Bad Input")
        elif choice == 3:
            # Collections menu
            while True:
                print()
                print("Collections Menu:")
                print()
                print('what would you like to do?')
                print()
                print("1 -> See all Collections")
                print("2 -> back")
                print()

                inner_choice = int(input("Choice 1,2: "))
                if inner_choice == 1:
                    # query data
                    cursr = con.cursor(buffered = True)
                    query = "SELECT * FROM collection"
                    cursr.execute(query)

                    #print data
                    print("Name\t\tType\t\tDescript\t\tAddress\t\tPhone\t\tContact")
                    print("-----------------------------------------------------------------------------------------------------")
                    for row in cursr:
                        print()
                        for value in row:
                            print(value + "\t", end = "")
                    cursr.close()

                elif inner_choice == 2:
                    choice = 0
                    break
                else:
                    print("Bad Input")
        elif choice == 4:
            break
        else:
            print("Bad Input")


def main():
    print()
    print()
    print("----------------------------------------------------------------------------------------------")
    print("*this next section would not be printed in a real application, is for grader purpouses only*")
    print()
    print("-when asked for an id, if you type 'exit' you will close the program")
    print()
    print("-dummy id's and passwords are given below for testing purpouses")
    print()
    print('ID           Password            Permision')
    print('-------------------------------------------')
    print('1111         admin                  admin')
    print('2222         dataentry            dataentry')
    print('3333         enduser               enduser')
    print('4444         blocked               blocked')
    print()
    print()
    print('*end of added info*')
    print('-----------------------------------------------------------------------------------------------')
    print()
    print()


    while True: 
        #login by getting id and password, and doing a query
        # assumes that the login will be correct 
        id = input("ID: ")
        if id == "exit" or id == "quit":
            break
        password = input("Password: ")
        cs = con.cursor()
        get_permision = "SELECT permision FROM users WHERE id = %s AND pass = %s"
        entries = (id,password)
        cs.execute(get_permision,entries)

        perm = []
        for per in cs:
            perm.append(per[0])
        cs.close()
        permision = perm[0]
        
        # calls appropriate user menu based on permision from above
        if permision == "admin":
            print('Welcome admin. Login successful.')
            admin_menu()
        elif permision == "dataentry":
            print('Login successful.')
            DE_menu()
        elif permision == "enduser":
            print('Login successful.')
            end_menu()
        elif permision == 'blocked':
            print('Sorry, you have been blocked from access.')
            break
        else:
            continue
    print('Thanks for stopping by!')
    print()
    con.close()
    print('program ended successfully')

if __name__ == "__main__":
    main()