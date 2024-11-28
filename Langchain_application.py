import streamlit as st
import langchain_helper as lh

st.title("Where to Study?")
country = st.sidebar.text_input("Enter the city/state/country name")
course = st.sidebar.text_input("Enter the course name")

if country:
    if course:
        # Get response from langchain_helper
        response = lh.place_to_study(country, course)
        
        # Splitting the response into places
        universities = response["university_name"].strip().split(",")
        
        st.header(f"Some of the Universities in {country} to study {course} are:")
        for item in universities:
            # Format the list for better readability
            st.write("-", item)
    else:
        st.header("Please enter the course name to study.")  


    # Displaying Places to Visit and Things to Eat side by side
    # col1, col2 = st.columns(2)

    # with col1:
    #     st.header("Places to Visit")
    #     for place in places[:5]:
    #         st.write("- ", place)

    # with col2:
    #     st.header("Things to Eat")
    #     for eat in eats[:5]:
    #         st.write("- ", eat)

else:
    st.header("Enter the country name to study")


    

