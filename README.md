# GoalGetter50
#### Video Demo:  <https://youtu.be/v3w6F8US6Mg>

#### Description: GoalGetter50 is a web application designed to help users manage their tasks and goals. The interactive web App offers typical yet effective ways to list and manage tasks and goals, which have become quite a hard thing to do in this mordern, wide-world. The simple, user-friendly interface allows user to create lists of their due task. The app also allows common manipulations of Task that help manage tasks innovatively.

## Installation

1. **Install the Requirements**: Use the command `pip install -r requirements.txt`
2. **Change Directory**: Use the command `cd project`
3. **Run Flask**: Use the command `flask run`

## Features
- **Simple Design**: Made with Simple and User Freindly Design.
- **Sign In**: Sign In to dynamically save your progresses and notes.
- **Log In**: Log In into GoalGetter50 to access list anytime!
- **Log Out**: Log Out anytime without fearing about data loss.
- **Generate Quote**: Generate Random Quotes to keep the user Motivated & Fresh.
- **Add Task**: Add Tasks which will appear on the list.
- **Complete Task**: Mark Tasks Complete when done.
- **Remove Task**: Remove Tasks when no longer required.
- **Archive Task**: Archieve Tasks to avoid losing it by accident.
- **Undo Task**: Undo Task from completed and archived.
- **Completed**: Check which Tasks are completed.
- **Archived** : View Archived Tasks.
- **Timer** : Use Timer to do tasks in time limit.
- **Start, Pause, Resume** : Manipulate Timer when it starts.
- **Add Sticky Notes**: Create notes with a title and content.
- **Delete Sticky Notes**: Remove notes with a simple click.
- **Dynamic UI**: Notes are dynamically added to the DOM.
- **Light and Dark Mode**: Toggle between light and dark themes using switch.
- **Statistics**: Show Summary Statistics about Tasks.
- **Responsive Design**: Optimized for various screen sizes.

## Design
- The website uses a green color theme to spread positivity and happiness.
- A navbar was used to make the website more professional. However, the primary reason
is to guide the users.
- The website also has a dark mode setting, which can be accessed by clicking the
button

## Usage
- Use add task to add simple and short tasks, and mark it complete afer doing it to keep record.
- The list can be used to note down *Homework* or *Assignments*.
- Time can be added to remind the due date.
- Notes section can be used to create simple yet visually effective sticky notes.
- Notes can be used as *Flash Cards* by using the Title as Question and Content as Answer.
- Timer can be used to set fixed Time Duration for Excercises or Studies.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python) for server-side logic
- **Database**: SQLite
- **Version Control**: Git

## Credit
- CS50.ai
- Microsoft Copilot (for bug fixes and designs)


## License
This project is licensed under CS50

### Summary of the License
- You can use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.
- There is no warranty, and the software is provided "as is."
- You must include the original license in any substantial portions of the software.

Copyright (c) 2024 Nafis Fuad

## About
- Hey there Everyone! This is Nafis Fuad, a nerdy guy who took CS50x. In this section, i'll be mostly talking about the files i used and what each files contain.
In my Flask application, I started by defining the `login_required` decorator to ensure users are authenticated before accessing other routes. The `register` function allows new users to create an account by entering a username and password, which was hashed for security. The `login` function handles user authentication by checking given information and starting a session for the user. When users want to log out, the `logout` function clears the session data. The `index` function serves as the homepage, displaying the active tasks. Through the `add_task` function, users can add tasks to their list. Task completion handled with the `complete_task` function, which toggles the completion status of a task. The `delete_task` function allows users to remove tasks from the list. In the `completed` function, I display tasks that have been marked as completed. The `undo_task` function lets users unarchive tasks, making them visible again. In the `archived` function, I retrieve and display tasks that users have archived. The `archive_task` function enables users to archive tasks they want to hide temporarily. For the timer feature, the `timer` function renders the timer page. Lastly, the `notes` function handles the creation and display of user notes, and I manage note-related actions with `add_note` and `delete_note` functions, while the `get_notes` function returns user notes in JSON format for potential AJAX use. Overall, I've built a user-friendly task and notes management system with authentication and database integration. For most of the functions, an HTML file was used for the page.

### Special Thanks and Grattitude to to CS50x Team for making available such amazing opportunity for the world to explore the Best Introduction to Computer Science Course.

