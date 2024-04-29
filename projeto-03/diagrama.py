# diagram.py
from diagrams import Diagram
from diagrams.custom import Custom
from diagrams.aws.cost import Budgets as BG
from diagrams.aws.compute import Lambda as LB

with Diagram("Web Service", show=False):
    csv = Custom("Telegram", "./utils/telegram.png")
    BG("Cost Explorer") >> LB("Função Lambda") >> csv
