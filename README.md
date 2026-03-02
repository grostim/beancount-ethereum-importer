# Ethereum transaction importer for Beancount

## Configuration

Example of configuration file: [config.json](config.json.example).

`beancount-ethereum` can load data from [Etherscan](https://etherscan.io/) or block explorers with similar API like [Blockscout](https://blockscout.com/poa/xdai/).

If you are using Etherscan, get your API key at https://etherscan.io/.

## Usage

Download transactions to file:

```
python beancount_ethereum/downloader.py --config=config.json --output-dir=downloads
```

Add importer to import configuration ([example](import_config.py.example)):
import_balances statement is optional and default to False.

```
import beancount_ethereum

CONFIG = [
    beancount_ethereum.importer.Importer(config_path='config.json', import_balances=True),
]
```

Check with `identify`:

```
python import_config.py identify downloads
```

Import transactions with `extract`:

```
python import_config.py extract downloads
```
