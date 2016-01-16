Title: Install Oracle Java 1.8.0/8.0 under Debian 7
Date: 2016-01-16 11:56
Category: Java
Tags: java, oracle, debian, ubuntu

```bash
cd ~/
wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-i586.tar.gz
mkdir /opt/jdk
tar -zxf ~/jdk-8u51-linux-i586.tar.gz -C /opt/jdk
update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_51/bin/java 100
update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_51/bin/javac 100
update-alternatives --config java
echo export "JAVA_HOME=/opt/jdk/jdk1.8.0_51/" >> ~/.bash_profile
```