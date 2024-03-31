import streamlit as st
from dbhelp import DB
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.sidebar.title("Airport Dashboard")

db = DB()

user_option = st.sidebar.selectbox('Menu', ['Check flights', 'Analytics', 'About'])

if user_option == 'Check flights':
    st.title('Check flights')

    col1, col2, col3 = st.columns(3)

    city = db.fetch_city_name()

    with col1:
        start_date = db.get_date("Select a start date", min_date="2019-01-03", max_date="2019-12-06")
        if start_date is not None:
            st.write(f"Start Date: {start_date.strftime('%Y-%m-%d')}")

    with col2:
        source = st.selectbox("Select Source", sorted(city))

    with col3:
        destination = st.selectbox("Select Destination", sorted(city))

    if st.button('Search'):
        if start_date is not None:
            # Convert start_date to string in 'YYYY-MM-DD' format
            start_date_str = start_date.strftime('%Y-%m-%d')
            flights_data = db.fetch_flights_from_date(start_date_str, source, destination)

            if flights_data:
                # Display flight details in a table
                st.table(pd.DataFrame(flights_data,
                                      columns=["Airline", "Date", "Source", "Destination", "Price"]))
            else:
                st.write("No flights found for the specified criteria.")

elif user_option == 'Analytics':
    st.title('Analytics')
    airline, frequency = db.fetch_flights_frequency()

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            title='Distribution of Flights by Airline'
        )
    )
    st.header('Flights by Airline(Freq. Distribution)')
    st.plotly_chart(fig, use_container_width=True)

    city, frequency = db.busy_airport()

    # Create a DataFrame for the data
    data = {'Airport': city, 'Frequency': frequency}
    df = pd.DataFrame(data)

    # Streamlit app
    st.title('Interactive Bar Chart: Busy Airports')

    # Create an animated bar chart with Plotly Express
    fig = px.bar(
        df,
        x='Airport',
        y='Frequency',
        color='Frequency',
        labels={'Frequency': 'Flights'},
        title='Busiest Airports',
        animation_frame='Airport',
        color_continuous_scale=px.colors.sequential.Plasma,
    )

    # Customize layout
    fig.update_layout(
        xaxis_title='Airport',
        yaxis_title='Frequency',
        xaxis={'categoryorder': 'total descending'},
    )

    # Display the animated bar chart
    st.plotly_chart(fig)

else:

    st.title('About Airport Dashboard')

    # Your Photo
    st.sidebar.image('dp.png', caption='Pratik Bokade', use_column_width=False, width=100)

    # Contact Information
    st.sidebar.header('Contact Information')
    st.sidebar.write("**Email:** pratikbokadework@gmail.com")
    st.sidebar.write("**LinkedIn:** [Pratik Bokade](https://www.linkedin.com/in/pratik-bokade-b15466230/)")
    st.sidebar.write("**Twitter:** [pratik_csv](https://twitter.com/pratik_csv)")

    # Introduction
    st.markdown("""
    Welcome to the Airport Dashboard! This interactive dashboard provides valuable insights into flight data, allowing users to check flights, explore analytics, and more.

    **Date Range:** From 2019-01-03 to 2019-12-06

    **Data Source:** This dashboard fetches data from a static database hosted on AWS. The information includes flight details such as airlines, dates, sources, destinations, and prices.

    Please explore the different sections in the sidebar to make the most of this dashboard. If you have any questions or feedback, feel free to reach out.

    Enjoy your journey through the Airport Dashboard!
    """)

    # Features
    st.header('Key Features')
    st.markdown("""
    - **Check Flights:** View information about available flights based on selected criteria.
    - **Analytics:** Explore interactive charts and graphs to gain insights into flight data.
    - **Busy Airports:** Discover the busiest airports based on flight frequency.
    """)

    # Acknowledgements
    st.header('Acknowledgements')
    st.markdown("""
    - Special thanks to [Streamlit](https://streamlit.io/) for making it easy to create interactive web apps with Python.
    - Data source: [Your Data Source, if applicable]
    """)
