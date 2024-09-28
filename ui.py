import streamlit as st
import time
from config import load_settings

def run_ui(incident_crew, logger):
    st.title("IT Infrastructure Incident Management")

    settings = load_settings()

    # Display the system logs at the top with a scroll bar
    st.subheader("System Logs")
    with open(settings['system_log_file'], "r") as log_file:
        log_content = log_file.read()
    st.text_area("System Logs", log_content, height=200, max_chars=None)

    # Button to run incident analysis
    if st.button("Run Incident Analysis"):
        st.write("Running Incident Analysis...")

        # Run the incident management crew
        incident_crew.kickoff()
        logger.info("Incident management tasks completed.")

        # Display run.log content dynamically
        st.subheader("Run Log Output")

        # Dynamically update the run.log file content
        run_log_content = ""
        log_file_path = "run.log"
        while True:
            with open(log_file_path, "r") as run_log_file:
                new_log_content = run_log_file.read()
            if new_log_content != run_log_content:
                st.text_area("Run Log", new_log_content, height=300)
                run_log_content = new_log_content

            # Sleep for a short time to avoid excessive refreshes
            time.sleep(1)