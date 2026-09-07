import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="GetResumeCounter")
@app.cosmos_db_input(
    "documents",
    "CosmosDbConnectionString",
    database_name="AzureResume",
    container_name="Counter",
    id="1",
    partition_key="1"
)
@app.cosmos_db_output(
    "updatedDocument",
    "CosmosDbConnectionString",
    database_name="AzureResume",
    container_name="Counter"
)
def GetResumeCounter(req: func.HttpRequest, documents: func.DocumentList, updatedDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Richiesta HTTP ricevuta per l\'aggiornamento del contatore.')

    if not documents:
        count = 1
    else:
        count = documents[0]['count'] + 1

    doc_to_save = {
        "id": "1",
        "count": count
    }
    
    updatedDocument.set(func.Document.from_dict(doc_to_save))

    return func.HttpResponse(
        json.dumps({"count": count}),
        status_code=200,
        mimetype="application/json",
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )