import streamlit as st
from services.persistence.exercise_repository import get_or_create_user,create_user
def render_login_wall():

    if "user_id" in st.session_state:
        return True
    st.markdown('''
        <style>
        .outercontainer{
            margin-top:15vh;
            animation:reveal 4s ease-in 0s 1 forwards;
        }

        @keyframes reveal{
            0%{
                margin-top:100vh;
            }
            100%{
                margin-top:10vh;
            }
        }
        @keyframes reveal2{
            0%{
                margin-top:100vh;
            }
            100%{
                margin-top:-5vh;
            }
        }
        @media (max-width:768px){
            .outercontainer{
                margin-top:-5vh;
            animation:reveal2 4s ease-in 0s 1 forwards;
        }
            }
            
        }
        </style>

        <div class="outercontainer" style="display:flex;justify-content:center;">
            <div style="color:black;">
                <h2 style="font-size:4rem;text-align:center;color:white;">
                    Alpha<span style="font-size:4rem;color:red;font-family:serif;">Rep
                    </span>
                </h2>
                <p style="font-family:serif;font-size:2rem;color:grey;">
                    Your Personal AI Gym Trainer
                </p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown("## Please Login To Take Out Beast From You...")
    with st.form("Login With AlphaRep"):
        name = st.text_input("Enter Your Name To begin Session",placeholder="Enter Your Name Eg:-Aaquib khilji",type="default")
        password = st.text_input("Enter Your Password (if you are new User Just Enter Your new Password)",type="password",placeholder="Enter Your Password")
        submit_button = st.form_submit_button("Start Session")
        st.markdown("""
<script>
const observer = new MutationObserver(() => {

    const inputs = window.parent.document.querySelectorAll('input');

    inputs.forEach((input)=>{

        input.setAttribute("autocomplete","off");
        input.setAttribute("autocorrect","off");
        input.setAttribute("autocapitalize","off");
        input.setAttribute("spellcheck","false");

    });

});

observer.observe(
    window.parent.document.body,
    {
        childList:true,
        subtree:true
    }
);
</script>
""", unsafe_allow_html=True)
    if submit_button:
        if name and password:

            user = get_or_create_user(name, password)

            if user is not None:
                st.session_state["user_id"] = user["id"]
                st.session_state["username"] = user["username"]
                st.rerun()

            else:
                st.error(
                    "⚠️ An account with this username already exists. "
                    "Please enter the correct password or choose a different username."
                )

        else:
            st.error("Please enter Both Fields.")
    return False