Title: Specify instance name in connectiong string (MSSQL)
Date: 2016-02-27 19:47
Category: MSSQL
Tags: mssql, sql, connection string

To connect to default SQL instance, provide just server DNS name (or IP address):
```csharp
string connectionString = @"Data Source=SERVER_NAME; Initial Catalog=DATABASE_NAME; User ID=; Password=";
```

To connect to specific SQL instance, provide instance name after server DNS name:
```csharp
string connectionString = @"Data Source=SERVER_NAME\INSTANCE_NAME; Initial Catalog=DATABASE_NAME; User ID=; Password=;
```
