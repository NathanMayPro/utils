import os
import sys


class DATA_HUB:
    def __init__(self, path_of_creation:str= ""):
        self.path_of_creation = path_of_creation
        self.dir_list = ["data_lake","data_warehouse","data_vault","data_mart","knowledge_base"]
        self.file_list = ["main.py","__init__.py","__main__.py","__version__.py","__author__.py","__license__.py","__doc__.py"]

    def init(
        path_of_creation:str= "",
        dir_list: list = ["data_lake","data_warehouse","data_vault","data_mart","knowledge_base"],
        file_list: list = ["main.py","__init__.py","__main__.py","__version__.py","__author__.py","__license__.py","__doc__.py"],
    ) -> bool:
        """ The goal of this function is to init a bunch of file
        that are useful for data stuff
        
        Args :
            
        Output :

        """
        # create complete path
        dir_list = [os.path.join(path_of_creation,dir) for dir in dir_list]
        file_list = [os.path.join(path_of_creation,file) for file in file_list]

        for dir in dir_list:
            os.mkdir(dir)

        for file in file_list:
            # Create a file
            os.system("touch "+file)
        
        return True
    
    def remove(
        element_to_remove:list = [],
    ) -> bool:
        """ The goal of this function is to remove a bunch of file
        that are useful for data stuff
        
        Args :
            
        Output :

        """
        
        for element in element_to_remove:
            os.system(f"rm {'-rf ' if element.count('.') == 0 else ''}"+element)
        
        return True
    
            