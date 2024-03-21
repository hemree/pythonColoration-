import os 
from datetime import datetime, timedelta
from random import randint


today = datetime.today()


weekend_days = [5, 6]  

for i in range(1, 70):
    for j in range(0, randint(1, 5)):
      
        current_date = today - timedelta(days=i)
        
       
        if current_date.weekday() not in weekend_days:
            
            commit_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
            
          
            os.system('git add .')
            os.system('git commit --date="' + commit_date + '" -m "commit"')


os.system('git push -u origin main')
