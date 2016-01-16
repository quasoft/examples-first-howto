Title: Install Open Trip Planner 0.11.x under Debian 7.4
Date: 2016-01-16 12:15
Category: Java
Tags: open trip planner, java, debian

First, install Git, Java 1.7 and Maven:

```bash
apt-get update
apt-get install git
apt-get install openjdk-7-jre
apt-get install maven
```

Next, install Open Trip Planner 0.11.x and build package.

```bash
cd /opt
git clone https://github.com/opentripplanner/OpenTripPlanner
cd OpenTripPlanner
git checkout 0.11.x
```

Next, increase maven memory limits and build application:

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
java -Xmx768m -jar otp-core/target/otp.jar --build /var/otp/graphs/sample
```

Start server:
```bash
java -Xmx768m -jar otp-core/target/otp.jar --server --port 8080 --router sample --graphs /var/otp/graphs/
```

Open your your trip planner with web browser: http://localhost:8080
