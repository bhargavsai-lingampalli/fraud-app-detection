import streamlit as st
import fraud_detection


def model_prediction(appid, n=1000):
    return fraud_detection.predict(appid, n)


# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Fraud App Detection"])

# Main Page
if app_mode == "Home":
    st.header("FRAUD APP DETECTION USING SENTIMENT ANALYSIS")
    image_path = "frontend/homepage.jpg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Fraud App Detection System! 🔍🛡️
    
    Our mission is to help you identify potential fraud in mobile applications quickly and accurately. By entering the \
    link of an app, our system will analyze it to detect any suspicious activity or fraudulent elements. Together, \
    let's ensure a safer digital environment!
    
    ### How It Works
    1. **Enter App Link:** Navigate to the **Fraud Detection** page and input the link of the app you wish to analyze.
    2. **Analysis:** Our advanced algorithms will process the app link, examining it for known fraud patterns and vulner\
    abilities.
    3. **Results:** View the analysis results along with recommendations for safeguarding against potential threats.
    
    ### Why Choose Us?
    - **High Accuracy:** We leverage cutting-edge machine learning techniques for reliable fraud detection.
    - **User-Friendly:** Our interface is designed to be intuitive and straightforward, making it easy for anyone to use.
    - **Quick Results:** Get insights in seconds, enabling prompt action to mitigate risks.
    
    ### Get Started
    Click on the **Fraud Detection** page in the sidebar to enter an app link and harness the power of our Fraud App Detection System!
    
    ### About Us
    Discover more about our project, meet the team, and learn about our vision on the **About** page.
    """)

# About Project
elif app_mode == "About":
    st.header("About")
    st.markdown("""
        # About Us

        Welcome to the Fraud App Detection System! Our goal is to empower users by providing advanced tools for identifying potential fraud in mobile applications. 
        
        ## Our Technology
        We utilize **Python** as the core programming language for our application, leveraging its powerful libraries and frameworks to ensure efficiency and accuracy. Our system employs **sentiment analysis** techniques to analyze user reviews and predict the likelihood of fraudulent activity. By examining patterns in user feedback, we can uncover red flags that may indicate fraud.
        
        ### How Sentiment Analysis Works
        - **Data Collection:** We gather user reviews from various sources, creating a comprehensive dataset.
        - **Natural Language Processing (NLP):** Our algorithms process the text, extracting meaningful insights and sentiment scores.
        - **Prediction:** By analyzing sentiment trends, we can identify potential issues within an app, helping users make informed decisions.
        
        ## Our Team
        We are a passionate team of developers and data scientists dedicated to enhancing app security and user trust in the digital marketplace. Our diverse backgrounds and expertise in machine learning, data analysis, and software development drive our commitment to innovation.
        
        ## Our Vision
        We believe in a safer online environment where users can confidently engage with mobile applications. Through our Fraud App Detection System, we aim to provide tools that enhance transparency and protect consumers from potential fraud.
        
        Thank you for choosing us on this journey towards safer digital experiences!
                """)

# Prediction Page
elif app_mode == "Fraud App Detection":
    st.header("Fraud App Detection")
    test_text = st.text_input("Enter: ", "")

    # Predict button
    if st.button("Predict"):
        try:
            st.snow()
            st.write("Our Prediction")
            result = model_prediction(test_text)
            # Reading Labels
            st.success(f"Model is Predicting it's {result[0]}\n\n{result[1]}")
        except Exception as e:
            st.success("Invalid Link!")
