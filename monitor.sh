#!/bin/bash

# Website monitoring script
# This script checks if the website is responding and restarts services if needed

LOG_FILE="/home/ec2-user/jackspoetic/monitor.log"
WEBSITE_URL="http://localhost"
FLASK_PROCESS="python app.py"

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Check if website is responding
check_website() {
    if curl -s -f "$WEBSITE_URL" > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Check if Flask process is running
check_flask() {
    if pgrep -f "$FLASK_PROCESS" > /dev/null; then
        return 0
    else
        return 1
    fi
}

# Restart Flask application
restart_flask() {
    log_message "Restarting Flask application..."
    cd /home/ec2-user/jackspoetic
    source venv/bin/activate
    pkill -f "$FLASK_PROCESS" 2>/dev/null
    sleep 2
    nohup python app.py > flask.log 2>&1 &
    sleep 5
}

# Main monitoring logic
log_message "Starting website monitoring check..."

# Check if Flask is running
if ! check_flask; then
    log_message "Flask process not found, restarting..."
    restart_flask
fi

# Check if website is responding
if ! check_website; then
    log_message "Website not responding, restarting Flask..."
    restart_flask
    
    # Check again after restart
    sleep 10
    if ! check_website; then
        log_message "Website still not responding after restart"
    else
        log_message "Website restored after restart"
    fi
else
    log_message "Website is responding normally"
fi 