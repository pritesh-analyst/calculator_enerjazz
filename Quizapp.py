import streamlit as st
import random

# Define the dictionary with questions and options
Ques = {
    "Bharat Natyam": ["Rukmani Devi Arundel","Leela Samson","Mrilani Sarabhai","Bejyanti Mala","Komal vardhan","T. bal sarasabati","Padma Subramanyam","S.K Saroj",
                      "M.K Saroja","Ramgopal","Priyadarshini govind","Malvika Sarkar","C.B Chandrasekhar","B.P dhananjayan","Shanta","Minakshi Shrinivasan","Gita chandran",
                      "Anand Shankar Jayant","Alarmel velli","Nartaki natraj","R.Mathukannmal"],
    "Kuchipudi": ["Yamini Krishanmurti","Laxmi narayan shastri","Radha reddi","Raja reddi","Padama reddi","Vedantum satyanarayan","Vempatti chitrasatyam","Mallika sarabhai",
                  "Aparna sathisan","Swapn sundri","Sobha naydu","Haleem Khan","Sidderdra Yogi"]


    "Odissi": ["Kelucharan Mahapatra", "Madhvi mudgal", "Harekrishan behra", "Sonal mansingh", "Kiran sehgal", "Rani karn", "Sanyukt panigrahi", "Kalicharan patnayak", "Indrani rehman", 
               "Mohan mahapatra", "Sujata mahapatra", "Minati mishra", "Kumkum mohanti", Gangadhar pradhan", Durgacharan ranvir"],
    # "Manipuri": ["M", "N"],
    # "Mohiniattam": ["O", "P", "Q"],
    # "Kathakali": ["R", "S", "T"],
    # "Kathak": ["U", "V", "W"],
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
    other_options = other_options[:3]
    
    # Combine correct answer and other options
    all_options = [correct_answer] + other_options
    
    # Shuffle all options
    random.shuffle(all_options)
    
    return dance_form, all_options, correct_answer

def main():
    st.title('Classical Dance Quiz')
    st.markdown('Select the correct dance form for each question.')
    
    if 'next_question' not in st.session_state:
        st.session_state.next_question = True

    if st.session_state.next_question:
        st.session_state.dance_form, st.session_state.options, st.session_state.correct_answer = get_next_question()
        st.session_state.user_answer = None
        st.session_state.feedback = None
        st.session_state.next_question = False
    
    # Display the current question and options
    st.subheader(f"Who is the Dancer that belongs to '{st.session_state.dance_form}' ?")
    
    # Display options as radio buttons if user_answer is None
    user_answer = st.radio('Your Choices:', st.session_state.options)
    
    # Display Submit button if the answer hasn't been submitted yet
    if st.button('Submit') and st.session_state.user_answer is None:
        # Check the answer and provide feedback
        st.session_state.user_answer = user_answer
        st.session_state.feedback = 'Correct!' if st.session_state.user_answer == st.session_state.correct_answer else f"Incorrect. The correct answer is {st.session_state.correct_answer}"
    
    # Display feedback and next button if the answer has been submitted
    if st.session_state.feedback:
        st.write(st.session_state.feedback)
        
        if st.button('Next'):
            st.session_state.next_question = True
            st.experimental_rerun()  # Force rerun to update state immediately

if __name__ == '__main__':
    main()
