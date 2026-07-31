import streamlit as st
from datetime import datetime
import random

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CodeAlpha Chatbot",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: gray;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .status-box {
        text-align: center;
        padding: 8px;
        border-radius: 10px;
        background-color: rgba(0, 200, 100, 0.1);
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        color: gray;
        font-size: 13px;
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "name" not in st.session_state:
    st.session_state.name = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "message_count" not in st.session_state:
    st.session_state.message_count = 0


# =========================================================
# BOT RESPONSE FUNCTION
# =========================================================

def get_bot_response(user_message):

    message = user_message.lower().strip()
    name = st.session_state.name

    # Greetings
    if message in ["hello", "hi", "hey", "hii", "hello bot"]:

        responses = [
            f"Hello {name}! 👋 Nice to meet you.",
            f"Hi {name}! 😊 How can I help you?",
            f"Hey {name}! 👋 What's up?"
        ]

        return random.choice(responses)

    # How are you
    elif "how are you" in message:

        responses = [
            "I'm doing great! Thanks for asking. 😊",
            "I'm doing fantastic! How about you?",
            "All systems are running perfectly! 🤖"
        ]

        return random.choice(responses)

    # Who are you
    elif message in ["who are you", "tell me about yourself"]:

        return (
            "I'm **CodeAlpha Bot 🤖**, a rule-based chatbot "
            "built using Python and Streamlit for the "
            "**CodeAlpha Python Programming Internship**."
        )

    # Bot name
    elif message in [
        "what is your name",
        "what's your name",
        "your name"
    ]:

        return "My name is **CodeAlpha Bot 🤖**."

    # User name
    elif message in [
        "what is my name",
        "what's my name",
        "my name"
    ]:

        return f"Your name is **{name}**! 😄"

    # Creator
    elif message in [
        "who created you",
        "who made you",
        "who is your creator"
    ]:

        return (
            "I was created by **Siddhu** as part of the "
            "**CodeAlpha Python Programming Internship**. 👨‍💻"
        )

    # What can you do
    elif message in [
        "what can you do",
        "what do you do",
        "features"
    ]:

        return """
I can do a few things! 🤖

- 👋 Greet you
- 💬 Have a basic conversation
- 🧑 Remember your name during this session
- 🕐 Tell you the current time
- 📅 Tell you today's date
- 😂 Tell you a programming joke
- 💻 Talk about Python
- ℹ️ Tell you about myself
- ❓ Show available commands

Type **help** to see more.
"""

    # Python
    elif message in [
        "what is python",
        "tell me about python",
        "python"
    ]:

        return (
            "🐍 **Python** is a popular high-level programming language "
            "known for its simple syntax and readability. It is widely "
            "used in web development, automation, data science, "
            "machine learning, AI, and software development."
        )

    # Streamlit
    elif message in [
        "what is streamlit",
        "streamlit"
    ]:

        return (
            "🎈 **Streamlit** is an open-source Python framework "
            "that makes it easy to build interactive web applications "
            "for Python projects."
        )

    # Time
    elif message in [
        "time",
        "what time is it",
        "current time",
        "tell me the time"
    ]:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"🕐 The current time is **{current_time}**."

    # Date
    elif message in [
        "date",
        "what is the date",
        "today's date",
        "todays date",
        "current date"
    ]:

        current_date = datetime.now().strftime(
            "%A, %d %B %Y"
        )

        return f"📅 Today is **{current_date}**."

    # Thank you
    elif message in [
        "thank you",
        "thanks",
        "thank you bot",
        "thanks bot"
    ]:

        responses = [
            "You're welcome! 😊",
            "Happy to help! 😄",
            "Anytime! 🤖",
            f"You're welcome, {name}! 👋"
        ]

        return random.choice(responses)

    # Jokes
    elif message in [
        "tell me a joke",
        "joke",
        "programming joke"
    ]:

        jokes = [
            (
                "Why do programmers prefer dark mode? "
                "Because light attracts bugs! 🐛😂"
            ),
            (
                "Why did the programmer quit his job? "
                "Because he didn't get arrays! 😄"
            ),
            (
                "Why was the computer cold? "
                "Because it left its Windows open! 😂"
            ),
            (
                "There are 10 types of people in the world: "
                "those who understand binary and those who don't. 🤓"
            )
        ]

        return random.choice(jokes)

    # Help
    elif message in ["help", "commands"]:

        return """
### 🆘 Available Commands

Try asking me:

- `hello`
- `how are you`
- `who are you`
- `what is your name`
- `what is my name`
- `who created you`
- `what can you do`
- `what is python`
- `what is streamlit`
- `tell me a joke`
- `what time is it`
- `today's date`
- `thank you`
- `bye`

You can also use the **Quick Actions** in the sidebar.
"""

    # Goodbye
    elif message in [
        "bye",
        "goodbye",
        "see you",
        "exit"
    ]:

        return (
            f"Goodbye **{name}**! 👋 "
            "It was nice chatting with you. Have a wonderful day!"
        )

    # Unknown input
    else:

        responses = [
            (
                "Sorry, I don't understand that yet. 😅 "
                "Try typing **help** to see what I can answer."
            ),
            (
                "Hmm... I haven't learned that response yet. 🤔 "
                "Type **help** to see my available commands."
            ),
            (
                "I'm only a rule-based chatbot, so I don't understand "
                "everything yet. 🤖 Try typing **help**."
            )
        ]

        return random.choice(responses)


