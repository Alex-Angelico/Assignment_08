#------------------------------------------#
# Title: Assignmen08.py
# Desc: Version of CD Inventory program
# incorporating full class structure
# Change Log: (Who, When, What)
# Alex Angelico, 2020-08-31, created file
# Alex Angelico, 2020-09-01, added structured
# error handling
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    """
    def __init__(self, ID=None, title="...", artist="..."):
        self.__cd_id = ID
        self.__cd_title = title 
        self.__cd_artist = artist

    @property    
    def cd_id(self):
        return self.__cd_id
        
    @cd_id.setter
    def cd_id(self, t_ID):
        if str(t_ID).isalpha():
            raise Exception("Numeric value required for ID.")
        else:
            self.__cd_id = t_ID
        
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, t_tit):
        if str(t_tit).isnumeric():
            raise Exception("That doesn't sound like a track title.")
        else:
            self.__cd_title = t_tit
        
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, t_art):
        if str(t_art).isnumeric:
            raise Exception("That's doesn't sound like an artist name.")
        else:
            self.__cd_artist = t_art
    
    def __str__(self):
        return '{} | {} | {}'.format(self.__cd_id, self.__cd_title, self.__cd_artist)

# -- PROCESSING -- #
class DataProcessor:
    """Processes data within the runtime
    
    properties:
    
    methods:
        add_cd: processes user input values into a new CD object
        delete_cd processes user input ID values through current inventory table and deletes matches by cd_id attribute
    """
    @staticmethod
    def add_cd(addID, addtitle, addartist, table):
        """Converts user input data into a new CD object and appends to current inventory table
        
        Args:
            addID (string): numerical identification for the new CD
            addtitle (string): album title of the new CD
            addartist (string): artist name of the new CD
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime
        
        Returns:
            None.
        """
        newCD = CD(addID, addtitle, addartist)
        table.append(newCD)
        print()
        
    @staticmethod
    def delete_cd(delID, table):
        """Deletes CD objects by cd_id attribute from current inventory table
        
        Args:
            delID (list of strings): holds one or more ID values designated for deletiton
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime
            
        Returns:
            None.
        """
        remove_count = 0
        for row in delID: delID = row.strip().split(',')

        for _id in delID:
            try:
                _id = int(_id)
            except:
                print('"',_id,'"',' is not valid ID input. Removing from delete list and returning to main menu.', sep='')
                delID.remove(_id)
            pass
            for row in table:
                if row.cd_id == _id:
                    remove_count += 1
                    table.remove(row)

        if remove_count == 0: print('No matching IDs')
        else: print(f'{remove_count} total IDs removed out of {len(delID)}')
        
    
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): Saves 2D data structure in runtime to file
        load_inventory(file_name): Loads 2D data structure into runtime from file
    """
    @staticmethod
    def save_inventory(fileName, table):
        """Function to manage transcription of data from list of CD objects in
        current inventory to file
        
        Args:
            fileName (string): name of file used to wrtie the data to
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime
            
        Returns:
            None.
        """
        tempTbl = []
        FileIO.load_inventory(strFileName, tempTbl)
        
        try:
            if str(table) != str(tempTbl):
                objFile = open(fileName, 'w')
                for row in table:
                    lstValues = [row.cd_id, row.cd_title, row.cd_artist]
                    lstValues[0] = str(lstValues[0])
                    objFile.write(','.join(lstValues) + '\n')
                objFile.close()
        except:
            print('There are no new CDs in Inventory to save.')

    @staticmethod
    def load_inventory(fileName, table):
        """Function to manage data ingestion from file to a list of CD objects

        Reads the data from file identified by fileName into a 2D table
        (list of CD objects) table one line in the file represents one CD object row in table.

        Args:
            fileName (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()
        
        try:
            objFile = open(fileName, 'r')
        except(IOError):
                print('CD Inventory file not found. Creating now. Please restart program.')
                objFile = open(fileName, 'w+')
                objFile.close()
                sys.exit()
        
        for line in objFile:
            try:
                if line != {}: pass
            except(TypeError, ValueError):
                print('Corrupt or missing data.')
                sys.exit()
            data = line.strip().split(',')
            data[0] = int(data[0])
            inventoryCD = CD(data[0], data[1], data[2])
            table.append(inventoryCD)
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output
    
    properties:

    methods:
        print_menu(): Displays program options for user
        menu_choice(): Gets user input based on print_menu() choices
        show_inventory(table): Displays current inventory in runtime from list of CD objects
        add_cd_input(table): Gets user input for new CD entries
    """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[1] Load Inventory from file\n[2] Add CD to Inventory\n[3] Delete CD from Inventory')
        print('[4] Display Current Inventory\n[5] Save Inventory to file\n[6] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        options = ["1","2","3","4","5","6"]
        while True:
            choice = input('Which operation would you like to perform? [1, 2, 3, 4, 5, or 6]: ').strip()
            try:
                if options.count(choice) == 1: break
            except:
                continue
        print()
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime.

        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')
        
    def add_cd_input(table):
        """Gets user input for new CD information
        
        Args:
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime.
        
        Returns:
            ID (string): numerical identification for the new CD
            title (string): album title of the new CD
            artist (string): artist name of the new CD
        """
        used_ids = []
        for row in table:
            used_ids.append(row.cd_id)

        while True:
            ID = input('Enter numerical ID: ').strip()
            try:
                ID = int(ID)
                break
            except:
                continue
        
        while ID in used_ids:
            print('That ID already exists. Please enter a new ID.')
            while True:
                ID = input('Enter numerical ID: ').strip()
                try:
                    ID = int(ID)
                    break
                except:
                    continue

        while True:
            title = input('What is the CD\'s title? ').strip()
            try:
                if (len(title)) > 0: break
            except:
                continue
        
        while True:
            artist = input('What is the Artist\'s name? ').strip()
            try:
                if (len(artist)) > 0: break
            except:
                continue

        return ID, title, artist


# -- Main Body of Script -- #
import sys
FileIO.load_inventory(strFileName, lstOfCDObjects)

while True:
    IO.print_menu()
    menuChoice = IO.menu_choice()
    
    if menuChoice == "6":
        break

    if menuChoice == "1":
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        overwrite_verification = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled.\n')
        if overwrite_verification.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue
    
    elif menuChoice == "2":
        print("Please provide new CD info.")
        
        add_verification = 'y'
        while add_verification == 'y':
            newID, newTitle, newArtist = IO.add_cd_input(lstOfCDObjects)

            print('\nYou entered:')
            print('ID\tCD Title (by: Artist)')
            print(f'{newID}\t{newTitle} (by:{newArtist})\n')
            input_validation = input("Is this information correct? [y/n]: ").lower()
            if input_validation == "y":
                pass
            elif input_validation == "n":
                continue
            DataProcessor.add_cd(newID, newTitle, newArtist, lstOfCDObjects)
            while True:
                add_verification = input('Would you like to add another CD? [y/n] ').lower()
                try:
                    if add_verification == 'y': break
                    elif add_verification == 'n': break
                except:
                    continue
        continue
        
    elif menuChoice == "3":
        IO.show_inventory(lstOfCDObjects)

        while True:
            cdIDdel = [input('Enter one or more IDs to delete, separated by commas (example: "1,2,3"): ').strip()]
            try:
                if cdIDdel != ['']: break
            except:
                continue
            
        DataProcessor.delete_cd(cdIDdel, lstOfCDObjects)
        continue

    elif menuChoice == "4":
        IO.show_inventory(lstOfCDObjects)
        continue
    
    elif menuChoice == "5":
        
        while True:
            save_verification = input('Save current inventory to file? [y/n] ').strip().lower()
            try:
                if save_verification == 'y':
                    FileIO.save_inventory(strFileName, lstOfCDObjects)
                    break
                elif save_verification == 'n':
                    input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
                    break
            except:
                continue
        continue
    
    else:
        print("Error.")