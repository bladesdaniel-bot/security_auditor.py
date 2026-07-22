```
# Local AI Security Auditor Agent

## Overview
The Local AI Security Auditor Agent is a robust, offline cybersecurity monitoring script designed to analyze system health, network status, and email payloads for potential threats. By leveraging a local Large Language Model (LLM) via Ollama, this agent processes sensitive system and email data entirely on your machine, ensuring zero data leakage to cloud servers.

It features a **Persistent Memory System** that records past audits, allowing the AI to maintain context over time, track ongoing issues, and learn from previous security alerts.

## Key Features
* **Total Privacy (Offline AI):** Uses the local Ollama model (`supergemma4-26b-uncensored-gguf-v2:latest`) for analysis, keeping your sensitive network and email data 100% local.
* **Hardware Diagnostics:** Monitors real-time CPU, RAM, and Disk usage using `psutil`.
* **Network Auditing:** Integrates with a custom PowerShell network diagnostic script (`netcheck.ps1`) to check for blocked ports, suspicious traffic, or connectivity issues.
* **Email Threat Scanning:** Ingests raw email payloads via the command line to scan for phishing attempts, malicious links, and malware signatures.
* **Persistent Memory Bank:** Automatically logs every audit (including timestamp, task, outcome, and success state) into a JSON memory bank. The last 5 logs are injected into future prompts to provide the AI with historical context.
* **GUI Integration Ready:** Outputs its final assessment to a `status.json` file, making it easy to hook this script up to a visual dashboard or frontend application.

## Prerequisites
1. **Python 3.8+**
2. **Ollama:** Must be installed and running locally.
3. **Required Python Packages:** 
   pip install psutil python-dotenv ollama
4. **Local LLM Model:** Pull the required model via Ollama:
   ollama run hf.co/jiunsong/supergemma4-26b-uncensored-gguf-v2:latest
   *(Note: You can change the model in the `security_auditor` function if you prefer a different local model).*

## Configuration & Setup
Before running the script, you **must** update the hardcoded paths to match your local system environment.

1. **Memory Directory:** 
   Update `DESKTOP_PATH` (around line 17) to where you want the memory JSON saved.
   DESKTOP_PATH = r"C:\Your\Path\Here\AI_Agent_Memory"
   
2. **Network Diagnostics Script:** 
   Update `script_path` (around line 59) to point to your actual PowerShell network script.
   script_path = r"C:\Your\Path\Here\netcheck.ps1"
   
3. **Custom Instructions (Optional):**
   Create a file named `security_auditor_instructions.md` in the same directory as this script. You can use this file to give the AI specific company policies or custom rules for its audit. If the file is missing, the script defaults to standard health and malware scanning.

## How to Use

Run the script from your terminal or command prompt.

**Standard System & Network Audit:**
python security_auditor.py

**System Audit + Email Payload Scan:**
To have the agent scan a specific email or text file for phishing/malware, pass the file path as an argument:
python security_auditor.py "C:\Path\To\suspicious_email.txt"

## How the Pipeline Works
1. **Data Collection:** The script captures live CPU/RAM/Disk stats and executes your `netcheck.ps1` script to grab network status.
2. **Payload Processing:** If an email file is provided via the CLI, it reads the contents.
3. **Memory Injection:** It reads the last 5 entries from `security_auditor_memory_bank.json`.
4. **AI Analysis:** All this data is bundled into a prompt and sent to the local Ollama model.
5. **Output & State Update:** 
   * The AI's response is printed to the terminal.
   * If words like "CRITICAL", "MALWARE", or "PHISHING" are detected in the response, it flags the system as critical.
   * It writes the final state ("critical" or "healthy") to `status.json`.
   * It saves the new interaction back into the persistent Memory Bank.

```
