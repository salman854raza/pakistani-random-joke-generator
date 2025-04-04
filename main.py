import streamlit as st
import requests

# Custom CSS for better styling
st.markdown("""
<style>
    .joke-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #6c757d;
    }
    .setup {
        font-weight: bold;
        color: #343a40;
        font-size: 1.1em;
    }
    .punchline {
        font-style: italic;
        color: #495057;
        margin-top: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

def get_random_joke():
    """Fetch a random Urdu joke from the FastAPI backend"""
    try:
        response = requests.get("https://pakistani-jokes-api.vercel.app/random-joke")
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def main():
    st.title("🇵🇰 Pakistani Joke Generator")
    st.markdown("Experience authentic Pakistani humor with just one click!")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Get New Joke", key="generate_btn"):
            st.session_state.joke = get_random_joke()
    
    with col2:
        if st.button("Clear", type="secondary"):
            if 'joke' in st.session_state:
                del st.session_state.joke
    
    st.divider()
    
    if 'joke' in st.session_state and st.session_state.joke:
        joke = st.session_state.joke
        st.markdown(f"""
        <div class="joke-box">
            <div class="setup">🎭 {joke['setup']}</div>
            <div class="punchline">💥 {joke['punchline']}</div>
        </div>
        """, unsafe_allow_html=True)
    elif 'joke' in st.session_state:
        st.warning("Couldn't fetch a joke. Try again!")
    
    st.divider()
    
    # Footer
    st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        <p>Built with ♥ by <a href='https://github.com/salman854raza' target='_blank'>Salman Raza</a></p>
        <p>API: <a href='https://pakistani-jokes-api.vercel.app/docs' target='_blank'>FastAPI Backend</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
