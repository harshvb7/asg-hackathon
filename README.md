
### Running the project locally

Install Docker

```
docker-compose -f project/local.yml up
```


### TODOs

[ ] Migrate the infrastructure to CDK

[ ] Use mysql instead of sqlite

[ ] Use RDS

[ ] Manage all secrets using secrets manager

[ ] Improve loose security groups

[ ] Improve lambda function with logs and failure callbacks

[ ] Build a cool application to load test

[ ] Add locust.io load tester

[ ] Add target tracking policy to asg to demonstrated scaling up with load test


### Note: Lambda function is located at project/lambda_function.py 