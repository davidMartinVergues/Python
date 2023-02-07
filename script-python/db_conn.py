import sys
#sys.path.append('C:\\Program Files\\Anaconda3\\lib\\site-packages\\psycopg2')
#'C:\\Program Files\\Anaconda3\\lib\\site-packages\\psycopg2'
import psycopg2
from psycopg2 import extras


conn = psycopg2.connect(host="XXXXX", 
                        port = XXXX, 
                        database="titulaciones", 
                        user="XXXXX",
                        password="XXXXX")
extras = extras
