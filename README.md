Here's a `README.md` for your KTS Badminton Club Day Management application:

---

# KTS Badminton Club Day Management

This Streamlit-based web application helps manage player rotations, court assignments, and player sign-outs for KTS Badminton club day events. The app allows the admin to upload player lists, manually select players present for the day, add visitors, assign courts, manage rest periods, and download reports of players who participated.

## Features

1. **Upload Member List**: Admin can upload a CSV file containing player names and grades.
2. **Select Players Present**: Allows the admin to select players who are present for the day's session.
3. **Visitor Management**: Admin can manually add visitor players, who are highlighted in a different color for identification.
4. **Court Assignment**: Automatically assigns players to courts, with 4 players per court.
5. **Rest and Queue Management**: Players not assigned to a court are placed in a rest queue and are prioritized for the next round. No player can be rested for two consecutive rounds.
6. **Player Sign-Out**: Allows players to sign out if they need to leave early, removing them from future game generations.
7. **Download Report**: Admin can download a list of all players who participated on each club day.
8. **Grading System**: Players can be grouped by grade (A, B, C, D), and the app can generate games by grouping A&B grades together and C&D grades together. If players are not equally distributed, the app can mix players for game generation.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/kts-badminton-management.git
   cd kts-badminton-management
   ```

2. **Install the Required Python Packages**
   Ensure that you have Python installed. Then, install the required packages:
   ```bash
   pip install streamlit pandas
   ```

3. **Run the Application**
   You can start the application using the following command:
   ```bash
   streamlit run kts_badminton.py
   ```

4. **Open the Application in Your Browser**
   Once the app is running, you can access it by opening the provided URL (usually `http://localhost:8501`) in your browser.

## Usage

1. **Upload the Member List**
   - Upload a CSV file containing player names and grades (A, B, C, D). You can use the sample `members.csv` provided in the repository.
   - Example CSV format:
     ```csv
     Name,Grade
     Alice,A
     Bob,B
     Charlie,C
     ```

2. **Select Players Present**
   - Select players who are present for today's club session. The list will be based on the uploaded member list.

3. **Add Visitor Players**
   - Add visitor players manually. Visitor players are highlighted with a different color to distinguish them from regular members.

4. **Input Court Details**
   - Specify the number of courts and the game duration (10, 12, 14, or 16 minutes).

5. **Generate Court Assignments**
   - The app will assign 4 players per court based on the input data. Unassigned players will be placed in the rest queue, ensuring they are prioritized for the next round.

6. **Manage Player Sign-Out**
   - Players can sign out if they need to leave early, ensuring they won’t be included in future game rounds.

7. **Download Club Day Report**
   - Download a CSV file listing all players who participated on the day.

## Future Enhancements

- **Advanced Scheduling Algorithms**: More sophisticated algorithms for scheduling games based on player history and performance.
- **Automated Notifications**: Notify players about their next game via email or SMS.
- **Detailed Statistics**: Track player participation statistics over time.
  
## License

This project is licensed under the Cyber Kiwi License 

---

This `README.md` provides an overview of the app, its features, and instructions on how to set it up and use it. Let me know if you'd like to make any changes!
