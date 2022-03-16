import streamlit as st
import trelloAPI as tr
import pandas as pd
import plotly.express as px
import calendar
import datetime

df = pd.read_pickle('data')
venue = list(df['Venue'].unique())
venue.append('All')
wind_dir = ['N', 'NE','E', 'SE', 'S', 'SW', 'W', 'NW']
wind_str = ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts', '23-27knts','27+knts']

st.title('Dais Condition Analysis')

a = st.sidebar.selectbox('Mode', ['Condition Review', 'Condition Logging', 'Training Calendar'])
if a == 'Condition Review':
    rnge = st.sidebar.slider('How Long Ago?', value=datetime.date.today(), max_value=datetime.date.today(), min_value=min(df['Date']))
    ven = st.sidebar.selectbox('Venue', venue)
    df = df[df['Date'] >= rnge]
    for i in venue:
        if ven == i:
            if ven != 'All':
                df = df[df['Venue'] == ven]
            st.header(ven)
            diag = st.sidebar.selectbox('Diagram', ['Wind Strength', 'Wind Direction', 'Notes'])
            if diag == 'Wind Strength':
                fig = px.line_polar(df, theta=df['Wind Strength'].value_counts().index, r=df['Wind Strength'].value_counts(), line_close=True, category_orders={ 'r' : ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts']}) #
                st.plotly_chart(fig, use_container_width=True)

            if diag == 'Wind Direction':
                fig = px.line_polar(df, theta=df['Wind Direction'].value_counts().index, r=df['Wind Direction'].value_counts(), line_close=True, category_orders={ 'r' : ['N', 'NE','E', 'SE', 'S', 'SW', 'W', 'NW']}) #
                st.plotly_chart(fig, use_container_width=True)

            if diag == 'Notes':
                st.subheader('Venue Notes')
                dir = st.select_slider('Wind Direction', options=wind_dir)
                df = df[df['Wind Direction'] == dir]
                stren = st.select_slider('Wind Strength', options=wind_str)
                df = df[df['Wind Strength'] == stren]
                df.sort_values(by='Date', ascending=False, inplace=True)
                for i in range(len(df.index)):
                    with st.expander(df.iloc[i]['Name']+',  ('+str(df.iloc[i]['Date'])+')'):
                        st.write(df.iloc[i]['Notes'])
                        st.write(df.iloc[i]['Video'])



if a == 'Condition Logging':
    st.header('Condition Logging')
    name = st.text_input('Session Name')
    str = st.select_slider('Wind Strength', options=wind_str)
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input('Date')
        dir = st.selectbox('Wind Direction', wind_dir)

    with col2:
        venue.append('Add')
        ven = st.selectbox('Venue', venue)
        if ven == 'Add':
            ven = st.text_input('New Venue')

    notes = st.text_area('Add notes')

    video = st.text_input('Add Video Link')

    if st.button('Add Training Session'):
        st.write('Wind Strength', str)
        st.write('Wind Direction', dir)
        st.write('Date', date)
        st.write('Venue', ven)
        st.write('Notes', notes)
        st.write(type(date))

        try:
            data = pd.read_pickle('data')
        except:
            data = pd.DataFrame()
        data = data.append({'Name':name, 'Wind Strength': str, 'Wind Direction': dir, 'Date': date, 'Venue': ven, 'Notes': notes, 'Video':video}, ignore_index=True)
        data.to_pickle('data')

    else:
        st.write('Press button to log a training session')

if a == 'Training Calendar':
    st.write('calender here')
    stuff = pd.read_pickle('data')
    st.dataframe(stuff.astype(str))
