from persiantools.jdatetime import JalaliDateTime

def jalaliToday():
    dt = JalaliDateTime.now()
    return dt.strftime("%Y/%m/%d")

if __name__ == '__main__':
    print(jalaliToday())