# =========================================================
# ADD QUICK MESSAGE
# =========================================================

def quick_message(message):

    timestamp = datetime.now().strftime("%I:%M %p")

    st.session_state.messages.append({
        "role": "user",
        "content": message,
        "time": timestamp
    })

    response = get_bot_response(message)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": datetime.now().strftime("%I:%M %p")
    })

    st.session_state.message_count += 1


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🤖 CodeAlpha Bot")

    st.caption("Your Python Virtual Assistant")

    st.divider()

    # User profile
    st.subheader("👤 User Profile")

    name_input = st.text_input(
        "Your Name",
        value=st.session_state.name,
        placeholder="Enter your name..."
    )

    if name_input:
        st.session_state.name = name_input.strip()

    st.divider()

    # Quick actions
    st.subheader("⚡ Quick Actions")

    if st.button(
        "👋 Say Hello",
        use_container_width=True
    ):
        quick_message("hello")
        st.rerun()

    if st.button(
        "🤖 About Bot",
        use_container_width=True
    ):
        quick_message("who are you")
        st.rerun()

    if st.button(
        "🐍 What is Python?",
        use_container_width=True
    ):
        quick_message("what is python")
        st.rerun()

    if st.button(
        "😂 Tell Me a Joke",
        use_container_width=True
    ):
        quick_message("tell me a joke")
        st.rerun()

    if st.button(
        "❓ Help",
        use_container_width=True
    ):
        quick_message("help")
        st.rerun()

    st.divider()

    # Statistics
    st.subheader("📊 Chat Statistics")

    st.metric(
        "Messages Sent",
        st.session_state.message_count
    )

    st.metric(
        "Total Chat Messages",
        len(st.session_state.messages)
    )

    st.divider()

    # Clear chat
    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.session_state.message_count = 0

        st.rerun()


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 CodeAlpha Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A Rule-Based Virtual Assistant built with Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="status-box">
        🟢 <b>CodeAlpha Bot is Online</b>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# REQUIRE USER NAME
# =========================================================

if not st.session_state.name:

    st.info(
        "👋 Welcome! Please enter your name in the sidebar "
        "to start chatting."
    )

    st.stop()


# =========================================================
# WELCOME MESSAGE
# =========================================================

if len(st.session_state.messages) == 0:

    st.markdown(
        f"""
### 👋 Hello {st.session_state.name}!

I'm **CodeAlpha Bot**, your virtual assistant.

You can ask me simple questions or type **help** to discover
what I can do.

Start the conversation below! 👇
"""
    )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        st.caption(message["time"])


# =========================================================
# CHAT INPUT
# =========================================================

user_input = st.chat_input(
    f"Message CodeAlpha Bot as {st.session_state.name}..."
)


if user_input:

    timestamp = datetime.now().strftime("%I:%M %p")

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": timestamp
    })

    st.session_state.message_count += 1

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_input)
        st.caption(timestamp)

    # Generate response
    bot_response = get_bot_response(user_input)

    bot_time = datetime.now().strftime("%I:%M %p")

    # Add bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response,
        "time": bot_time
    })

    # Display bot response
    with st.chat_message("assistant"):

        st.markdown(bot_response)
        st.caption(bot_time)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        CodeAlpha Basic Chatbot • Built with Python & Streamlit
        <br>
        Python Programming Internship Project
    </div>
    """,
    unsafe_allow_html=True
)
