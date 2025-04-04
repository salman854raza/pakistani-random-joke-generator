import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://pakistani-jokes-api.vercel.app/random-joke")
        # ("http://localhost:8000/random-joke")
        # ("https://official-joke-api.appspot.com/jokes/random")
        # ("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "Why did the programmer quit his job? \n because he didn't get arrays!"
    
def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to generate a random joke")

    if st.button("Generate a Joke!"):
        joke = get_random_joke()
        st.success(joke)

    st.divider()

    st.markdown(
        """
    <div style='text-align:center;'>
        <p>Joke from official joke API</p>
        <p>Build with ♥ by <a href='https://github.com/salman854raza'>Salman Raza</a> using Streamlit </p>
    </div>
""", 
        unsafe_allow_html=True
    )

    

if __name__ == "__main__":
    main()