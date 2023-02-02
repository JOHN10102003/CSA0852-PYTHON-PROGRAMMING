month=(input("enter the month:")) 
 date=int(input("enter the date:")) 
 if ((month == 'Mar') and (date > 19)) or (month == 'Apr') or (month == 'May') or ((month =='Jun') and (date< 20)): 
     print("SUMMER") 
 elif ((month == 'Jun') and (date > 20)) or (month == 'Jul') or (month == 'Aug') or ((month =='Sep') and (date< 21)): 
     print("SPRING") 
 elif ((month == 'SEP') and (date > 21)) or (month == 'Oct') or (month == 'Nov') or ((month =='Dec') and (date < 20)): 
     print("FALL") 
 elif ((month == 'Dec') and (date > 20)) or (month == 'Jan') or (month == 'Feb') or ((month =='Mar') and (date < 19)): 
     print("WINTER") 
 else: 
     print("enter vaild input")
