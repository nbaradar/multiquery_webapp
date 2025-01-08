from pymongo.collection import Collection
from datetime import datetime

async def save_query_result(
    collection: Collection, 
    prompt: str, 
    responses: dict
):
    """
    Save the query result to the MongoDB collection.

    :param collection: The MongoDB collection to save the result to.
    :param prompt: The user's query.
    :param responses: The responses from the language model providers.
    """
    document = {
        "query": prompt,
        "responses": responses,
        "timestamp": datetime.utcnow()
    }
    result = await collection.insert_one(document)
    return str(result.inserted_id)
