from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import pandas as pd
import time

# Load the wallet list from CSV
df = pd.read_csv("wallets.csv")
wallets = df['wallet_id'].tolist()

# Setup the GraphQL API for Compound V2
transport = RequestsHTTPTransport(
    url="https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2",
    verify=True,
    retries=3,
)
client = Client(transport=transport, fetch_schema_from_transport=True)

# For storing results
results = []

for i, wallet in enumerate(wallets):
    print(f"Fetching wallet {i+1}/{len(wallets)}: {wallet}")

    query = gql(f"""
    {{
      account(id: "{wallet.lower()}") {{
        tokens {{
          symbol
          supplyBalanceUnderlying
          borrowBalanceUnderlying
        }}
      }}
    }}
    """)

    try:
        response = client.execute(query)
        account = response.get("account", {})

        total_supply = 0
        total_borrow = 0

        if account:
            for token in account.get("tokens", []):
                total_supply += float(token["supplyBalanceUnderlying"])
                total_borrow += float(token["borrowBalanceUnderlying"])

        results.append({
            "wallet_id": wallet,
            "total_supply": total_supply,
            "total_borrow": total_borrow
        })

    except Exception as e:
        print(f"Error for {wallet}: {e}")
        results.append({
            "wallet_id": wallet,
            "total_supply": 0,
            "total_borrow": 0
        })

    time.sleep(0.5)

# Save to CSV
output = pd.DataFrame(results)
output.to_csv("wallet_transactions.csv", index=False)
print("✅ Done! Data saved to wallet_transactions.csv")
