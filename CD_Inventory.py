#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# RBengu,     2021-Aug-28, filled in pseudocode to complete assignment 08
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    
    def __init__(self, cd_id, cd_title, cd_artist):
        self.id = cd_id
        self.title = cd_title
        self.artist = cd_artist
        
    @property
    def cd_id(self):
        return self.id
    
    @property
    def cd_title(self):
        return self.title
    
    @property
    def cd_artist(self):
        return self.artist
    
    @cd_id.setter
    def cd_id(self, value):
        self.id = value   
        
    @cd_title.setter
    def cd_title(self, value):
        self.id = value 
        
    @cd_artist.setter
    def cd_artist(self, value):
        self.artist = value
        
    def __str__(self):     
        return (str(self.cd_id) + ',' +  self.cd_title + ',' +  self.cd_artist )


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """  
    @staticmethod
    def load_inventory(file_name):
        """
        Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list): data structure (list) that holds the data during runtime

        Returns:
            table (list of dict): 2d data structure (list of dicts) that holds the data during runtime
            
        """
        
        try:
            with open(file_name, 'rb') as objFile:
                list = pickle.load(objFile)
            return list
        
        except FileNotFoundError as e:
            print('Data file does not exist!')
            print('Built in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """
        Writes data from list of dictionaries to file
        
        Args:
            file_name (string): name of file to save data to
            
            lst_Inventory (list): data structure (list) that holds the data during runtime
            
        Returns:
            None
        """
        
        with open(file_name, 'wb') as objFile:
            pickle.dump(lst_Inventory, objFile)
        objFile.close()


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handles Input/Output with user"""    

    @staticmethod
    def print_menu():
        """
        Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """
        Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(list):
        """
        Displays current inventory table


        Args:
            list (list of elements): data structure that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for obj in list:
            print('{}\t{} (by:{})'.format( obj.cd_id, obj.cd_title, obj.cd_artist))
        print('======================================')
        
    @staticmethod
    def new_entry():
        """
        Asks the user to enter details for their new entry, and adds it to memory
        
        Args:
            None.
        
        Returns:
            ID (string): ID of new entry
            
            Title (string): Title of new entry
            
            Artist(string): Artist of new entry
        """
        
        ID = int(input('Enter ID: ').strip())
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        
        lstOfCDObjects.append( CD(ID, title, artist))

# -- Main Body of Script -- #
while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # Process menu selection
    # Process exit first
    if strChoice == 'x':
        break
    # Process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # Process add a CD
    elif strChoice == 'a':
        
        # Ask user for new ID, CD Title and Artist and adds to list
        IO.new_entry()
        continue  # start loop back at top.
    
    # Process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # Process save inventory to file
    elif strChoice == 's':
        
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        # Process choice
        if strYesNo == 'y':
            # Save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            pass
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # Catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




