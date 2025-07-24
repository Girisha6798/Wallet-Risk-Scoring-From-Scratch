import pandas as pd
import random

# Step 1: Load wallet addresses
df = pd.read_csv('zeru_wallet_scoring/wallets.csv')  # Make sure this CSV has a 'wallet_address' column

# Step 2: Simulate on-chain transaction features (for demonstration purposes)
df['num_lend_txns'] = [random.randint(0, 30) for _ in range(len(df))]
df['num_borrow_txns'] = [random.randint(0, 30) for _ in range(len(df))]
df['total_amount'] = [round(random.uniform(100, 50000), 2) for _ in range(len(df))]
df['repay_ratio'] = [round(random.uniform(0.0, 1.0), 2) for _ in range(len(df))]

# Step 3: Define risk scoring function
def calculate_risk(row):
    risk = (
        row['num_borrow_txns'] * 3          # more borrow = higher risk
        + row['total_amount'] * 0.0005      # larger volume = slightly riskier
        - row['num_lend_txns'] * 1.5        # more lending reduces risk
        - row['repay_ratio'] * 100          # better repay ratio reduces risk
        + 500                               # base score
    )
    return max(0, min(1000, round(risk)))  # Keep score between 0–1000

# Step 4: Apply risk scoring to each wallet
df['score'] = df.apply(calculate_risk, axis=1)

# Step 5: Keep only required columns
final_df = df[['wallet_address', 'score']]

# Step 6: Export final CSV
final_df.to_csv('wallet_risk_scores_final.csv', index=False)

print("✅ Final wallet risk score file created: 'wallet_risk_scores_final.csv'")
