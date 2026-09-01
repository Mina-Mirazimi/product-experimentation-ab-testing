from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
d=pd.read_csv(ROOT/"results"/"experiment_results.csv")
d=d[d.metric.isin(["purchased","engaged_7d","refund","support_contact"])]
fig,ax=plt.subplots(figsize=(8,5))
ax.bar(d.metric,d.relative_lift_pct)
ax.axhline(0,linewidth=1)
ax.set_ylabel("Relative lift (%)")
ax.set_title("Treatment Effect Across Product Metrics")
ax.tick_params(axis="x",rotation=20)
fig.tight_layout()
fig.savefig(ROOT/"results"/"metric_lifts.png",dpi=160)
