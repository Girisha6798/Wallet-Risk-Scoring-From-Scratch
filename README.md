# Zeru Wallet Risk Scoring - Task 2

This project analyzes wallet risk using a sample dataset of 100+ wallets.

## Files

- `wallets.csv`: Input list of wallet IDs.
- `wallets_with_scores.csv`: Risk score (randomized 100–900).
- `wallets_with_categories.csv`: Final output with risk category.
- `step2_calculate_risk_score.py`: Code to assign risk scores.

## Risk Scoring Logic

For this prototype, we used randomized scoring between 100–900 as a placeholder.

In a real-world scenario, scoring would depend on:
- Borrow vs. supply ratio
- Liquidation history
- Number of protocol interactions
- Wallet age and transaction volume

## Categories
- **Low Risk**: 100–399
- **Medium Risk**: 400–699
- **High Risk**: 700–900

## Next Steps (Future Work)
- Integrate on-chain data (Compound V2/V3)
- Define scoring weights based on DeFi behavior
