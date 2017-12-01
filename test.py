import datetime

beg = datetime.datetime.now()

end = beg + datetime.timedelta(hours=3)

print((end - beg).seconds)