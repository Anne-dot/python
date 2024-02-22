from datetime import datetime

dt = datetime.now()

f = open("/home/anne/kool/python/andruse_ylesanded/python/datetime.log", "a")

f.write(str(dt) + "\n")


# crontab - kas panna kasutaja v rooti jaoks?
# crontab -e -> edit
# 1 - nano <-easiest

# cron expression - märksõna
# https://www.digitalocean.com/community/tutorial-collections/how-to-use-cron-to-automate-tasks
# pwd  - present working directory - terminalis

# * * * * * python3 /home/anne/kool/python/andruse_ylesanded/python.timelog.py
# Ctrl + X
# sudo cron

# cron: can't lock /var/run/crond.pid, otherpid may be 183: Resource temporarily unavailable - 
# see oli oma koduarvutis
# nüüd vaja see panna Zone'i üles, et saaksin arvuti kinni panna ja see töötaks

# nano on terminali editor

#Zone'is
# anne@D0019:~$ ssh virt123071@ta23ruusmann.itmajakas.ee -i .ssh/id_rsa_zone
# mkdir ta23cron
# testisin, kas python3 on kirj > python3 > quit() -et kinni panna
# Kuidas fail sinna kausta - Githubi kaudu - nii väikesele scriptile liiga ajamahukas - teen uue faili ja kopeerin
# nano timelog.py

# perioodilised zone'i tööd crontab
# python3 /data01/virt123071/ta23cron/timelog.py

