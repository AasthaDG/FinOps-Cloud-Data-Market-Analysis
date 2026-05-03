import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FinOps Dashboard", layout="wide")

# Load data
df = pd.read_csv("cost_data.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# ---------------- HEADER ----------------
st.title("💰 FinOps Cost Intelligence Dashboard")
st.subheader("StubHub-style Cloud Cost Visibility & Optimization Simulator")

# ---------------- KPI ----------------
total_cost = df["cost"].sum()
avg_cost = df["cost"].mean()
top_service = df.groupby("service")["cost"].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("Total Cost", f"${total_cost}")
col2.metric("Avg Cost", f"${round(avg_cost,2)}")
col3.metric("Top Service", top_service)

st.markdown("---")

# ---------------- COST TREND ----------------
st.subheader("📈 Cost Over Time (Spike Detection View)")
trend = df.groupby("date")["cost"].sum().reset_index()

fig1 = px.line(trend, x="date", y="cost", markers=True)
st.plotly_chart(fig1, use_container_width=True)


# ---------------- EVENT SPIKE VIEW ----------------
st.subheader("🚨 Event-Driven Cost Spike Simulation")

event_trend = df.groupby(["date", "event"])["cost"].sum().reset_index()

fig = px.line(
    event_trend,
    x="date",
    y="cost",
    color="event",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
🧠 Insight:
- Non-event days show stable baseline cost
- Event day (1) shows sudden spike across compute + serverless services

💡 FinOps Interpretation:
This simulates how ticket marketplaces experience cost surges during high-demand events.
Early detection helps avoid unexpected budget overruns.
""")

# ---------------- SERVICE COST ----------------
st.subheader("⚙️ Cost by Service")
service_cost = df.groupby("service")["cost"].sum().reset_index()

fig2 = px.bar(service_cost, x="service", y="cost")
st.plotly_chart(fig2, use_container_width=True)

# ---------------- TEAM COST ----------------
st.subheader("👥 Cost by Team")
team_cost = df.groupby("team")["cost"].sum().reset_index()

fig3 = px.pie(team_cost, names="team", values="cost")
st.plotly_chart(fig3, use_container_width=True)

# ---------------- PROVIDER COST ----------------
st.subheader("☁️ Cloud Provider Cost Split")
provider_cost = df.groupby("cloud_provider")["cost"].sum().reset_index()

fig4 = px.bar(provider_cost, x="cloud_provider", y="cost")
st.plotly_chart(fig4, use_container_width=True)

# ---------------- INSIGHTS ----------------
st.subheader("🚨 FinOps Insights (Auto-generated logic)")

highest_service = service_cost.sort_values("cost", ascending=False).iloc[0]
highest_day = trend.sort_values("cost", ascending=False).iloc[0]

st.info(f"""
• Highest cost driver: {highest_service['service']} (${highest_service['cost']})  
• Peak spending day: {highest_day['date'].date()} (${highest_day['cost']})  
• Compute-heavy workload indicates scaling pressure  
• Opportunity: optimize EC2 / VM utilization during peak days  
""")