import boto3

# Initialize SNS client
sns = boto3.client('sns', region_name='us-east-1')

# Replace this with your actual Topic ARN from CloudFormation Outputs
topic_arn = 'arn:aws:sns:us-east-1:123456789012:PatientReportsTopic'

# Load report content
with open('../reports/sample_report.txt', 'r') as file:
    message = file.read()

# Publish to SNS
response = sns.publish(
    TopicArn=topic_arn,
    Message=message,
    Subject='New Patient Report'
)

print('Message ID:', response['MessageId'])
