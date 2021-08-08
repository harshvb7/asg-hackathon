from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3_deploy


class HackathonStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "myHackathonBucket", versioned=True, public_read_access=False)
        s3_deploy.BucketDeployment(
            self,
            sources=[s3_deploy.Source.asset('./project')],
            destination_bucket=bucket,
            id="bucketDeployment"
        )

        # The code that defines your stack goes here
