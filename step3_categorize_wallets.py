import pandas as pd

# Load wallets with scores
df = pd.read_csv('zeru_wallet_scoring/wallets_with_scores.csv')

# Categorize risk level
def get_risk_category(score):
    if score <= 300:
        return 'High Risk'
    elif score <= 600:
        return 'Medium Risk'
    else:
        return 'Low Risk'

df['risk_category'] = df['risk_score'].apply(get_risk_category)

# Save updated file
df.to_csv('zeru_wallet_scoring/wallets_with_categories.csv', index=False)

print("✅ Wallets categorized into risk levels and saved to wallets_with_categories.csv")
