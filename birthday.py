import datetime
birthday = input("Qual eh a data do seu aniversario ")
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
print  ("Your birthday is " + birthdate.strftime('%B'))
