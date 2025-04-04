import streamlit as st
import random

# List of Pakistani-themed Urdu jokes (since no public API is available)
urdu_jokes = [
    {
        "setup": "ایک پاکستانی نے اپنے دوست سے پوچھا: 'تمہاری بیوی اتنی خاموش کیوں رہتی ہے؟'",
        "punchline": "دوست بولا: 'وہ بولتی تو ہے، لیکن میں سنتا نہیں!'"
    },
    {
        "setup": "پاکستان میں بجلی کیوں جاتی ہے؟",
        "punchline": "کیونکہ بجلی کو بھی لنچ بریک چاہیے!"
    },
    {
        "setup": "ایک بندہ اپنے بچے سے: 'بیٹا، پڑھائی کیوں نہیں کرتے؟'",
        "punchline": "بچہ بولا: 'بابا، واٹس ایپ پر سب کچھ مل جاتا ہے!'"
    },
    {
        "setup": "پاکستانی ڈرائیور سے پوچھا: 'تم اتنی سپیڈ سے گاڑی کیوں چلاتے ہو؟'",
        "punchline": "وہ بولا: 'جلدی گھر جانا ہے، ورنہ بجلی چلی جائے گی!'"
    },
    {
        "setup": "ایک بندے نے دوسرے سے پوچھا: 'تمہارا پسندیدہ کھانا کیا ہے؟'",
        "punchline": "دوسرا بولا: 'جو مفت ملے!'"
    }
]

def get_random_joke():
    """Fetch a random Urdu joke from the list"""
    try:
        # Randomly select a joke from the list
        joke = random.choice(urdu_jokes)
        return f"{joke['setup']} \n\n {joke['punchline']}"
    except:
        # Fallback joke in case something goes wrong
        return "ایک بندہ بولا: 'میں بہت مصروف ہوں!' \n\n دوسرا بولا: 'واٹس ایپ پر تو نہیں لگتا!'"

def main():
    # Set page configuration for a wider layout and custom title
    st.set_page_config(page_title="پاکستانی جوک جنریٹر", layout="centered")

    # Custom CSS for a powerful and appealing UI
    st.markdown("""
        <style>
        .title {
            font-size: 40px;
            color: #2E8B57;
            text-align: center;
            font-family: 'Noto Nastaliq Urdu', serif;
        }
        .subtitle {
            font-size: 20px;
            color: #555555;
            text-align: center;
            font-family: 'Noto Nastaliq Urdu', serif;
        }
        .joke-box {
            background-color: #F0FFF0;
            padding: 20px;
            border-radius: 10px;
            font-size: 18px;
            font-family: 'Noto Nastaliq Urdu', serif;
            text-align: right;
            direction: rtl;
        }
        .button {
            background-color: #2E8B57;
            color: white;
            font-size: 18px;
            font-family: 'Noto Nastaliq Urdu', serif;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown('<p class="title">پاکستانی جوک جنریٹر</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">بٹن دبائیں اور ہنسی سے لطف اٹھائیں!</p>', unsafe_allow_html=True)

    # Button to generate a joke
    if st.button("نیا جوک بنائیں!", key="generate", help="ایک نیا جوک حاصل کریں"):
        joke = get_random_joke()
        st.markdown(f'<div class="joke-box">{joke}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="joke-box">یہاں آپ کا جوک نظر آئے گا!</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()