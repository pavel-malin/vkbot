from datetime import *
from dateutil.relativedelta import relativedelta



def good_pasport(date_of_birth, pass_date):
    date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
    pass_date = datetime.strptime(pass_date, '%Y-%m-%d')

    now_date = datetime.now()

    if now_date < date_of_birth + relativedelta(years=+20) + relativedelta(months=+1):
        return True
    elif ((now_date > date_of_birth + relativedelta(years=+20) + relativedelta(months=+1)) and
          (now_date < date_of_birth + relativedelta(years=+45) + relativedelta(months=+1))):
        if pass_date > date_of_birth + relativedelta(years=+20):
            return True
    elif now_date > date_of_birth + relativedelta(years=+45) + relativedelta(months=+1):
        if pass_date > date_of_birth + relativedelta(years=+45):
            return True

    else:
        return False


print(good_pasport('2006-02-10', '2018-03-14'))
