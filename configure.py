import boto3

AWS_ACCESS_KEY_ID     = "AKIAXYKJXPHUCJQ5T4NG"
AWS_SECRET_ACCESS_KEY = "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"

ec2 = boto3.resource(
      'ec2', 
      region_name='us-east-1',
      aws_access_key_id=AWS_ACCESS_KEY_ID, 
      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

ami_id = "ami-0e731c8a588258d0d"#ami-0e731c8a588258d0d (64-bit (x86), uefi-preferred) / ami-0bbebc09f0a12d4d9 (64-bit (Arm), uefi)

instance = ec2.create_instances(
           ImageId=ami_id,
           MinCount=1,
           MaxCount=1,
           InstanceType="t2.micro",
           TagSpecifications=[{'ResourceType':'instance',
                               'Tags': [{
                                'Key': 'Name',
                                'Value': 'WebTier' }]}])

response = ec2.run_instances(
    ImageId=ami_id,
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{
            'Key': 'Name',
            'Value': 'WebTier Worker'
        }]
    }]
)
