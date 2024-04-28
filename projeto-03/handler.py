import boto3

sessao = boto3.Session(profile_name="auto-curso")
cliente_ce = sessao.client("ce")


def get_cost(event, context):

    resposta = cliente_ce.get_cost_and_usage(
        TimePeriod={
            "Start": "2024-03-01",
            "End": "2024-03-30"
        },
        Granularity="MONTHLY",
        Metrics=[
            "AmortizedCost"
        ]
    )
    print(resposta)

    return {
        "statusCode": 200
    }


get_cost({}, {})
