Title: Get instance ID of current instance from bash
Date: 2017-02-12 00:37
Category: AWS/Metadata
Tags: aws, metadata, instance-id, current, bash

Examples:
---------

```bash
instanceid=`wget -q -O - http://169.254.169.254/latest/meta-data/instance-id`
```
