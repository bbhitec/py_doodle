import curses
import threading
import time
import sys

# Simulation function
def run_simulation(sim_window, input_window, stop_event):
    counter = 0
    max_y, _ = sim_window.getmaxyx()  # Get the window dimensions
    current_line = 0  # Keep track of the current line in the simulation window

    # Allow scrolling in the window
    sim_window.scrollok(True)
    
    while not stop_event.is_set():
        counter += 1
        # Check if the current line exceeds the window height
        if current_line >= max_y - 1:
            sim_window.scroll()  # Scroll the window when full
            current_line = max_y - 2  # Keep the new line at the bottom
        else:
            current_line += 1
        
        # Print the output on the current line
        sim_window.addstr(current_line, 1, f"Simulation Output: {counter}")
        sim_window.refresh()

        # Keep the cursor in the input window
        input_window.move(2, 1)
        input_window.refresh()
        
        time.sleep(1)

# User input handler
def handle_user_input(input_window, stop_event):
    curses.echo()  # Enable real-time input display
    input_window.addstr(1, 1, "User Input: ")
    input_window.refresh()

    while not stop_event.is_set():
        input_window.move(2, 1)  # Position the cursor for input
        user_input = input_window.getstr(20).decode("utf-8")  # Get the input from the user
        
        # If the user inputs 'q', trigger an exit
        if user_input.strip().lower() == 'q':
            stop_event.set()  # Signal to stop threads
            break

        # Clear input line and display the input
        input_window.clear()
        input_window.addstr(1, 1, "User Input: " + user_input)
        input_window.refresh()

# Main function to initialize curses and run threads
def main(stdscr):
    # Clear screen
    curses.curs_set(1)  # Show cursor
    
    # Create a stop event to signal threads to stop gracefully
    stop_event = threading.Event()
    
    # Get the full height and width of the terminal
    height, width = stdscr.getmaxyx()

    # Ensure that the terminal has a minimum size to handle the windows
    min_height = 10  # Arbitrary minimum height
    min_width = 30   # Arbitrary minimum width

    if height < min_height or width < min_width:
        stdscr.clear()
        stdscr.addstr(0, 0, "Terminal too small. Please resize to at least 10x30.")
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting
        return

    # Calculate the division: 2/3 for sim_window, 1/3 for input_window
    sim_height = (2 * height) // 3
    input_height = height // 3
    
    # Create windows for simulation and user input
    sim_window = curses.newwin(sim_height, width, 0, 0)
    input_window = curses.newwin(input_height, width, sim_height + 1, 0)  # Input window starts after the horizontal line
    
    # Draw a horizontal line between the simulation and input sections
    stdscr.hline(sim_height, 0, '-', width)  # Horizontal line at the bottom of sim_window
    stdscr.refresh()
    
    # Create threads
    sim_thread = threading.Thread(target=run_simulation, args=(sim_window, input_window, stop_event))
    input_thread = threading.Thread(target=handle_user_input, args=(input_window, stop_event))
    
    # Start threads
    sim_thread.daemon = True
    input_thread.daemon = True
    sim_thread.start()
    input_thread.start()
    
    try:
        # Keep the main thread alive to allow other threads to run
        while not stop_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle Ctrl-C gracefully
        stop_event.set()  # Signal threads to stop
    finally:
        # Wait for the simulation and input threads to finish
        sim_thread.join()
        input_thread.join()
        print("\nExiting gracefully...")

# Initialize the curses application
if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        # In case of interruption during curses setup
        print("\nCurses interrupted. Exiting gracefully...")
        sys.exit(0)
