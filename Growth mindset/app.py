import streamlit as st

       
st.set_page_config(page_title="Growth Mindset Project",page_icon="✨")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to the Growth Mindset Challenge! 🚀")
st.write("Embrace Challenges,Learn from Mistakes,Persist Through Difficulties,IFind Lessons and Inspiration in the Success of Others")

# Quote
st.header("💡Today's Growth Mindset Quote")
st.write("Every challenge is a chance to grow, and every mistake is a lesson. Keep learning, keep improving, and success will follow! 🌱✨")

st.header("What's Your Challenge Today?")
# input field for challenge
user_input=st.text_input("Describe a challenge you're facing today:")

# conditions
if user_input:
    st.success(f"You are facing:{user_input}. Keep pushing forward towards your goals! 🚀")
else:
    st.warning("Tell us about a challenge to get started! 🌟")

# Reflecting
st.header("Reflect on your challenge!")
# Input field for challenge
reflection=st.text_input("What did you learn from this challenge?")

# condition
if reflection:
    st.success(f"🌟 Great insight! Keep learning and growing!{reflection} 🌱✨")
else:
    st.warning("Reflecting on past challenges can help you grow! 🌟 Share your difficulties")

    # Motivation    
st.header("🌟 Motivation")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.– Winston Churchill")
    
    # achievements 
st.header("🏆 Celebrate Your Achievements!")
achievement=st.text_input("Share something you have recently achieved:")

if achievement:
     st.success(f"Congratulations! on your achievement! 🎉🌟{achievement}")
else:
        st.info("🎉Share your wins, no matter how big or small! 🤩")    


button= st.button("submit")
if button:
           st.write("Thank you for sharing your thoughts")
           st.balloons()
           st.write("Keep pushing forward towards your goals! 🚀")

        # footer
        
st.write("Keep believing yourself. You are capable of amazing things! 🌟✨")
st.markdown("""
Created with ❤️ by [Warisha Naz]


   
