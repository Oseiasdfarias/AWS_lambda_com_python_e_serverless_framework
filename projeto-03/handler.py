import boto3
from datetime import datetime
from dateutil import relativedelta

from app import enviar_mendagem_telegram


sessao = boto3.Session()
cliente_ce = sessao.client("ce")


def get_cost(event, context):

    hoje = datetime.today()
    data_inicial = hoje.strftime("%Y-%m-01")

    mes_seguinte = hoje + relativedelta.relativedelta(months=1)
    data_final = mes_seguinte.strftime("%Y-%m-01")

    resposta = cliente_ce.get_cost_and_usage(
        TimePeriod={
            "Start": data_inicial,
            "End": data_final
        },
        Granularity="MONTHLY",
        Metrics=[
            "AmortizedCost"
        ]
    )
    valor = (resposta["ResultsByTime"][0]
             ["Total"]["AmortizedCost"]["Amount"])
    valor = round(float(valor), 2)

    mensagem = f"O custo da AWS no período [{data_inicial} : {data_final}] foi de R$ {valor}."  # noqa E501
    enviar_mendagem_telegram(mensagem=mensagem)

    return {
        "statusCode": 200
    }
