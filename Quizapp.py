import streamlit as st
import random

# Define the dictionary with questions and options
Ques = {
    "Bharat Natyam": ["Rukmani Devi Arundel","Leela Samson","Mrilani Sarabhai","Bejyanti Mala","Komal vardhan","T. bal sarasabati","Padma Subramanyam","S.K Saroj",
                      "M.K Saroja","Ramgopal","Priyadarshini govind","Malvika Sarkar","C.B Chandrasekhar","B.P dhananjayan","Shanta","Minakshi Shrinivasan","Gita chandran",
                      "Anand Shankar Jayant","Alarmel velli","Nartaki natraj","R.Mathukannmal"],
    "Kuchipudi": ["Yamini Krishanmurti","Laxmi narayan shastri","Radha reddi","Raja reddi","Padama reddi","Vedantum satyanarayan","Vempatti chitrasatyam","Mallika sarabhai",
                  "Aparna sathisan","Swapn sundri","Sobha naydu","Haleem Khan","Sidderdra Yogi"],


    "Odissi": ["Kelucharan Mahapatra", "Madhvi mudgal", "Harekrishan behra", "Sonal mansingh", "Kiran sehgal", "Rani karn", "Sanyukt panigrahi", "Kalicharan patnayak", "Indrani rehman", 
               "Mohan mahapatra", "Sujata mahapatra", "Minati mishra", "Kumkum mohanti", "Gangadhar pradhan", "Durgacharan ranvir"],

    "Kathakali": ["Anand shivraman", "Krishnan kutti", "Balltol narayan menan"," Udaishankar","Krishan narayan", "Shantarav","Keejpadam kumaran nayar", "Chemancheri nayar"],
    
    "Kathak": ["Birju maharaj"," Lacchu maharaj", "Sukhdev maharaj","Sitara devi","Sobhna narayan","Chandralekha bindadin maharaj",
              "Acchan maharaj","Manjushree chatarji","Kalika prasad","Uma sharma","Prerna deshpanday","Nandni singh","Narayan prasad"]
    
    "Manipuri": ["Jhaveri behan","Darshna nayana subarn ranjana","Guru amliSingh","Guru amubi","Guru vipin singh","Nalkumar Singh",
                "L. vino devi","Charu mathur","Savita mehta","Nirmala mehta","Thambal yama","Rajkumar singhjeet singh"],
    # "Mohiniattam": ["O", "P", "Q"],
    
    
    # "Sattriya": ["X", "Y", "Z"]
}

def get_next_question():
    # Select a dance form randomly from the dictionary
    dance_form = random.choice(list(Ques.keys()))
    options = Ques[dance_form]
    
    correct_answer = random.choice(options)  # Randomly select one option as correct answer
    
    # Collect options from other keys
    other_options = []
    for key, value in Ques.items():
        if key != dance_form:
            other_options.extend(value)
    
    # Shuffle other options and pick 3
    random.shuffle(other_options)
    other_options = other_options[:7]
    
    # Combine correct answer and other options
    all_options = [correct_answer] + other_options
    
    # Shuffle all options
    random.shuffle(all_options)
    
    return dance_form, all_options, correct_answer


def main():
    st.title('Classical Dance Quiz')
    st.markdown('Select the correct dancer for each question.')
    
    if 'next_question' not in st.session_state:
        st.session_state.next_question = True

    if st.session_state.next_question:
        st.session_state.dance_form, st.session_state.options, st.session_state.correct_answer = get_next_question()
        st.session_state.user_answer = None
        st.session_state.feedback = None
        st.session_state.next_question = False
    
    # Display the current question and options
    st.subheader(f"Who is the dancer that belongs to '{st.session_state.dance_form}'?")
    
    # Display options as radio buttons if user_answer is None
    user_answer = st.radio('Your Choices:', st.session_state.options)
    
    # Display Submit button if the answer hasn't been submitted yet
    if st.button('Submit') and st.session_state.user_answer is None:
        # Check the answer and provide feedback
        st.session_state.user_answer = user_answer
        if st.session_state.user_answer == st.session_state.correct_answer:
            st.session_state.feedback = '<p style="background-color: green; padding: 10px; border-radius: 5px;"><b style="color: black;">Correct!</b></p>'
        else:
            st.session_state.feedback = f'<p style="background-color: lightcoral; padding: 10px; border-radius: 5px;"><b style="color: black;">Incorrect.</b> The correct answer is <b>{st.session_state.correct_answer}</b></p>'
    
    # Display feedback and next button if the answer has been submitted
    if st.session_state.feedback:
        st.markdown(st.session_state.feedback, unsafe_allow_html=True)
        
        if st.button('Next'):
            st.session_state.next_question = True
            st.experimental_rerun()  # Force rerun to update state immediately


if __name__ == '__main__':
    main()
