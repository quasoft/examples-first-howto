Title: Create IAM policy to allow putting custom metric data to CloudWatch
Date: 2017-02-12 01:07
Category: AWS/CloudWatch
Tags: aws, iam, policy, cloudwatch, put, custom, metric, data

Examples:
---------

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1489270264000",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData",
                "cloudwatch:GetMetricStatistics"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```


