Title: Put memory used as custom CloudWatch metric data
Date: 2017-02-12 00:40
Category: AWS/CloudWatch
Tags: aws, cloudwatch, memory, used, custom, metric, data

Examples:
---------

```bash
memused=`free | awk 'NR==2{printf "%s", $3}'`
instanceid=`wget -q -O - http://169.254.169.254/latest/meta-data/instance-id`
timez=`date --utc +%FT%TZ`
aws cloudwatch put-metric-data --metric-name MemoryConsumption --namespace Custom --timestamp "$timez" --value "$memused" --unit Bytes --dimensions "InstanceId=$instanceid"

```
