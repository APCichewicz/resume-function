import azure.functions as func
from azure.data.tables import TableServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    connection_string = "DefaultEndpointsProtocol=https;AccountName=crc-cosmosdb-account;AccountKey=P3ssVwRobBqyYTm1STedtMSA9JSXmcDavwDAzy9GbKtpcG6N72R9RNjtD4iGx4poAQ85kxudN1sqACDbfpHG2A==;TableEndpoint=https://crc-cosmosdb-account.table.cosmos.azure.com:443/;"
    table_client = TableServiceClient.from_connection_string(conn_str=connection_string).get_table_client(table_name="crc-cosmosdb-table")
    partition_key = "visits"
    row_key = "counter"
    entity = table_client.get_entity(partition_key=partition_key, row_key=row_key)
    count = entity["count"] + 1
    entity["count"] = count
    table_client.update_entity(entity=entity, mode="replace")
    return func.HttpResponse(f"{count}", status_code=200)