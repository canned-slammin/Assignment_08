#----------------------------------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# SBurner, 2020-12-01, built out pseudocode for Assigment 08
#----------------------------------------------------------------------#

# -- MODULES -- #
import pickle

# -- DATA -- #
strFileName = 'cdInventory.dat'
strTextFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __incrementCount: adds 1 to number of CDs
        cdInfo: concatenates properties into a string
        __str__: returns cdInfo
    """
    # -- Fields -- #
    __numCDs = 0
    
    # -- Constructor -- #
    def __init__(self,intID,strTitle,strArtist):
        # -- Attributes -- #
        self.__cd_id = intID
        self.__cd_title = strTitle
        self.__cd_artist = strArtist
    
    # -- Properties -- #
    
    @property
    def cd_id(self):
        return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title.title()
    
    @property
    def cd_artist(self):
        return self.__cd_artist.title()
    
    @cd_id.setter
    def cd_id(self,value):
        if isinstance(value,int):
            self.__cd_id = value
        else:
            raise Exception("CD ID must be an integer")
            
    @cd_title.setter
    def cd_title(self,value):
        if isinstance(str,value):
            self.__cd_title
        else:
            raise Exception("CD Title must be a string")
            
    @cd_artist.setter
    def cd_artist(self,value):
        if isinstance(str,value):
            self.__cd_artist = value
        else:
            raise Exception("CD Artist must be a string")
    
    # -- Method -- #
    @staticmethod
    def __incrementCount():
        CD.__numCDs += 1
 
    def dicCD(self):
        dicCD = {"ID":self.__cd_id,"Title":self.__cd_title,"Artist":self.cd_artist}
        return dicCD
        
    def lstCD(self):
        lstCD = [str(self.__cd_id),self.__cd_title,self.__cd_artist]
        return lstCD 
    
    def __str__(self):
        return ', '.join(self.lstCD())

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # -- Fields -- #
    # -- Constructor -- #
        # -- Attributes -- #
    # -- Properties -- #
    # -- Method -- #
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """
        Method for saving inventory to a binary file.

        Parameters
        ----------
        file_name : string
            Name of .dat file to save to
        lst_Inventory : list
            List of CD objects to save to file

        Returns
        -------
        None.

    """
        
        try:
            with open(file_name,'wb') as objFile:
                pickle.dump(lst_Inventory,objFile)
                print("Inventory Saved!")
        except Exception as e:
            print(e)
            print('Inventory Not Saved')
            
    @staticmethod
    def load_inventory(file_name):
        """
        Method to load previously saved inventory from a binary file.

        Parameters
        ----------
        file_name : string
            name of binary file to laod data from

        Returns
        -------
        lst_Inventory : list
            list of CD objects to load from file

        """
        try:
            with open(file_name,'rb') as objFile:
                lst_Inventory = pickle.load(objFile)
            print('Inventory Loaded')
            return lst_Inventory
        except FileNotFoundError:
            print('Inventory File Not Found')
            print('Continuing With Program')
            lst_Inventory = []
            return lst_Inventory
        except Exception as e:
            print(e)
            print('Error, file not loaded')
            lst_Inventory = []
            return lst_Inventory
        
    @staticmethod
    def export_inventory(file_name,lst_inventory):
        """
        Method to export inventory as a human-readable file.

        Parameters
        ----------
        file_name : string
            file name of destination
        lst_inventory : list
            list of CD objects invetory

        Returns
        -------
        None.

        """
        try:
            with open(file_name,'w') as objFile:
                for row in lst_inventory:
                    strCD = str(row.cd_id) + ': ' + row.cd_title + ' (by: ' + row.cd_artist + ')\n'
                    objFile.write(strCD)
            print("Inventory exported as:",strTextFileName)
        except Exception as e:
            print(e)
            print('File Did Not Export')
            
class DataProcess:
    """
    Class to process data held in inventory.
    
    properties: None.
    
    Methods: 
        add_CD: Method to add a CD object to the inventory table
        del_CD: Method to remove a CD object from the inventory table
    """
    
    @staticmethod
    def add_cd(lstInput,table):
        """
        Method to add a CD object to the table.

        Parameters
        ----------
        lstInput : list
            list of inputs from collect_data function
        table : list
            list of CD objects

        Returns
        -------
        None.

        """
        if lstInput != None:
            cdID = lstInput[0]
            cdTitle = lstInput[1]
            cdArtist = lstInput[2]
            objCD = CD(cdID,cdTitle,cdArtist)
            table.append(objCD)
        
    def del_cd(table):
        """
        Method for deleting CD objects from inventory

        Parameters
        ----------
        table : list
           List of CD objects.

        Returns
        -------
        None.

        """
        try:
            # ask user which ID to remove
            intIDDel = int(input('Which ID would you like to delete? ').strip())
            # search thru table and delete CD
            intRowNr = -1
            blnCDRemoved = False
            for row in table:
                intRowNr += 1
                if row.cd_id == intIDDel:
                    del table[intRowNr]
                    blnCDRemoved = True
                    break
                if blnCDRemoved:
                    print('The CD was removed')
                if blnCDRemoved == False:
                    pass
                else:
                    print('Could not find this CD!')
        except ValueError:
            input('Invalid input, ID must be a number. Press [ENTER] to continue')
        
    
# -- PRESENTATION (Input/Output) -- #
class IO:
    """
    Class to present functionality to user.
    
    Methods:
        print_menu: Method to display user options
        menu_choice: Method to collect user input and return from a defined list of options
        display_inventory: Method to display inventory in a formatted table
        collect_input: Method to collect user input and return in a list format
        
    """
    
    @staticmethod
    def print_menu():
        """
        Method to display user options.

        Returns
        -------
        None.

        """
        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to Memory')
        print('[p] Export Current Inventory to Text File\n[x] Exit\n')
    
    @staticmethod
    def menu_choice():
        """
        Method to collect user input and return from a defined list of options

        Returns
        -------
        choice : TYPE
            DESCRIPTION.

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's','p', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s, p, or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def display_inventory(table):
        """
        Method to display inventory as a formatted tabe

        Parameters
        ----------
        table : List
            A 2D list of CD objects formatted as dictionaries

        Returns
        -------
        None.

        """
        print('===========CURRENT INVENTORY===========')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(row.cd_id,row.cd_title,row.cd_artist))      
        print('=======================================')
        
    
    @staticmethod
    def collect_info():
        """
        Method to collect user input and return in a list format

        Returns
        -------
        lstInput : list
            List of user inputs to be used to create a new CD object 

        """
        try:
            intID = int(input("Enter CD ID: "))
            strTitle = input("Enter CD Title: ")
            strArtist = input("Enter CD Artist: ")
            lstInput = [intID,strTitle,strArtist]
            return lstInput
        except ValueError:
            input('CD ID Must be an Integer. Press [ENTER] to Continue')
        

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)
# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # let user load inventory from file  
    if strChoice == 'l':
        print('NOTE: Loading inventory from file will overwrite existing inventory.')
        loadChoice = input('Enter Y to proceed, N to cancel: ').strip().lower()
        if loadChoice == 'y':
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.display_inventory(lstOfCDObjects)
            continue
        elif loadChoice == 'n':
            print('File not loaded, returning to menu')
            continue
        else:
            print('Invalid Input')
            continue
    # let user add data to the inventory
    if strChoice == 'a':
        DataProcess.add_cd(IO.collect_info(), lstOfCDObjects)
        IO.display_inventory(lstOfCDObjects)
        continue
    # show user current inventory
    if strChoice == 'i':
        IO.display_inventory(lstOfCDObjects)
        continue
    # let user delete file from inventory
    if strChoice == 'd':
        DataProcess.del_cd(lstOfCDObjects)
        IO.display_inventory(lstOfCDObjects)
        continue
    # let user save inventory to file
    if strChoice == 's':
        FileIO.save_inventory(strFileName, lstOfCDObjects)
        continue
    # let user export inventory to a text file
    if strChoice == 'p':
        FileIO.export_inventory(strTextFileName, lstOfCDObjects)
        continue
    # let user exit program
    if strChoice == 'x':
        print("Exiting Program")
        break
    # general error handling
    else:
        print('General Error')
