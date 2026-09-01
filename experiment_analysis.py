from pathlib import Path
import numpy as np, pandas as pd
from scipy import stats
import statsmodels.api as sm

ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data"/"rewards_experiment.csv")

def estimate(outcome,data=df):
    c=data.loc[data.treatment==0,outcome]; t=data.loc[data.treatment==1,outcome]
    e=t.mean()-c.mean()
    se=np.sqrt(t.var(ddof=1)/len(t)+c.var(ddof=1)/len(c))
    return [outcome,c.mean(),t.mean(),e,100*e/c.mean() if c.mean()!=0 else np.nan,
            e-1.96*se,e+1.96*se,2*(1-stats.norm.cdf(abs(e/se)))]

metrics=["purchased","orders","revenue","engaged_7d","refund","support_contact"]
cols=["metric","control_mean","treatment_mean","effect","relative_lift_pct","ci_low","ci_high","p_value"]
results=pd.DataFrame([estimate(m) for m in metrics],columns=cols)

obs=np.array([(df.treatment==0).sum(),(df.treatment==1).sum()])
_,srm_p=stats.chisquare(obs,np.repeat(len(df)/2,2))

X=sm.add_constant(df[["treatment","prior_orders","prior_spend","tenure_months"]])
adjusted=sm.OLS(df.purchased,X).fit(cov_type="HC1")

resdir=ROOT/"results"; resdir.mkdir(exist_ok=True)
results.to_csv(resdir/"experiment_results.csv",index=False)
pd.DataFrame({"metric":["users","treatment_share","srm_p_value","adjusted_conversion_effect","adjusted_conversion_p_value"],
"value":[len(df),df.treatment.mean(),srm_p,adjusted.params["treatment"],adjusted.pvalues["treatment"]]}).to_csv(resdir/"experiment_summary.csv",index=False)
print(results.to_string(index=False))
