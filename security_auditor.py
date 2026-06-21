import os

import platform

import psutil

import time

from dotenv import load_dotenv

from google import genai



# ==========================================

# 1. CREDENTIALS (SECURE LOAD)

# ==========================================

# This loads the hidden variables from your .env file

load_dotenv()



# This fetches the specific key securely without exposing it in the code

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)



def get_live_system_health():

    """Pulls real-time hardware data directly from your machine."""

    # 1. CPU

    cpu_usage = psutil.cpu_percent(interval=1)

    

    # 2. Memory (RAM)

    memory = psutil.virtual_memory()

    total_ram_gb = round(memory.total / (1024**3), 2)

    used_ram_gb = round(memory.used / (1024**3), 2)

    

    # 3. Storage (OS-Agnostic)

    # Automatically switch between Windows (C:\) and Linux/VirtualBox (/)

    if platform.system() == "Windows":

        disk_path = 'C:\\'

    else:

        disk_path = '/'

        

    disk = psutil.disk_usage(disk_path)

    total_disk_gb = round(disk.total / (1024**3), 2)

    free_disk_gb = round(disk.free / (1024**3), 2)

    

    # Format the data into a readable report for the AI

    report = (

        f"Live System Health Report:\n"

        f"- OS Detected: {platform.system()}\n"

        f"- CPU Usage: {cpu_usage}%\n"

        f"- RAM Usage: {memory.percent}% ({used_ram_gb} GB used / {total_ram_gb} GB total)\n"

        f"- Storage ({disk_path}): {disk.percent}% Used ({free_disk_gb} GB free / {total_disk_gb} GB total)"

    )

    return report



def security_auditor(system_report):

    """The AI Auditor scans the live system data for bottlenecks."""

    response = client.models.generate_content(

        model="gemini-2.0-flash",  

        contents=f"Review this live system health report for any performance bottlenecks or critical resource limits. Provide a brief analysis:\n{system_report}"

    )

    return response.text



def developer_agent(audit_report):

    """The AI Developer generates Python code to address the Auditor's findings."""

    response = client.models.generate_content(

        model="gemini-2.0-flash",  

        contents=f"Based on this system audit, write a Python script that could help mitigate the identified issues (e.g., clearing temp files if storage is low, or logging top memory-heavy processes). Do not use markdown backticks in the response.\n{audit_report}"

    )

    return response.text



# ==========================================

# 4. EXECUTION BLOCK (THE IGNITION SWITCH)

# ==========================================

if __name__ == "__main__":

    print("======================================")

    print("🔍 SECURITY AUDITOR ONLINE")

    print("======================================\n")

    print("Fetching live hardware metrics...")

    

    try:

        # Step 1: Grab hardware data

        health_data = get_live_system_health()

        print(f"\n{health_data}\n")

        print("-" * 40)

        

        # Step 2: Audit the data

        print("\n🕵️‍♂️ AUDITOR: Analyzing system health for bottlenecks...")

        audit_analysis = security_auditor(health_data)

        print(f"\n{audit_analysis}\n")

        print("-" * 40)

        

        # Step 3: Draft mitigation code

        print("\n👨‍💻 DEVELOPER: Drafting emergency mitigation script...")

        fix_script = developer_agent(audit_analysis)

        print("\n--- Mitigation Script ---")

        print(fix_script)

        print("-------------------------")

        

    except Exception as e:

        print(f"\n❌ Error during execution: {e}")
