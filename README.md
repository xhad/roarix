### Step 1


### install python requirements
Create the requirements.txt with the following packages:

```
Flask==0.12.2
requests==2.18.4
```

```pip2 install -r requirements.txt```

### create the blockchain daemon

```touch roarixd.py```

Or just cretae the the file, your-blockchain-named.py.

### create the basic class structure

- create a class, and call it your blockchain name. 

Your class will have the following arrays:

- self.chain
- self.transactions

self.chain is an array that will be the blockchain.

self.transaction is an araay that will hold current transactions.


### Example Block data

A blockchain is a series of blocks, where each block contains an array of currency transactions. Each block is connected to the previous block with a hash. This connects every block into a blockchain where each is connected one to the next, via hashes from the previous block.

```json

block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```




