from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class CdkS3DemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crea un bucket S3
        s3.Bucket(self, "MySecureBucket",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )

