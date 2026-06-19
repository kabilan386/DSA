# CloudFormation
import json
import yaml

# A basic CloudFormation template
cloudformation_template = """
AWSTemplateFormatVersion: '2010-09-09'
Description: 'A basic AWS CloudFormation template creating an S3 bucket'

Resources:
  MyS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub '${AWS::StackName}-my-basic-bucket-${AWS::AccountId}'

Outputs:
  BucketName:
    Description: 'Name of the newly created S3 bucket'
    Value: !Ref MyS3Bucket
  BucketArn:
    Description: 'ARN of the newly created S3 bucket'
    Value: !GetAtt MyS3Bucket.Arn
"""

def generate_template(filename="basic_template.yaml"):
    with open(filename, "w") as f:
        f.write(cloudformation_template.strip())
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    generate_template()