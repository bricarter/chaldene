import unittest
import sqlite3
import os

from chaldene.app import create_app


class BaseTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = create_app("testing")
        cls.client = cls.app.test_client()
        cls.test_data = { 
            1 : {
            "nonprofit_name": "zelena", 
            "item": "lamp",
            "quantity": 1
            }, 
            2 : {
            "nonprofit_name": "nachovy", 
            "item": "toothbrush",
            "quantity": 2
            }, 
            3 : { 
            "nonprofit_name": "cervene",   
            "item": "book",
            "quantity": 3
            }, 
            4 : {
            "nonprofit_name": "zluta", 
            "item": "blanket",
            "quantity": 4 
            },
            5 : {
            "nonprofit_name": "fialovy", 
            "item": "detergent",
            "quantity": 5 
            }
        }

        con = sqlite3.connect(cls.app.config["DATABASE"])
        cur = con.cursor()
        cur.executemany("INSERT INTO nonprofit (nonprofit_name) VALUES (:nonprofit_name);", [cls.test_data[1], cls.test_data[2], cls.test_data[3]])
        con.commit()

        cur.executemany("INSERT INTO resource (item, quantity) VALUES (:item, :quantity);", [cls.test_data[1], cls.test_data[2], cls.test_data[3]])
        con.commit()

        con.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.app.config["DATABASE"])
