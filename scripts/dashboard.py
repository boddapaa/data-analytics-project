"""
Interactive Dashboard using Streamlit
This script creates an interactive dashboard for data visualization and exploration.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os


# Page configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data
def load_data():
    """Load the sales data from CSV"""
    # Try to find the data file
    possible_paths = [
        '../data/sample_sales_data.csv',
        'data/sample_sales_data.csv',
        './data/sample_sales_data.csv'
    ]
    
    df = None
    for path in possible_paths:
        try:
            df = pd.read_csv(path)
            break
        except FileNotFoundError:
            continue
    
    if df is None:
        # If running from scripts directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        csv_path = os.path.join(project_root, 'data', 'sample_sales_data.csv')
        df = pd.read_csv(csv_path)
    
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.strftime('%B')
    
    return df


def main():
    """Main dashboard function"""
    
    # Title and description
    st.title("📊 Sales Analytics Dashboard")
    st.markdown("### Interactive Data Visualization and Exploration")
    st.markdown("---")
    
    # Load data
    try:
        df = load_data()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['date'].min(), df['date'].max()),
        min_value=df['date'].min().date(),
        max_value=df['date'].max().date()
    )
    
    # Category filter
    categories = st.sidebar.multiselect(
        "Select Categories",
        options=df['category'].unique(),
        default=df['category'].unique()
    )
    
    # Region filter
    regions = st.sidebar.multiselect(
        "Select Regions",
        options=df['region'].unique(),
        default=df['region'].unique()
    )
    
    # Apply filters
    if len(date_range) == 2:
        filtered_df = df[
            (df['date'].dt.date >= date_range[0]) &
            (df['date'].dt.date <= date_range[1]) &
            (df['category'].isin(categories)) &
            (df['region'].isin(regions))
        ]
    else:
        filtered_df = df[
            (df['category'].isin(categories)) &
            (df['region'].isin(regions))
        ]
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Sales",
            value=f"${filtered_df['sales'].sum():,.2f}",
            delta=f"{len(filtered_df)} transactions"
        )
    
    with col2:
        st.metric(
            label="Total Quantity",
            value=f"{filtered_df['quantity'].sum():,}",
            delta=f"{filtered_df['quantity'].mean():.1f} avg"
        )
    
    with col3:
        st.metric(
            label="Unique Products",
            value=filtered_df['product'].nunique(),
            delta=f"{len(categories)} categories"
        )
    
    with col4:
        st.metric(
            label="Average Sale",
            value=f"${filtered_df['sales'].mean():,.2f}",
            delta=f"±${filtered_df['sales'].std():.2f}"
        )
    
    st.markdown("---")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Trends", "🏆 Performance", "🗺️ Regional", "📊 Analysis"])
    
    with tab1:
        st.subheader("Sales Trends Over Time")
        
        # Time series plot
        daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
        fig_trend = px.line(
            daily_sales,
            x='date',
            y='sales',
            title='Daily Sales Trend',
            labels={'sales': 'Total Sales ($)', 'date': 'Date'}
        )
        fig_trend.update_traces(line_color='#1f77b4', line_width=2)
        fig_trend.update_layout(hovermode='x unified')
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Monthly aggregation
        col1, col2 = st.columns(2)
        
        with col1:
            monthly_sales = filtered_df.groupby(['year', 'month_name'])['sales'].sum().reset_index()
            fig_monthly = px.bar(
                monthly_sales,
                x='month_name',
                y='sales',
                color='year',
                title='Monthly Sales Comparison',
                labels={'sales': 'Total Sales ($)', 'month_name': 'Month'}
            )
            st.plotly_chart(fig_monthly, use_container_width=True)
        
        with col2:
            category_trend = filtered_df.groupby(['date', 'category'])['sales'].sum().reset_index()
            fig_cat_trend = px.line(
                category_trend,
                x='date',
                y='sales',
                color='category',
                title='Sales Trend by Category',
                labels={'sales': 'Total Sales ($)', 'date': 'Date'}
            )
            st.plotly_chart(fig_cat_trend, use_container_width=True)
    
    with tab2:
        st.subheader("Product and Category Performance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Top products
            top_products = filtered_df.groupby('product')['sales'].sum().sort_values(ascending=False).head(10)
            fig_products = px.bar(
                x=top_products.values,
                y=top_products.index,
                orientation='h',
                title='Top 10 Products by Sales',
                labels={'x': 'Total Sales ($)', 'y': 'Product'}
            )
            fig_products.update_traces(marker_color='coral')
            st.plotly_chart(fig_products, use_container_width=True)
        
        with col2:
            # Category breakdown
            category_sales = filtered_df.groupby('category')['sales'].sum()
            fig_category = px.pie(
                values=category_sales.values,
                names=category_sales.index,
                title='Sales Distribution by Category',
                hole=0.4
            )
            st.plotly_chart(fig_category, use_container_width=True)
        
        # Product performance table
        st.subheader("Product Performance Details")
        product_stats = filtered_df.groupby(['product', 'category']).agg({
            'sales': ['sum', 'mean', 'count'],
            'quantity': 'sum'
        }).round(2)
        product_stats.columns = ['Total Sales', 'Avg Sales', 'Transactions', 'Total Quantity']
        product_stats = product_stats.sort_values('Total Sales', ascending=False)
        st.dataframe(product_stats, use_container_width=True)
    
    with tab3:
        st.subheader("Regional Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Regional sales
            region_sales = filtered_df.groupby('region')['sales'].sum().reset_index()
            fig_region = px.bar(
                region_sales,
                x='region',
                y='sales',
                title='Sales by Region',
                labels={'sales': 'Total Sales ($)', 'region': 'Region'},
                color='sales',
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig_region, use_container_width=True)
        
        with col2:
            # Regional distribution pie chart
            fig_region_pie = px.pie(
                region_sales,
                values='sales',
                names='region',
                title='Regional Sales Distribution',
                hole=0.3
            )
            st.plotly_chart(fig_region_pie, use_container_width=True)
        
        # Heatmap: Category vs Region
        st.subheader("Category-Region Heatmap")
        pivot_data = filtered_df.pivot_table(
            values='sales',
            index='category',
            columns='region',
            aggfunc='sum',
            fill_value=0
        )
        
        fig_heatmap = px.imshow(
            pivot_data,
            labels=dict(x="Region", y="Category", color="Total Sales"),
            title="Sales Heatmap: Category vs Region",
            color_continuous_scale="YlOrRd",
            text_auto=True
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with tab4:
        st.subheader("Advanced Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Quantity vs Sales scatter
            fig_scatter = px.scatter(
                filtered_df,
                x='quantity',
                y='sales',
                color='category',
                size='sales',
                hover_data=['product', 'region'],
                title='Quantity vs Sales Analysis',
                labels={'quantity': 'Quantity Sold', 'sales': 'Sales Amount ($)'}
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            # Box plot for sales distribution
            fig_box = px.box(
                filtered_df,
                x='category',
                y='sales',
                color='category',
                title='Sales Distribution by Category',
                labels={'sales': 'Sales ($)', 'category': 'Category'}
            )
            st.plotly_chart(fig_box, use_container_width=True)
        
        # Correlation analysis
        st.subheader("Summary Statistics")
        st.dataframe(filtered_df[['sales', 'quantity']].describe(), use_container_width=True)
        
        # Raw data view
        with st.expander("📋 View Raw Data"):
            st.dataframe(filtered_df, use_container_width=True)
            
            # Download button
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Filtered Data as CSV",
                data=csv,
                file_name=f'filtered_sales_data_{datetime.now().strftime("%Y%m%d")}.csv',
                mime='text/csv',
            )
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>💡 Use the sidebar filters to explore different segments of the data</p>
            <p>📊 Data Analytics Project | Built with Streamlit & Plotly</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
