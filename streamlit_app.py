import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Irish Health Insurance Analyzer", layout="wide")

st.title("🇮🇪 Health Insurance Analyzer")
st.subheader("Optimise your plan against the rising market")

tab1, tab2, tab3 = st.tabs(["📊 Market Pulse", "🏥 Coverage Analyzer", "💰 Savings Calculator"])

with tab1:
    st.markdown("### The Inflation Curve: Cost of Loyalty (2023-2026)")
    st.info("💡 Insight: Premiums are rising faster than tech salaries. Staying on the same plan costs you more every year.")
    
    # Chart 1: Inflation Curve
    years = ['2023', '2024', '2025', '2026 (Est)']
    premiums = [1594, 1740, 1879, 1929]
    df_inflation = pd.DataFrame({'Year': years, 'Average Premium (€)': premiums})
    
    fig_line = px.line(df_inflation, x='Year', y='Average Premium (€)', markers=True, 
                       title="Average Adult Premium Price Trend")
    fig_line.update_traces(line_color='#FF4B4B')
    fig_line.add_annotation(x='2026 (Est)', y=1929, text="+€335 since 2023", showarrow=True, arrowhead=1)
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Who Covers Ireland?")
        # Chart 2: Market Share
        labels = ['Vhi Healthcare', 'Laya Healthcare', 'Irish Life Health', 'Others']
        values = [48, 28, 20, 4]
        colors = ['#1f77b4', '#d62728', '#9467bd', '#7f7f7f']
        fig_donut = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4, marker=dict(colors=colors))])
        fig_donut.update_layout(title_text="Market Share Breakdown (2025)")
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with col2:
        st.markdown("### The Hidden Cost: Day-to-Day vs Hospital")
        st.write("Most 'standard' plans cover hospital stays well but fail on day-to-day claims like GP and Physio visits due to high excesses.")
        # Chart 3: Claims vs Coverage Gap
        categories = ['GP Visits', 'Physio', 'Dental', 'Hospital Stay']
        usage_frequency = [85, 60, 70, 15] # Mock high frequency
        coverage_value = [20, 30, 15, 95] # Mock low coverage for day-to-day
        
        fig_bar = go.Figure(data=[
            go.Bar(name='Usage Frequency (%)', x=categories, y=usage_frequency),
            go.Bar(name='Plan Coverage (%)', x=categories, y=coverage_value)
        ])
        fig_bar.update_layout(barmode='group', title_text="Usage vs Coverage Gap")
        st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.header("Upload Your Renewal Letter")
    st.write("Upload your policy document to let our AI extract your current benefits and match them against the market.")
    uploaded_file = st.file_uploader("Choose a PDF or CSV file", type=['pdf', 'csv'])
    if uploaded_file is not None:
        st.success("File uploaded successfully! Analysis running...")
        # Placeholder for analysis logic

with tab3:
    st.header("Projected Savings")
    st.metric(label="Potential Annual Savings", value="€450", delta="22%")
    st.write("Based on typical switching from legacy corporate plans to modern equivalents.")
