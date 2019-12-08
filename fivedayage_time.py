from datetime import datetime, timedelta

now = datetime.now()
fiveday = now -timedelta(days=5)

file_name = 'save_fivedayage_time_' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.text'

file = open(file_name,'w')
file.write(str(fiveday))
file.close()
