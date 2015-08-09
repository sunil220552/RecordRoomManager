import dabase_manager
import logger
import previlagoues
import report
import statistics
import credentials

class RecordRoomManager:
   """ This class does the job of record room manager.
   Keeps track files in the record room, add/edit file 
   imformation, take backup of the information and etc.
   """
        
   def __init__():
       _dbm = dabase_manager.DabaseManager()
       _log = logger.Logger()

   def authenticate_user( cred ):
       """ This method is responsible for authenticating user into
       the services of record room manager.

       cred  : Credentials of user to be authenticated ( credentials.Credentials )

       return value : Instance of previlagoues.Previlagoues contining info about previlagoues of the user.
       """
       prev = previlagoues.Previlagoues()
       return prev

   def add_user(cred, prev )
       """ This method is responsible for adding new user to the 
       record room. 

       cred : Credentials of user to be added ( credentials.Credentials )
       prev : Previlagoues of user to be added ( previlagoues.Previlagoues )

       return value : True, if user is added successfully. Else Flase.
       """ 

       return True/False

   def add_file_details( file_details ):
       """ This method is responsible for adding new file to the database.

       file_details : Instance of file_details.FileDetails containg info about file to be added.

       return value : True, if file was added successfully. Else False.
       """

       return True/False

   def add_file_details( file_details ):
       """ This method is responsible for adding new file to the database.

       file_details : Instance of file_details.FileDetails containg info about file to be added.

       return value : True, if file was added successfully. Else False.
       """

       return True/False

   def fetch_file_details( rr_query ):
       """ This method is responsible for quering any information about the file.

       rr_query : Instance of record_query.RecordQuery, containg information about record to be queried
 
       return value : Instance of report.Report containg info about doc queried. 
       """ 
       rep = report.Report()
       return rep

   def rr_statistics():
       """ This method is responsible for generating stats about the record room.

       return value : Instance of statistics.Statistics() containg info about record room stats.
       """
       rr_stats = statistics.Statistics()
       return rr_stats

   def backup_db(backup_path):
       return True/False

   def merge_db(from, to):
       return True/False
