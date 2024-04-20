# diagram.py
from diagrams import Diagram
from diagrams.custom import Custom
from diagrams.aws.storage import SimpleStorageServiceS3 as S3
from diagrams.aws.compute import Lambda as LB
from diagrams.aws.engagement import SimpleEmailServiceSes as SES

with Diagram("Web Service", show=False):
    csv = Custom("CSV", "./utils/csv.png")
    csv >> S3("Bucket S3") >> LB("Função Lambda") >> SES("SES")
