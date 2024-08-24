import streamlit as st
import pandas as pd
import random

# Initialize session state
if 'members' not in st.session_state:
    st.session_state.members = []
if 'present_players' not in st.session_state:
    st.session_state.present_players = []
if 'rest_queue' not in st.session_state:
    st.session_state.rest_queue = []
if 'visitor_players' not in st.session_state:
    st.session_state.visitor_players = []
if 'signed_out_players' not in st.session_state:
    st.session_state.signed_out_players = []

# Function to upload a CSV file for the member list
def upload_members():
    uploaded_file = st.file_uploader("Upload Member List (CSV)", type="csv")
    if uploaded_file is not None:
        members_df = pd.read_csv(uploaded_file)
        st.session_state.members = members_df.to_dict('records')
        st.success("Member list uploaded successfully!")

# Function to select present players for the day
def select_present_players():
    st.subheader("Select Players Present")
    all_players = [player['Name'] for player in st.session_state.members]
    present_players = st.multiselect("Select Players", all_players)
    if st.button("Confirm Players Present"):
        st.session_state.present_players = present_players
        st.success(f"Selected {len(present_players)} players for today's session.")

# Function to add visitor players
def add_visitor_player():
    st.subheader("Add Visitor Player")
    visitor_name = st.text_input("Visitor Name")
    if st.button("Add Visitor"):
        st.session_state.visitor_players.append(visitor_name)
        st.success(f"Visitor {visitor_name} added successfully!")

# Function to input court details
def input_court_details():
    st.subheader("Court Details")
    num_courts = st.number_input("Number of Courts", min_value=1, max_value=10, step=1)
    game_duration = st.selectbox("Game Duration", options=[10, 12, 14, 16])
    if st.button("Generate Court Assignments"):
        generate_court_assignments(num_courts, game_duration)

# Function to generate court assignments
def generate_court_assignments(num_courts, game_duration):
    players = st.session_state.present_players + st.session_state.visitor_players
    random.shuffle(players)  # Randomize player order
    rest_players = []
    court_assignments = {}
    
    for i in range(num_courts):
        court_assignments[f'Court {i+1}'] = players[i*4:(i+1)*4]  # Assign 4 players per court
    
    if len(players) > num_courts * 4:
        rest_players = players[num_courts*4:]
    
    st.subheader("Court Assignments")
    for court, assigned_players in court_assignments.items():
        st.write(f"{court}: {', '.join(assigned_players)}")
    
    if rest_players:
        st.write(f"Resting Players: {', '.join(rest_players)}")
        st.session_state.rest_queue = rest_players

# Function to allow player sign-out
def player_sign_out():
    st.subheader("Player Sign-Out")
    sign_out_player = st.selectbox("Select Player to Sign Out", st.session_state.present_players)
    if st.button("Sign Out Player"):
        st.session_state.present_players.remove(sign_out_player)
        st.session_state.signed_out_players.append(sign_out_player)
        st.success(f"Player {sign_out_player} signed out successfully!")

# Function to download a report of players
def download_report():
    st.subheader("Download Report")
    played_players = st.session_state.present_players + st.session_state.signed_out_players
    if st.button("Generate Report"):
        report_df = pd.DataFrame(played_players, columns=["Name"])
        report_csv = report_df.to_csv(index=False)
        st.download_button(label="Download Report", data=report_csv, file_name="club_day_report.csv", mime="text/csv")

# Streamlit UI
st.title("KTS Badminton Club Day Management")

# Upload member list
upload_members()

# Select present players
if st.session_state.members:
    select_present_players()

# Add visitor player
add_visitor_player()

# Input court details and generate assignments
if st.session_state.present_players or st.session_state.visitor_players:
    input_court_details()

# Player sign-out functionality
if st.session_state.present_players:
    player_sign_out()

# Download report
download_report()
