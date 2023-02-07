import os
from zipfile import ZipFile

# a small pice of code to scan all directories in a path and search for .zip files and extract them to a required path.

DIR_PATH_TO_SCAN = 'D:\\CURSOS\\17_PYTHON\\Python_3_Deep_Dive_Part_4_OOP_35_horas'
DIR_PATH_TO_SAVE = 'D:\\CURSOS\\17_PYTHON\\Python_3_Deep_Dive_Part_4_OOP_35_horas\\code'

def extract_data(path:str)->None:

    with ZipFile(path, 'r') as zip:
        zip.extractall(os.path.join(DIR_PATH_TO_SAVE,path.split('\\')[-1]))
        
        
def list_directory(path:str)->str:
    
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            if fichero.is_dir():
                list_directory(fichero.path)
            else:
                if fichero.name.endswith(".zip"):
                    extract_data(fichero.path)
                    
            

            
list_directory(DIR_PATH_TO_SCAN)