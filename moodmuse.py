import streamlit as st
import random

# ---------------------- App Configuration ----------------------
st.set_page_config(page_title="MoodMuse", page_icon="🎵", layout="centered")

# ---------------------- App Title ----------------------
st.title("🎧 MoodMuse Ultra")
st.subheader("Let your feelings take the stage — pick a mood, get a vibe, and ride the feels! 🎭🎶💜")
st.write("Pick a category, search your vibe, and let MoodMuse reflect your emotional universe 💜")

# ---------------------- Categorized Mood Map ----------------------
categorized_moods = {
    "Mental Health": {
        "😰 Anxious": {"quote": "You don’t have to control your thoughts. You just have to stop letting them control you. – Dan Millman", "song": "Weightless by Marconi Union", "youtube": "https://www.youtube.com/watch?v=UfcAVejslrU", "bgcolor": "#F3E5F5", "image": "https://media.giphy.com/media/ToMjGpP5t9vKjeGniyQ/giphy.gif"},
        "😭 Heartbroken": {"quote": "The emotion that can break your heart is sometimes the very one that heals it.", "song": "Back to December by Taylor Swift", "youtube": "https://www.youtube.com/watch?v=QUwxKWT6m7U", "bgcolor": "#F8BBD0", "image": "https://media.giphy.com/media/1BXa2alBjrCXC/giphy.gif"},
        "😓 Stressed": {"quote": "You can't control everything. Sometimes you just need to relax and trust the process.", "song": "Breathe by Taylor Swift", "youtube": "https://www.youtube.com/watch?v=Zlot0i3Zykw", "bgcolor": "#FFE0B2", "image": "https://media.giphy.com/media/l3V0j3ytFyGHqiV7W/giphy.gif"},
        "😵‍💫 Burnt Out": {"quote": "Almost everything will work again if you unplug it for a few minutes, including you.", "song": "Creep by Radiohead", "youtube": "https://www.youtube.com/watch?v=XFkzRNyygfk", "bgcolor": "#EFEBE9", "image": "https://media.giphy.com/media/3o7TKV4NxlB3zSn28A/giphy.gif"},
        "🥱 Tired": {"quote": "Rest when you're weary. Refresh and renew yourself.", "song": "Breathe Me by Sia", "youtube": "https://www.youtube.com/watch?v=wbP0c5xTNRg", "bgcolor": "#ECEFF1", "image": "https://media.giphy.com/media/3orieXHf4o3nSP3zW0/giphy.gif"},
    },
    "Energy & Productivity": {
        "💪 Motivated": {"quote": "The future depends on what you do today. – Mahatma Gandhi", "song": "Stronger by Kanye West", "youtube": "https://www.youtube.com/watch?v=PsO6ZnUZI0g", "bgcolor": "#E8F5E9", "image": "https://media.giphy.com/media/l41Yg5P3F5G4a7HnG/giphy.gif"},
        "🏃‍♀️ Energetic": {"quote": "Energy and persistence conquer all things. – Benjamin Franklin", "song": "Can't Stop the Feeling! by Justin Timberlake", "youtube": "https://www.youtube.com/watch?v=ru0K8uYEZWw", "bgcolor": "#F1F8E9", "image": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"},
        "👩‍💻 Productive": {"quote": "The way to get started is to quit talking and begin doing. – Walt Disney", "song": "Work by Rihanna", "youtube": "https://www.youtube.com/watch?v=HL1UzIK-flA", "bgcolor": "#DCEDC8", "image": "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"},
        "🧠 Focused": {"quote": "Starve your distractions, feed your focus.", "song": "Power by Kanye West", "youtube": "https://www.youtube.com/watch?v=L53gjP-TtGE", "bgcolor": "#E3F2FD", "image": "https://media.giphy.com/media/l3q2wJsC23ikjzC7y/giphy.gif"},
        "😴 Sleepy": {"quote": "A good laugh and a long sleep are the best cures.", "song": "Asleep by The Smiths", "youtube": "https://www.youtube.com/watch?v=4B7ypA1M4xM", "bgcolor": "#E0F2F1", "image": "https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif"},
    },
        "Nature & Serenity": {
        "🌊 Flowing": {"quote": "Go with the flow. Let the rhythm guide you.", "song": "Ocean Eyes by Billie Eilish", "youtube": "https://www.youtube.com/watch?v=viimfQi_pUw", "bgcolor": "#E0F7FA", "image": "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif"},
        "🌄 Grounded": {"quote": "Stay close to nature. It will never fail you.", "song": "Banana Pancakes by Jack Johnson", "youtube": "https://www.youtube.com/watch?v=6Graa_Vm5eA", "bgcolor": "#F1F8E9", "image": "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif"},
        "🌬️ Breezy": {"quote": "Sometimes the wind knows which direction to take.", "song": "Somewhere Only We Know by Keane", "youtube": "https://www.youtube.com/watch?v=Oextk-If8HQ", "bgcolor": "#E3F2FD", "image": "https://media.giphy.com/media/l0ExncehJzexFpRHq/giphy.gif"},
        "🍃 Fresh": {"quote": "A fresh start isn’t a place. It’s a mindset.", "song": "New Light by John Mayer", "youtube": "https://www.youtube.com/watch?v=2PH7dK6SLC8", "bgcolor": "#E8F5E9", "image": "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"},
        "🌞 Sunny": {"quote": "Keep your face to the sun and you cannot see a shadow. – Helen Keller", "song": "Here Comes the Sun by The Beatles", "youtube": "https://www.youtube.com/watch?v=KQetemT1sWc", "bgcolor": "#FFF9C4", "image": "https://media.giphy.com/media/fxsqOYnIMEefC/giphy.gif"}
    },
    "Bold & Brave": {
        "🧨 Explosive": {"quote": "Let the sparks fly. Unleash your energy.", "song": "Thunder by Imagine Dragons", "youtube": "https://www.youtube.com/watch?v=fKopy74weus", "bgcolor": "#FFEBEE", "image": "https://media.giphy.com/media/l2SpRt7iVj3r8Aq92/giphy.gif"},
        "🦁 Fearless": {"quote": "Do one thing every day that scares you. – Eleanor Roosevelt", "song": "Fight Song by Rachel Platten", "youtube": "https://www.youtube.com/watch?v=xo1VInw-SKc", "bgcolor": "#E1F5FE", "image": "https://media.giphy.com/media/3orieQzQW3t9MrA9Vu/giphy.gif"},
        "🚀 Ambitious": {"quote": "Shoot for the moon. Even if you miss, you’ll land among the stars.", "song": "Sky Full of Stars by Coldplay", "youtube": "https://www.youtube.com/watch?v=VPRjCeoBqrI", "bgcolor": "#E3F2FD", "image": "https://media.giphy.com/media/xUPGcF0YzJfOB6rjEA/giphy.gif"},
        "⚡ Bold": {"quote": "Fortune favors the bold.", "song": "Believer by Imagine Dragons", "youtube": "https://www.youtube.com/watch?v=7wtfhZwyrcc", "bgcolor": "#FFF3E0", "image": "https://media.giphy.com/media/26FL1soZ3STRDSLGU/giphy.gif"},
        "🥊 Competitive": {"quote": "Push yourself because no one else is going to do it for you.", "song": "Remember the Name by Fort Minor", "youtube": "https://www.youtube.com/watch?v=VDvr08sCPOc", "bgcolor": "#FBE9E7", "image": "https://media.giphy.com/media/xT9IgIc0lryrxvqVGM/giphy.gif"}
    },
    "Social & Playful": {
        "🕺 Party Mode": {"quote": "Life’s too short to not dance in your room alone.", "song": "24K Magic by Bruno Mars", "youtube": "https://www.youtube.com/watch?v=UqyT8IEBkvY", "bgcolor": "#FFF8E1", "image": "https://media.giphy.com/media/3o6ZthU1eI0zY0KfQs/giphy.gif"},
        "😹 Goofy": {"quote": "Being silly is a superpower.", "song": "Happy by Pharrell", "youtube": "https://www.youtube.com/watch?v=ZbZSe6N_BXs", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/3orieZCbn2vYkz9Fh6/giphy.gif"},
        "🍕 Chill": {"quote": "Stay cool. Stay calm. Stay you.", "song": "Sunday Best by Surfaces", "youtube": "https://www.youtube.com/watch?v=YrtANPtnhyg", "bgcolor": "#E0F2F1", "image": "https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif"},
        "🎤 Karaoke Time": {"quote": "Sing like no one’s listening.", "song": "Shallow by Lady Gaga & Bradley Cooper", "youtube": "https://www.youtube.com/watch?v=bo_efYhYU2A", "bgcolor": "#F3E5F5", "image": "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif"},
        "🎮 Nerdy": {"quote": "Embrace your inner geek. Nerds run the world.", "song": "The Middle by Jimmy Eat World", "youtube": "https://www.youtube.com/watch?v=oKsxPW6i3pM", "bgcolor": "#E8EAF6", "image": "https://media.giphy.com/media/3o6Zt0R1FQ5GQy5qWs/giphy.gif"}
    },
      "Relationships": {
        "❤️ Romantic": {"quote": "Love is composed of a single soul inhabiting two bodies. – Aristotle", "song": "Perfect by Ed Sheeran", "youtube": "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/xT0BKmtQGLbumr5RCM/giphy.gif"},
        "😔 Lonely": {"quote": "The greatest thing in the world is to know how to belong to oneself. – Michel de Montaigne", "song": "Someone Like You by Adele", "youtube": "https://www.youtube.com/watch?v=hLQl3WQQoQ0", "bgcolor": "#ECEFF1", "image": "https://media.giphy.com/media/XreQmk7ETCak0/giphy.gif"},
        "🥹 Emotional": {"quote": "Feelings are much like waves, we can’t stop them but we can choose which ones to surf.", "song": "Jealous by Labrinth", "youtube": "https://www.youtube.com/watch?v=50VWOBi0VFs", "bgcolor": "#F8BBD0", "image": "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif"},
        "🫣 Embarrassed": {"quote": "Embarrassment is just a step toward growth. Own your awkward.", "song": "Apologize by OneRepublic", "youtube": "https://www.youtube.com/watch?v=ZSM3w1v-A_Y", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/d2Z9QYzA2aidiWn6/giphy.gif"}
    },

    "Introspective": {
        "😇 Hopeful": {"quote": "Hope is being able to see that there is light despite all of the darkness.", "song": "Rise Up by Andra Day", "youtube": "https://www.youtube.com/watch?v=lwgr_IMeEgA", "bgcolor": "#E1F5FE", "image": "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif"},
        "💭 Reflective": {"quote": "The unexamined life is not worth living. – Socrates", "song": "Holocene by Bon Iver", "youtube": "https://www.youtube.com/watch?v=TWcyIpul8OE", "bgcolor": "#EDE7F6", "image": "https://media.giphy.com/media/xT9DPqd5W0v8Z3A9PG/giphy.gif"},
        "🤍 Self-Loving": {"quote": "Love yourself first and everything else falls into line.", "song": "Love Myself by Hailee Steinfeld", "youtube": "https://www.youtube.com/watch?v=bMpFmHSgC4Q", "bgcolor": "#F3E5F5", "image": "https://media.giphy.com/media/xT9DPpf0zTqRASyzTi/giphy.gif"},
        "👻 Nostalgic": {"quote": "Sometimes you will never know the value of a moment until it becomes a memory.", "song": "Good Old Days by Macklemore", "youtube": "https://www.youtube.com/watch?v=1yYV9-KoSUM", "bgcolor": "#F3E5F5", "image": "https://media.giphy.com/media/3oKIPwoeGErMmaI43C/giphy.gif"}
    },

    "Fun & Random": {
        "🎉 Celebrating": {"quote": "Celebrate every win, no matter how small.", "song": "Celebrate by Kool & The Gang", "youtube": "https://www.youtube.com/watch?v=3GwjfUFyY6M", "bgcolor": "#FFF8E1", "image": "https://media.giphy.com/media/13ZHjidRzoi7n2/giphy.gif"},
        "😆 Silly": {"quote": "A day without laughter is a day wasted. – Charlie Chaplin", "song": "I'm Yours by Jason Mraz", "youtube": "https://www.youtube.com/watch?v=EkHTsc9PU2A", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif"},
        "🤯 Mind-Blown": {"quote": "New ideas are only scary until you explore them.", "song": "Technologic by Daft Punk", "youtube": "https://www.youtube.com/watch?v=RYQUsp-jxDQ", "bgcolor": "#FFF8E1", "image": "https://media.giphy.com/media/3og0IOUWBv9QwhMuOI/giphy.gif"},
        "🎭 Dramatic": {"quote": "Sometimes, life is just one big stage.", "song": "Bad Guy by Billie Eilish", "youtube": "https://www.youtube.com/watch?v=DyDfgMOUjCI", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/xUOxf48TSAxXZTJ9Is/giphy.gif"},
        "🤠 Playful": {"quote": "You don’t stop playing because you grow old; you grow old because you stop playing.", "song": "Sugar by Maroon 5", "youtube": "https://www.youtube.com/watch?v=09R8_2nJtjg", "bgcolor": "#FFF3E0", "image": "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif"},
        "🔥 Spicy": {"quote": "Add a little heat to life—spice things up!", "song": "Hotline Bling by Drake", "youtube": "https://www.youtube.com/watch?v=uxpDa-c-4Mc", "bgcolor": "#FFECB3", "image": "https://media.giphy.com/media/l2SpN8fMEX0nRt3MY/giphy.gif"}, 
        "🥶 Frozen": {"quote": "Some days are for stillness. Breathe in the quiet.", "song": "Let It Go by Idina Menzel", "youtube": "https://www.youtube.com/watch?v=L0MK7qz13bU", "bgcolor": "#E1F5FE", "image": "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif"},
        "🧊 Cold": {"quote": "Even in winter, there is light within.", "song": "Sweater Weather by The Neighbourhood", "youtube": "https://www.youtube.com/watch?v=GCdwKhTtNNw", "bgcolor": "#E3F2FD", "image": "https://media.giphy.com/media/3oEduSbSGpGaRX2Vri/giphy.gif"},
        "👻 Nostalgic": {"quote": "Sometimes you will never know the value of a moment until it becomes a memory.", "song": "Good Old Days by Macklemore", "youtube": "https://www.youtube.com/watch?v=1yYV9-KoSUM", "bgcolor": "#F3E5F5", "image": "https://media.giphy.com/media/3oKIPwoeGErMmaI43C/giphy.gif"}
    },
        "All Moods": {
        "😊 Happy": {
            "quote": "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
            "song": "‘Happy’ by Pharrell Williams 🎶",
            "youtube": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "bgcolor": "#FFFDE7",
            "image": "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"
        },
        "😢 Sad": {
            "quote": "Tears come from the heart and not from the brain. – Leonardo da Vinci",
            "song": "‘Fix You’ by Coldplay 🎧",
            "youtube": "https://www.youtube.com/watch?v=k4V3Mo61fJM",
            "bgcolor": "#E3F2FD",
            "image": "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif"
        },
        "😰 Anxious": {
            "quote": "You don’t have to control your thoughts. You just have to stop letting them control you. – Dan Millman",
            "song": "‘Weightless’ by Marconi Union 🌊",
            "youtube": "https://www.youtube.com/watch?v=UfcAVejslrU",
            "bgcolor": "#F3E5F5",
            "image": "https://media.giphy.com/media/ToMjGpP5t9vKjeGniyQ/giphy.gif"
        },
        "😡 Angry": {
            "quote": "Speak when you are angry and you will make the best speech you will ever regret. – Ambrose Bierce",
            "song": "‘Demons’ by Imagine Dragons 🔥",
            "youtube": "https://www.youtube.com/watch?v=mWRsgZuwf_8",
            "bgcolor": "#FFEBEE",
            "image": "https://media.giphy.com/media/3o6MblJFbbVt2MXi4o/giphy.gif"
        },
        "😔 Lonely": {"quote": "The greatest thing in the world is to know how to belong to oneself. – Michel de Montaigne", "song": "‘Someone Like You’ by Adele 🌧️", "youtube": "https://www.youtube.com/watch?v=hLQl3WQQoQ0", "bgcolor": "#ECEFF1", "image": "https://media.giphy.com/media/XreQmk7ETCak0/giphy.gif"},
        "💪 Motivated": {"quote": "The future depends on what you do today. – Mahatma Gandhi", "song": "‘Stronger’ by Kanye West 💪", "youtube": "https://www.youtube.com/watch?v=PsO6ZnUZI0g", "bgcolor": "#E8F5E9", "image": "https://media.giphy.com/media/l41Yg5P3F5G4a7HnG/giphy.gif"},
        "❤️ Romantic": {"quote": "Love is composed of a single soul inhabiting two bodies. – Aristotle", "song": "‘Perfect’ by Ed Sheeran 💖", "youtube": "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/xT0BKmtQGLbumr5RCM/giphy.gif"},
        "😎 Confident": {"quote": "Believe in yourself and you will be unstoppable.", "song": "‘Confident’ by Demi Lovato 💪", "youtube": "https://www.youtube.com/watch?v=cwLRQn61oUY", "bgcolor": "#E0F7FA", "image": "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif"},
        "😇 Peaceful": {"quote": "Peace comes from within. Do not seek it without. – Buddha", "song": "‘Let It Be’ by The Beatles 🍃", "youtube": "https://www.youtube.com/watch?v=QDYfEBY9NM4", "bgcolor": "#F1F8E9", "image": "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif"},
        "🥱 Tired": {"quote": "Rest when you're weary. Refresh and renew yourself.", "song": "‘Breathe Me’ by Sia 🌙", "youtube": "https://www.youtube.com/watch?v=wbP0c5xTNRg", "bgcolor": "#ECEFF1", "image": "https://media.giphy.com/media/3orieXHf4o3nSP3zW0/giphy.gif"},
        "😐 Bored": {"quote": "Only the curious have something to find.", "song": "‘Counting Stars’ by OneRepublic 🌌", "youtube": "https://www.youtube.com/watch?v=hT_nvWreIhg", "bgcolor": "#FFF3E0", "image": "https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif"},
        "🧘 Calm": {"quote": "When you realize nothing is lacking, the whole world belongs to you.", "song": "‘Weightless’ by Marconi Union ☁️", "youtube": "https://www.youtube.com/watch?v=UfcAVejslrU", "bgcolor": "#E0F2F1", "image": "https://media.giphy.com/media/26n6WywJyh39n1pBu/giphy.gif"},
        "🔥 Spicy": {"quote": "Add a little heat to life—spice things up!", "song": "‘Hotline Bling’ by Drake 🌶️", "youtube": "https://www.youtube.com/watch?v=uxpDa-c-4Mc", "bgcolor": "#FFECB3", "image": "https://media.giphy.com/media/l2SpN8fMEX0nRt3MY/giphy.gif"},
        "🥶 Frozen": {"quote": "Some days are for stillness. Breathe in the quiet.", "song": "‘Let It Go’ by Idina Menzel ❄️", "youtube": "https://www.youtube.com/watch?v=L0MK7qz13bU", "bgcolor": "#E1F5FE", "image": "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif"},
        "🤯 Overwhelmed": {"quote": "You don’t have to do everything today. One step at a time.", "song": "‘The Climb’ by Miley Cyrus 🧗‍♀️", "youtube": "https://www.youtube.com/watch?v=NG2zyeVRcbs", "bgcolor": "#FBE9E7", "image": "https://media.giphy.com/media/d2Z9QYzA2aidiWn6/giphy.gif"},
        "😤 Frustrated": {"quote": "Frustration is the first step toward improvement.", "song": "‘Numb’ by Linkin Park ⚡", "youtube": "https://www.youtube.com/watch?v=kXYiU_JCYtU", "bgcolor": "#FFCDD2", "image": "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif"},
        "🤗 Grateful": {"quote": "Gratitude turns what we have into enough.", "song": "‘Thank You’ by Dido 🙏", "youtube": "https://www.youtube.com/watch?v=j-fWDrZSiZs", "bgcolor": "#FFFDE7", "image": "https://media.giphy.com/media/d31w24psGYeekCZy/giphy.gif"},
        "😆 Silly": {"quote": "A day without laughter is a day wasted. – Charlie Chaplin", "song": "‘I’m Yours’ by Jason Mraz 😜", "youtube": "https://www.youtube.com/watch?v=EkHTsc9PU2A", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif"},
        "🧠 Focused": {"quote": "Starve your distractions, feed your focus.", "song": "‘Power’ by Kanye West 🎯", "youtube": "https://www.youtube.com/watch?v=L53gjP-TtGE", "bgcolor": "#E3F2FD", "image": "https://media.giphy.com/media/l3q2wJsC23ikjzC7y/giphy.gif"},
        "🎨 Creative": {"quote": "The chief enemy of creativity is good sense. – Picasso", "song": "‘Chandelier’ by Sia 🎨", "youtube": "https://www.youtube.com/watch?v=2vjPBrBU-TM", "bgcolor": "#FFF3E0", "image": "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif"},
        "😬 Nervous": {"quote": "Everything you’ve ever wanted is on the other side of fear.", "song": "‘Shake It Out’ by Florence + The Machine 🌫️", "youtube": "https://www.youtube.com/watch?v=WbN0nX61rIs", "bgcolor": "#F3E5F5", "image": "https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif"},
        "🎉 Celebrating": {"quote": "Celebrate every win, no matter how small.", "song": "‘Celebrate’ by Kool & The Gang 🎊", "youtube": "https://www.youtube.com/watch?v=3GwjfUFyY6M", "bgcolor": "#FFF8E1", "image": "https://media.giphy.com/media/13ZHjidRzoi7n2/giphy.gif"},
        "🫣 Embarrassed": {"quote": "Embarrassment is just a step toward growth. Own your awkward.", "song": "‘Apologize’ by OneRepublic 😳", "youtube": "https://www.youtube.com/watch?v=ZSM3w1v-A_Y", "bgcolor": "#FCE4EC", "image": "https://media.giphy.com/media/d2Z9QYzA2aidiWn6/giphy.gif"}
    }
}

# ---------------------- View Mode ----------------------
view_mode = st.radio("🔄 Browse Mode:", ["By Category", "All Moods"], horizontal=True)

if view_mode == "By Category":
    category = st.selectbox("📂 Choose a category:", [""] + [c for c in categorized_moods if c != "All Moods"])
    if category:
        moods = categorized_moods[category]
        search_term = st.text_input("🔍 Search a mood from this category:", "")
    else:
        moods = {}
        search_term = ""
else:
    moods = categorized_moods["All Moods"]
    category = "All Moods"
    search_term = st.text_input("🔍 Search any mood:", "")

mood_options = [m for m in moods if search_term.lower() in m.lower()]

if not mood_options:
    st.warning("No matching moods found.")
else:
    selected_mood = st.selectbox("💬 Choose your mood:", [""] + mood_options)

    if selected_mood:
        data = moods[selected_mood]

        if "celebrating" in selected_mood.lower():
            st.balloons()
        elif any(word in selected_mood.lower() for word in ["sad", "heartbroken", "lonely"]):
            st.snow()
        elif any(word in selected_mood.lower() for word in ["motivated", "bold", "confident", "ambitious"]):
            st.toast("🔥 You’re on fire today!", icon="💥")
        elif any(word in selected_mood.lower() for word in ["grateful", "peaceful", "calm"]):
            st.toast("🕊️ Inner peace achieved.", icon="🧘")
        elif "creative" in selected_mood.lower():
            st.toast("🎨 Creative burst unlocked!", icon="🌈")
        elif "nervous" in selected_mood.lower():
            st.toast("😌 Take a breath. You got this!", icon="💫")
        elif "bored" in selected_mood.lower():
            st.toast("🎲 Time to shake things up!", icon="🎮")
        elif "angry" in selected_mood.lower():
            st.toast("😤 Deep breath... let it go.", icon="🧯")
        elif "focused" in selected_mood.lower():
            st.toast("🎯 Locked in and unstoppable.", icon="🚀")
        elif "playful" in selected_mood.lower():
            st.toast("🤸 Let’s have some fun!", icon="🎈")
        elif "spicy" in selected_mood.lower():
            st.toast("🌶️ Hot stuff coming through!", icon="🔥")
        elif "embarrassed" in selected_mood.lower():
            st.toast("😳 It happens to the best of us.", icon="💞")
        elif "hopeful" in selected_mood.lower():
            st.toast("🌅 A brighter day is coming.", icon="🌈")
        elif "overwhelmed" in selected_mood.lower():
            st.toast("📦 One step at a time. You got this.", icon="📘")

        st.markdown(f"""<style>.stApp {{background-color: {data['bgcolor']};}}</style>""", unsafe_allow_html=True)
        st.image(data["image"], use_container_width=True)
        st.success("Here's something to match your mood 🎁")
        st.markdown(f"### 💡 Quote:\n> *{data['quote']}*")
        st.markdown(f"### 🎵 Now Playing:\n**{data['song']}**")
        st.video(data["youtube"])

        st.markdown("""
        <a href="https://open.spotify.com/search/{0}" target="_blank">
            <button style="margin-top: 10px; background-color:#1DB954; color:white; padding:10px 16px; font-size:16px; border:none; border-radius:8px; cursor:pointer;">🎧 Explore on Spotify</button>
        </a>
        """.format(selected_mood.replace(" ", "%20")), unsafe_allow_html=True)

        gratitude = st.text_area("💌 What's one thing you're grateful for today?")
        if gratitude:
            st.markdown(f"✅ _“{gratitude}”_ – Beautiful reflection 💜")

        share_msg = f"MoodMuse Vibe 🎧\nMood: {selected_mood}\nQuote: \"{data['quote']}\"\nNow playing: {data['song']}"
        st.text_area("📋 Copy & Share this vibe:", value=share_msg, height=150)

        if st.button("🔁 Try Another Mood"):
            st.rerun()

# ---------------------- Footer ----------------------
st.markdown("---")
st.caption("🚀 Made with 💜 by Ranjani · MoodMuse · 2025")
