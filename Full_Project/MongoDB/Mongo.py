from pymongo import MongoClient as Mongo


class Data:
    def __init__(self):
        """
		Connect To MongoDB
        :param ip: Ip to connect too
        :param port: Port for connection
        """
        # Use the URL in a file to connect.
        with open('./mongo_connect.txt', 'r') as file:
            data = file.read()
        try:
            self.client = Mongo(data)
        except:
            pass
        self.Database = self.client.movieDB
        # self.Collection1 = self.Database.






def Main():
    pass



if __name__ == "__main__":
    Main()