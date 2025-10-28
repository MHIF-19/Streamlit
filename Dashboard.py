import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="PSL Dashboard")

df=pd.read_csv("Psl_Complete_Dataset.csv")

st.sidebar.header("Filter By: ")
filter=st.sidebar.selectbox("",["Team Data","Batting Data","Bowling Data"])

st.logo(image="https://upload.wikimedia.org/wikipedia/en/2/24/Official_logo_of_Pakistan_Super_League.png")


c1,c2=st.columns([1,4])
with c2:
    st.title("Ultimate PSL Stats")

with c1:
    st.image("https://upload.wikimedia.org/wikipedia/en/2/24/Official_logo_of_Pakistan_Super_League.png",width=200)

sound=st.button("Play Aesthetic PSL Sound")
if sound:
    st.audio("psl.mp3",autoplay=True)

total_matches=df.match_id.nunique()
total_stadiums=df.venue.nunique()
total_teams=df.batting_team.nunique()
total_runs=df.total_runs.sum()
total_wickets=df.is_wicket.sum()
total_fours=(df.batsman_runs==4).sum()
total_sixes=(df.batsman_runs==6).sum()

col1,col2,col3=st.columns(3)

with col1:
    st.write(f"Total Matches Played: {total_matches}")
    st.write(f"Total Teams Participated: {total_teams}")
    st.write(f"Total Stadiums Used: {total_stadiums}")

with col2:
    st.write(f"Total Runs Scored: {total_runs}")
    st.write(f"Total Wickets: {total_wickets}")

with col3:
    st.write(f"Total Fours Smashed: {total_fours}")
    st.write(f"Total Sixes Smashed: {total_sixes}")


st.markdown("---")

a=df.groupby("match_id")["winner"].value_counts().reset_index()
pd.DataFrame(a)
team_wins=a.winner.value_counts().reset_index()
team_wins.columns=["Team","Wins"]
top_team=team_wins.iloc[0]
st.write(f"Most Successfull Team Of PSL is: **{top_team["Team"]}** with **{top_team["Wins"]}** wins")


runs_by_batter2=df.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).reset_index()
runs_by_batter2.columns=["Batter","runs"]
top_batter=runs_by_batter2.iloc[0]
st.write(f"Most Runs In PSL History: **{top_batter.Batter}** with **{top_batter.runs}** runs")


wickets_bowler2=df.groupby("bowler")["is_wicket"].sum().sort_values(ascending=False).reset_index()
wickets_bowler2.columns=["Bowler","wickets"]
top_bowler=wickets_bowler2.iloc[0]
st.write(f"Most Wickets in PSL History: **{top_bowler.Bowler}** with **{top_bowler.wickets}** wickets")

st.markdown("---")

if filter=="Batting Data":

    st.subheader("All Time Top 10 Higest Runs Scorer (2016-2024)")
    check=st.checkbox("Filter By Year")
    if check:
        start=st.number_input("Enter Starting Year",min_value=2016,max_value=2024,value=2016)
        end=st.number_input("Enter Ending Year",min_value=2016,max_value=2024,value=2024)
        filtered_df=df[(df.season>=start) & (df.season<=end)]
        runs_by_batter =filtered_df.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(10)
        st.bar_chart(runs_by_batter)
    else:   
        runs_by_batter =df.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(10)
        st.bar_chart(runs_by_batter)


    st.subheader("Runs Scored by Batsman over time")
    check3=st.selectbox("Select the batter",df.batter.unique())
    filtered_df2=df[df.batter==check3]
    line=filtered_df2.groupby("season")["batsman_runs"].sum()
    st.line_chart(line)





if filter=="Bowling Data":

    st.subheader("All Time Top 10 WicketTakers (2016-2024)")
    check2=st.checkbox("Filter By Years")
    if check2:
        start=st.number_input("Enter Starting Year",min_value=2016,max_value=2024,value=2016)
        end=st.number_input("Enter Ending Year",min_value=2016,max_value=2024,value=2024)
        filtered_df=df[(df.season>=start) & (df.season<=end)]
        wickets_bowler =filtered_df.groupby("bowler")["is_wicket"].sum().sort_values(ascending=False).head(10)
        st.bar_chart(wickets_bowler)
    else:   
        wickets_bowler=df.groupby("bowler")['is_wicket'].sum().sort_values(ascending=False).head(10)
        st.bar_chart(wickets_bowler)



    st.markdown("---")

    st.subheader("Wickets taken by Bowler over time")
    check4=st.selectbox("Select the Bowler",df.bowler.unique())
    filtered_df3=df[df.bowler==check4]
    line=filtered_df3.groupby("season")["is_wicket"].sum()
    st.line_chart(line)



if filter=="Team Data":

    st.subheader("Average Runs Scored by Each Team (Per Match)")
    filtered_df4=df.groupby(["match_id","batting_team"])["total_runs"].sum().reset_index()
    team_runs=filtered_df4.groupby("batting_team")["total_runs"].mean().sort_values(ascending=False)
    st.bar_chart(team_runs)


    st.markdown("---")

    st.subheader("Average Wickets Taken by Each Team (Per Match)")
    filtered_df5=df.groupby(["match_id","bowling_team"])["is_wicket"].sum().reset_index()
    team_wickets=filtered_df5.groupby("bowling_team")["is_wicket"].mean().sort_values(ascending=False)
    st.bar_chart(team_wickets)

    st.markdown("---")

    st.subheader("Most Matches win by Each Team")
    year_check=st.checkbox("Filter by Year")
    if year_check:
        pass
    else:
        st.bar_chart(team_wins,x="Team",y="Wins")