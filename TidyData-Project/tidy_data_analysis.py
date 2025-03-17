import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("olympics_08_medalists.csv")
# Streamlit UI
st.markdown("<h2 style='color: #0000FF;'>🏅 2008 Olympic Medalists - Tidy Data Project</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #FF6347;'>📊 Raw Data Preview</h3>", unsafe_allow_html=True)
st.markdown("""
            Our raw data is a mess that requires a lot of tidying up. 
            It has every athlete listed for every event, whether they competed in it or not.
            We will fix this utilizing a series of data cleaning methods, 
            after which we will use visualizations to display the data in an easily consumable manner.
            """)
st.dataframe(df.head()) 

# Create space between data and visualizations
st.markdown("<br>", unsafe_allow_html=True)


st.markdown("<h3 style='color: #FF6347;'>📊 Melted Data Preview</h3>", unsafe_allow_html=True)
st.markdown("""First, we use the `melt()` function to transform 
            the dataset so that each row represents a single athlete's medal in a specific event.""")
df_melted = (
        df 
        .melt(id_vars=["medalist_name"], var_name="Event", value_name="Medal") # melted on the athlete name
        # Renamed to Athlete to make it easier to read
        .rename(columns={'medalist_name':"Athlete" })
        .drop_duplicates() # In case there are any repeat entries
        .dropna() # Dropping rows with missing values to ensure we have complete records for analysis
    )   
st.dataframe(df_melted.head())

# Create space between data and visualizations
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h3 style='color: #FF6347;'>🧽Cleaning the Data</h3>", unsafe_allow_html=True)
st.markdown("""We then split the `Event` column into `Gender` and `Event` to separate athlete participation details. 
            This makes the data more structured.""")
# Split the column to make the data easier to digest, a new column for gender and a new column for event
df_melted[['Gender', 'Event']] = df_melted['Event'].str.split('_', expand=True)
# Capitalize all of the data to make it look neat
df_melted['Event'] = df_melted['Event'].str.capitalize()
df_melted['Gender'] = df_melted['Gender'].str.capitalize()
df_melted['Medal'] = df_melted['Medal'].str.capitalize()
st.dataframe(df_melted.head())

# Create space between data and visualizations
st.markdown("<br>", unsafe_allow_html=True)


#Here we start the visualization section of the page
st.markdown("<h2 style='color: #0000FF;'>👀 Visualizing the Data</h2>", unsafe_allow_html=True)
st.markdown("""
            Now that we have cleaned the data, lets display it in ways that make it easy to consume!
            Below are three ways of visualizing the data.
            1) Medal Count by Event & Gender
            2) Seeing a Specific Athlete's Achievement
            3) Viewing Medalists by Filtering Event & Gender
            """)

# Create space between data and visualizations
st.markdown("<br>", unsafe_allow_html=True)

# Aggregating using a pivot table, pivoting data to calculate the number of medals per event and gender
pivot_table = df_melted.pivot_table(
    values='Medal',
    index='Event',
    columns='Gender',
    aggfunc='count'
)
st.markdown("<h3 style='color: #FF6347;'> 1) 🏆 Medal Count by Event & Gender</h3>", unsafe_allow_html=True)
# Using an expander so you only see the explanation for the visual if you wish
with st.expander("See explanation for this visualization"):
    st.markdown("""
            This bar chart shows the distribution of medals by **event** and **gender**. 
            The **x-axis** represents different Olympic events, and the **y-axis** shows the **number of medals**. 
            The bars are divided by **gender**, with separate bars for **men** and **women** in each event. 
            This chart allows us to see how the number of medals varies by event and gender.
            """)
with st.expander("See pivot table used for visualization below"):
    st.markdown("""
    This is the **pivot table** used to achieve the bar chart below
    """)
    st.table(pivot_table)

st.bar_chart(pivot_table, use_container_width= True)



# Create space between data and visualizations
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)



# Dropdown box for selecting an athlete and seeing their achievements
st.markdown("<h3 style='color: #FF6347;'> 2) ⭐ Select an Athlete to View Their Achievement", unsafe_allow_html=True)
with st.expander("See explanation for this visualization"):    
    st.markdown("""
            In this section, you can select an **athlete** from the dropdown menu. 
            Once selected, you'll be able to see the events they participated 
            in and the **type of medal** (Gold, Silver, or Bronze) they won in their event. 
            It's a great way to explore the individual achievements of athletes in the 2008 Olympics.
            """)
selected_athlete = st.selectbox("Choose an athlete:", df_melted["Athlete"].unique())
athlete_data = df_melted[df_melted["Athlete"] == selected_athlete]
st.write(f"Achievement for {selected_athlete}")
for index, row in athlete_data.iterrows():
        st.write(f"🏆 {row['Event']} - {row['Medal']} Medal")

# Create space between data and visualizations
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Dropdowns for selecting Gender and Event
st.markdown("<h3 style='color: #FF6347;'> 3) 🏅 Select Gender & Event to View Medalists</h3>", unsafe_allow_html=True)
# Using an expander so you only see the explanation for the visual if you wish
with st.expander("See explanation for this visualization"):
    st.markdown("""
            Use the dropdown menus to choose a **gender** and an **event**. 
            After making your selections, a list of athletes who won medals in the chosen event and gender will be displayed.
            The table will show the **athlete names** and the **medal types** (Gold, Silver, Bronze) they won in that event. 
            Additionally, the medalists will be sorted by medal type, 
            with **Gold medalists** displayed first, followed by **Silver** and **Bronze** medalists.
            This allows you to see the top medalists in specific events and compare the performance of different genders in those events.
            """)
selected_gender = st.selectbox("Choose a gender:", df_melted["Gender"].unique())
selected_event = st.selectbox("Choose an event:", df_melted["Event"].unique())
# Filter dataset based on selections
filtered_medalists = df_melted[(df_melted["Gender"] == selected_gender) & 
                               (df_melted["Event"] == selected_event)]
medal_order = pd.Categorical(filtered_medalists["Medal"], categories=["Gold", "Silver", "Bronze"], ordered=True)
filtered_medalists = filtered_medalists.sort_values(by="Medal", key=lambda x: medal_order)
# Display results
st.write(f"### Medalists in {selected_event} ({selected_gender})")
st.table(filtered_medalists[["Athlete", "Medal"]])



