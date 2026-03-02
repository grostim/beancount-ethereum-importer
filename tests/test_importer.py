import os
import json
import pytest
import datetime
from decimal import Decimal

from beancount.core.number import D
from beancount_ethereum.importer import Importer

@pytest.fixture
def config_path(tmp_path):
    config = {
        "name": "ethereum_test",
        "account_map": {
            "0x1234567890123456789012345678901234567890": "Assets:Crypto:ETH"
        },
        "fee_account": "Expenses:Crypto:Fees",
        "expenses_account": "Expenses:Misc",
        "income_account": "Income:Misc",
        "base_currency": "ETH"
    }
    path = tmp_path / "config.json"
    with open(path, 'w') as f:
        json.dump(config, f)
    return str(path)

@pytest.fixture
def tx_file(tmp_path):
    txs = [
        {
            "time": int(datetime.datetime.now().timestamp()),
            "tx_id": "0xabc123",
            "from": "0x1234567890123456789012345678901234567890",
            "to": "0x0000000000000000000000000000000000000000",
            "value": "1.5",
            "currency": "ETH"
        }
    ]
    path = tmp_path / "ethereum_test.json"
    with open(path, 'w') as f:
        json.dump(txs, f)
    return str(path)

def test_importer_identify(config_path, tmp_path):
    importer = Importer(config_path=config_path)

    # Should identify correct filename
    filepath = str(tmp_path / "ethereum_test.json")
    assert importer.identify(filepath) is True

    # Should reject incorrect filename
    wrong_filepath = str(tmp_path / "wrong_name.json")
    assert importer.identify(wrong_filepath) is False

def test_importer_extract(config_path, tx_file):
    importer = Importer(config_path=config_path)

    entries = importer.extract(tx_file)
    assert len(entries) == 1

    tx = entries[0]
    assert tx.meta['txid'] == "0xabc123"
    assert len(tx.postings) > 0
