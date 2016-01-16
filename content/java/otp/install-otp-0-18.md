Title: Install Open Trip Planner 0.18.x under Debian 7.6
Date: 2016-01-16 12:45
Category: Java
Tags: open trip planner, java, debian

First, [install java 1.8.0/8.0 under Debian 7]({filename}../install-oracle-java-1-8-in-debian.md).
(If using older version of Open Trip Planner like 0.11.x, you will need Java 1.7/7.0 instead)

Next, install maven and git:

```bash
apt-get update
apt-get install git
apt-get install maven
```

Install Open Trip Planner 0.18:

```bash
cd /opt
git clone https://github.com/quasoft/OpenTripPlanner
cd OpenTripPlanner
git checkout 0.18.x
```

Increase maven memory limits and build application:

```bash
export MAVEN_OPTS="-Xmx2000m"
mvn clean package
```

If building seems too slow, try to skip tests:

```bash
mvn clean package –DskipTests
```

Next, download sample GTFS and map data and build Graph object:

```bash
mkdir -p /var/otp/graphs/sample && cd /var/otp/graphs/sample
wget "http://developer.trimet.org/schedule/gtfs.zip" -O trimet.gtfs.zip
wget http://osm-extracted-metros.s3.amazonaws.com/portland.osm.pbf
java -Xmx768m -jar target/otp-0.18.0.jar --build /var/otp/graphs/sample
```

Start server:
```bash
java -Xmx768m -jar target/otp-0.18.0.jar --router sample --graphs /var/otp/graphs/ --server --port 8080
```

Open your your trip planner with web browser: http://localhost:8080