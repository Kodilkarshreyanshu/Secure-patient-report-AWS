# Secure Patient Report Management using AWS

## 📌 Overview
This project demonstrates how to securely deliver patient reports using AWS services like EC2, SNS, and a custom VPC.

## 🏗️ Architecture
- Custom VPC created via AWS CloudFormation
- EC2 instance to simulate report hosting
- Amazon SNS for secure patient report delivery

## 🚀 Deployment Steps

1. Launch the CloudFormation stack using `cloudformation/vpc-sns-ec2.yaml`.
2. SSH into the EC2 instance and install Python + Boto3.
3. Run the `scripts/publish_report.py` script from your local or EC2 environment.
4. Subscribe an email endpoint to the SNS topic to receive the patient report.

## 🛠️ Tools Used
- AWS CloudFormation
- Amazon EC2
- Amazon SNS
- Python (boto3)

---

