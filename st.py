import streamlit as st
import trelloAPI as tr
import pandas as pd
import plotly.express as px
import calendar

df = pd.read_pickle('pic')
#cal = calendar.cal()
venue = list(df['Venue'].unique())
venue.append('All')
wind_dir = ['N', 'NE','E', 'SE', 'S', 'SW', 'W', 'NW']
wind_str = ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts']

st.title('Dais Condition Analysis')

a = st.sidebar.selectbox('Mode', ['Condition Review', 'Condition Logging', 'Training Calendar'])
if a == 'Condition Review':
    ven = st.sidebar.selectbox('Venue', venue)
    for i in venue:
        if ven == i:
            if ven != 'All':
                df = df[df['Venue'] == ven]
            st.header(ven)
            diag = st.sidebar.selectbox('Diagram', ['Wind Strength', 'Wind Direction', 'Notes'])
            if diag == 'Wind Strength':
                fig = px.line_polar(df, theta=df['Wind'].value_counts().index, r=df['Wind'].value_counts(), line_close=True, category_orders={ 'r' : ['0-7knts', '7-12knts', '12-15knts', '15-18knts', '18-23knts']}) #
                st.plotly_chart(fig, use_container_width=True)

            if diag == 'Wind Direction':
                fig = px.line_polar(df, theta=df['Direction'].value_counts().index, r=df['Direction'].value_counts(), line_close=True, category_orders={ 'r' : ['N', 'NE','E', 'SE', 'S', 'SW', 'W', 'NW']}) #
                st.plotly_chart(fig, use_container_width=True)

            if diag == 'Notes':
                st.subheader('Venue Notes')
                dir = st.select_slider('Wind Direction', options=wind_dir)
                str = st.select_slider('Wind Strength', options=wind_str, value=('0-7knts','18-23knts'))
                #for i in df.rows:
                with st.expander('Date'):
                    st.write("some note written for the venue in question. More logic is needed")
                with st.expander('Date'):
                    st.write("some note written for the venue in question. More logic is needed")

if a == 'Condition Logging':
    st.header('Condition Logging')
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

    if st.button('Add Training Session'):
        st.write('Wind Strength', str)
        st.write('Wind Direction', dir)
        st.write('Date', date)
        st.write('Venue', ven)
        st.write('Notes', notes)

        try:
            data = pd.read_pickle('data')
        except:
            data = pd.DataFrame()
        data = data.append({'Wind Strength': [str], 'Wind Direction': [dir], 'Date': [date], 'Venue': [ven], 'Notes': [notes]}, ignore_index=True)
        data.to_pickle('data')
    else:
        st.write('Press button to log a training session')

if a == 'Training Calendar':
    st.write('calender here')
    stuff = pd.read_pickle('data')
    st.dataframe(stuff.astype(str))
