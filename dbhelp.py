import mysql.connector
import pandas as pd
import streamlit as st


class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='EnterYourPasswordHere',
                database='indigo'
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL")
        except:
            print("Connection Error")

    def fetch_city_name(self):
        city = []
        self.cursor.execute('''
        SELECT DISTINCT (Destination) FROM indigo.flights
        UNION 
        SELECT DISTINCT (Source) FROM indigo.flights
        ''')
        data = self.cursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def get_date(self, label="Select a date", min_date=None, max_date=None, default_date=None):
        min_date = pd.to_datetime(min_date) if min_date else None
        max_date = pd.to_datetime(max_date) if max_date else None
        selected_date = st.date_input(label, min_value=min_date, max_value=max_date, value=default_date)
        return selected_date

    def fetch_flights_from_date(self, start_date, source, destination):
        query = f'''
        SELECT Airline,Date_of_Journey as Date, Source,Destination,Price FROM indigo.flights
        WHERE Date_of_Journey >= '{start_date}'
          AND Source = '{source}'
          AND Destination = '{destination}'
        '''
        self.cursor.execute(query)
        flights_data = self.cursor.fetchall()
        return flights_data

    def fetch_flights_frequency(self):

        airlines = []
        frequency = []

        self.cursor.execute('''
        SELECT  Airline, COUNT(*) FROM indigo.flights
        group by Airline
        ''')

        data = flights_data = self.cursor.fetchall()

        for item in data:
            airlines.append(item[0])
            frequency.append(item[1])

        return airlines,frequency

    def busy_airport(self):

        city = []
        frequency = []

        self.cursor.execute('''
        select source, count(*) from(select source from indigo.flights
							union all
							select destination from indigo.flights) t
        group by t.source
        order by count(*) desc''')


        data = flights_data = self.cursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency
    
    
    





