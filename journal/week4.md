# Week 4 — Postgres and RDS

### Made and connected RDS 

![RDS image](assets/week4/wk4-rds.png)

## Added bash scripts 

![bash scripts](assets/week4/wk4-bash.png)

## Added the DB driver

![DB driver](assets/week4/wk4-db-driver-install.png)

## Connected to the DB

![Connected to the DB](assets/week4/wk4-db-connect.png)

## Added lambdas

I used 2 lambdas in the end too (like Andrew's video) because Lambda started supporting python 3.9 after Andrew's video came out, and the postgres lambda layer only suports 3.8, which led to some experimentation to bug fix...! 

![lambdas](assets/week4/wk4-lambda.png)

## Creating activities

Note there's a bug in Andrew's implementation, as he has hard coded his user handle as "andrewbrown" in the start of all the backend functions. This happens to work on his videos, as the user name he's entering to cognito also has the handle "andrewbrown", but for anyone else it won't work due to the join on user handle! I fixed by passing the user through as props in the Front end and then sending in the form's json data. 

![Creating activities in the gui](assets/week4/wk4-create-activities1.png)

![Created activities show up in the DB](assets/week4/wk4-creating-activities2.png)
