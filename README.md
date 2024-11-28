# University Finder Using LangChain

**University Finder** is a simple web application designed to help users find universities or colleges offering specific courses in different countries or regions. The app integrates a backend powered by Google's Gemini model through LangChain, with a frontend built using Streamlit for an interactive user experience.

## Features

- **User Input**: Users can specify the country (or city/state) and the course they wish to study.
- **University Recommendations**: Provides a list of universities or colleges that offer the selected course in the specified location.
- **Interactive UI**: The application is built with Streamlit, ensuring a simple, responsive, and interactive interface.

## How It Works

### Frontend (Streamlit)
The frontend is developed using Streamlit, which collects user input for:
1. **Country/Region**: The user enters the country or region (including city or state) where they want to study.
2. **Course**: The user specifies the course they wish to pursue.

Once both inputs are entered, the frontend sends these details to the backend to retrieve relevant universities.

### Backend (LangChain with Google Gemini)
The backend handles the core functionality with LangChain and Google Gemini. Here's how it works:
1. **Inputs**: The backend receives the country and course information.
2. **Processing**: LangChain formats the request and queries the Google Gemini API.
3. **Response**: The Gemini model processes the query and returns a list of universities that offer the course in the given location.
4. **Display**: The backend sends a comma-separated list of university names back to the frontend for display.

### Example Workflow
- **Frontend**: The user enters **Germany** as the country and **Robotics** as the course.
- **Backend**: The backend processes this request using LangChain to query Google Gemini, which returns a list of universities offering robotics programs in Germany.
- **Frontend**: The application displays a list of university names for the user.

## Requirements

To run this project locally, you'll need the following dependencies:

- Python 3.7 or later
- Streamlit
- LangChain
- `google-generativeai`
- `langchain-google-genai`
- API key for Google Gemini

## Setup

Follow these steps to get the project running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/university-finder.git
   cd university-finder

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

3. **Set up your Google API key**:

   - Go to the Google Cloud Console.
   - Create a new project and enable the Gemini API.
   - Set the environment variable for the API key:
   ```bash
   export GOOGLE_API_KEY="your_google_api_key"

4. **Run the Streamlit app**:
   ```bash
   streamlit run Langchain_application.py

The app will open in your browser, and you can begin using it to find universities offering your chosen course.

## Example Usage

### Frontend:
- The user enters **Germany** as the country and **Robotics** as the course.
- The app displays a list of universities in Germany that offer a robotics program.

### Backend:
- The inputs are sent to the Google Gemini API via LangChain.
- The Gemini model processes the request and returns a list of university names.

### Frontend:
- The list of universities is shown on the frontend as a comma-separated list.

## Future Enhancements

- **User Reviews**: Add user-generated reviews or ratings for each university.
- **Additional Features**: Allow users to search for things to do or places to eat in the area where the university is located.
- **Expanded Data**: Integrate more detailed information about each university, such as programs, campus details, and admission requirements.

## License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

## Contribution

Feel free to contribute by opening issues or submitting pull requests. If you have any questions or suggestions, don't hesitate to reach out!





 
