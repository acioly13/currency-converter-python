import pytest

@pytest.mark.asyncio
async def test_convert_and_list_transactions(client):
    payload = {
        "user_id": 1,
        "from_currency": "USD",
        "to_currency": "BRL",
        "amount": 100
    }

    # Chama a rota /convert
    response = await client.post("/convert", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 1
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "BRL"

    # Busca no /transactions
    response = await client.get("/transactions?userId=1")
    assert response.status_code == 200
    transactions = response.json()
    assert len(transactions) > 0
    assert transactions[-1]["from_value"] == 100
