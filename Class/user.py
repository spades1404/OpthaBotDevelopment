from Database.firebase import Database

class User():
    def __init__(self,usern):

        dict = usern.to_dict()

        self.id = usern.id
        self.username = dict["username"]
        self.fname = dict["fname"]
        self.lname = dict["lname"]
        #self.admin = bool(dict["admin_priv"])



        return
