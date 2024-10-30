from matplotlib import pyplot as plt
import pandas as gp

states = gp.read_file("https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_500k.zip")

trumpOrBiden = data[(data["candidate"] == "Donald Trump") | (data["candidate"] == "Joe Biden")] #used bitwise or
votes_by_state = trumpOrBiden.groupby(["state", "candidate"], as_index=False)["votes"].sum()
votes_pivot = votes_by_state.pivot(index="state", columns="candidate", values="votes")
votes_share = votes_pivot.div(votes_pivot.sum(axis=1), axis=0)

plotting_df = pd.merge(states, votes_share, left_on="NAME", right_on="state")

plotting_df.plot(figsize=(16, 6), column="Donald Trump", cmap="bwr", legend=True, vmin=0.4, vmax=0.6)
plt.xlim(-180, -63)
plt.title("Donal Trump")
plt.show()