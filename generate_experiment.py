from pathlib import Path
import numpy as np
import pandas as pd

def generate_experiment(n_users=30000, seed=2026):
    rng=np.random.default_rng(seed)
    prior_orders=rng.poisson(1.8,n_users)
    prior_spend=np.maximum(0,22+31*prior_orders+rng.normal(0,28,n_users))
    tenure=rng.integers(1,49,n_users)
    high_value=(prior_spend>=np.quantile(prior_spend,.70)).astype(int)
    treatment=rng.binomial(1,.5,n_users)

    logit=-1.35+.16*prior_orders+.004*prior_spend+.008*tenure
    p0=1/(1+np.exp(-logit))
    lift=.025+.018*(1-high_value)
    purchased=rng.binomial(1,np.clip(p0+treatment*lift,.01,.95))
    orders=purchased*(1+rng.poisson(.35+.10*treatment,n_users))
    aov=np.maximum(8,48+.08*prior_spend+rng.normal(0,15,n_users))
    revenue=orders*aov
    engaged=rng.binomial(1,np.clip(.46+.07*treatment+.035*prior_orders,.05,.95))
    refund=purchased*rng.binomial(1,.055+.003*treatment,n_users)
    support=rng.binomial(1,.075+.002*treatment,n_users)

    return pd.DataFrame({"user_id":np.arange(1,n_users+1),"treatment":treatment,
        "prior_orders":prior_orders,"prior_spend":prior_spend.round(2),
        "tenure_months":tenure,"high_value_user":high_value,"purchased":purchased,
        "orders":orders,"revenue":revenue.round(2),"engaged_7d":engaged,
        "refund":refund,"support_contact":support})

if __name__=="__main__":
    df=generate_experiment()
    out=Path(__file__).resolve().parents[1]/"data"/"rewards_experiment.csv"
    df.to_csv(out,index=False)
    print(f"Wrote {len(df):,} users")
