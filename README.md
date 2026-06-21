# Autonomous Self-Healing System Monitor

This project provides an automated IT Operations (AIOps) tool that bridges real-time system hardware metrics with AI-driven analysis. It monitors your computer's health and generates custom scripts to resolve performance bottlenecks.

## Core Features
* Live System Monitoring: Automatically retrieves real-time CPU, RAM, and Disk usage data using psutil.
* Intelligent Auditing: Uses Google Gemini to analyze hardware health reports and identify critical performance bottlenecks.
* Automated Mitigation: Acts as an autonomous developer to write custom Python scripts designed to address specific detected issues (e.g., memory spikes, low disk space).
* OS Agnostic: Dynamically detects the host operating system to monitor the correct storage volumes.



## Prerequisites
* Python 3.9+
* Google GenAI SDK
* psutil (for system monitoring)
* A valid GEMINI_API_KEY

## Setup
1. Install dependencies:
   pip install google-genai python-dotenv psutil

2. Configure Environment:
   Create a .env file in the root directory:
   GEMINI_API_KEY=your_actual_api_key_here

## Usage
Run the script to perform a full health check and mitigation draft:
python system_monitor.py

## How It Works
1. Gather: The script polls hardware metrics from your OS.
2. Audit: The data is sent to an AI Auditor to flag resource bottlenecks.
3. Draft: An AI Developer agent takes the audit report and generates a remediation script tailored to your specific system state.

## Security Disclaimer
This tool uses generative AI to produce mitigation scripts. Always review the generated code before executing it on your machine, especially if it involves system-level file or process management.
