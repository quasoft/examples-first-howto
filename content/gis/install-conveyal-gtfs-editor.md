Title: Install conveyal GTFS editor.
Date: 2016-01-16 13:03
Category: GIS
Tags: gtfs, editor, conveyal

```bash
sudo apt-get install git zip
sudo apt-get install openjdk-7-jre
sudo apt-get install postgresql-9.1 postgresql-9.1-postgis
wget http://downloads.typesafe.com/releases/play-1.2.5.zip
unzip play-1.2.5.zip
sudo su postgres
createdb gtfs-editor 
psql gtfs-editor < /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
\q

sudo nano /etc/postgresql/9.1/main/pg_hba.conf

# "local" is for Unix domain socket connections only
local     all      all                      trust
# IPv4 local connections:
host      all      all      127.0.0.1/32    trust
# IPv6 local connections:
host      all      all      ::1/128         trust

sudo /etc/init.d/postgresql restart

cd ~/
git clone https://github.com/conveyal/gtfs-editor.git
cd gtfs-editor
cp conf/application.conf.template conf/application.conf
nano conf/application.conf

http.address=127.0.0.1
db.user=postgres
db.pass=?

/home/user/play-1.2.5/play run
```