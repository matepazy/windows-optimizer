import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import time
import requests

version = str("v1.0")

def download_script(url, save_path):
    try:
        # Send an HTTP GET request to the URL to fetch the script content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful

        # Save the content of the script to a file
        with open(save_path, "wb") as file:
            file.write(response.content)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching script from URL:\n{e}\nThis could either be because you don't have internet access, or the script has been removed, or the site is unavaliable!")

def execute_batch_file(batch_file_path):
    try:
        # Use subprocess.run() to execute the batch file
        subprocess.run(batch_file_path, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing batch file '{batch_file_path}': {e}")

def run_hybrid_script(script_content):
    try:
        # Create a temporary batch file
        batch_file_path = os.path.join(os.getcwd(), "temp_script.bat")
        with open(batch_file_path, "w") as batch_file:
            batch_file.write(script_content)

        # Execute the temporary batch file using subprocess.run()
        subprocess.run(batch_file_path, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        # If there's an error, print the error message
        messagebox.showerror("Error", f"Error executing hybrid script:\n{e}")

    # Remove the temporary batch file
    os.remove(batch_file_path)

remove_bloatware_script = "./scripts/debloat.ps1"
remove_msedge_script = "./scripts/rmmsedge.bat"
remove_cortana_script = "./scripts/rmcortana.ps1"
disable_telemetry_script = "./scripts/telemetry.ps1"
disable_winupdate_script = "./scripts/diswinupdate.ps1"
enable_winupdate_script = "./scripts/enwinupdate.ps1"
classic_context_script = "./scripts/contextmenu.ps1"
fileextension_script = "./scripts/fileextension.ps1"
dis_stickeykeys_script = "./scripts/stickykeys.ps1"
remove_bloatware_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/debloat.ps1"
remove_msedge_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/rmmsedge.bat"
remove_cortana_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/rmcortana.ps1"
disable_telemetry_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/telemetry.ps1"
disable_winupdate_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/diswinupdate.ps1"
enable_winupdate_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/enwinupdate.ps1"
classic_context_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/contextmenu.ps1"
fileextension_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/fileextension.ps1"
dis_stickeykeys_script_url = "https://wp.matepaz.repl.co/optimizer/scripts/stickykeys.ps1"

def removebloatware():
    os.mkdir("./scripts")
    response = messagebox.askyesno("Confirmation", "This will delete the following programs:\nMicrosoft.BingNews\nMicrosoft.BingWeather\nMicrosoft.GetHelp\nMicrosoft.Getstarted\nMicrosoft.MicrosoftOfficeHub\nMicrosoft.PowerAutomateDesktop\nMicrosoft.SecHealthUI\nMicrosoft.People\nMicrosoft.Todos\nMicrosoft.WindowsAlarms\nMicrosoft.WindowsCamera\nmicrosoft.windowscommunicationsapps\nMicrosoft.WindowsFeedbackHub\nMicrosoft.WindowsMaps\nMicrosoft.WindowsSoundRecorder\nMicrosoft.YourPhone\nMicrosoft.ZuneMusic\nMicrosoft.ZuneVideo\nMicrosoftTeams\n")
    if response == True:
        download_script(remove_bloatware_script_url, remove_bloatware_script)
        try:
            # Execute the PowerShell script using subprocess.run()
            result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', remove_bloatware_script],
                                    capture_output=True, text=True, check=True)

            # If the script runs successfully, show a system dialog
            messagebox.showinfo("Success!", "Debloating was successful!\nNow you are safe from Microsoft's Bloatware")
            os.remove("./scripts/debloat.ps1")
            os.removedirs("./scripts")

        except subprocess.CalledProcessError as e:
            # If the script encounters an error, show an error message dialog
            messagebox.showerror("Error", f"Error executing PowerShell script:\n{e.stderr}")
            os.remove("./scripts/debloat.ps1")
            os.removedirs("./scripts")

    else:
        pass

def removeedge():
    os.mkdir("./scripts")
    response = messagebox.askyesno("Confirmation", "Are you sure about this?")
    download_script(remove_msedge_script_url, remove_msedge_script)
    if response == True:
        # Read the content of the hybrid script from the file
        with open(remove_msedge_script, "r") as script_file:
            hybrid_script_content = script_file.read()
        # Execute the hybrid script using the run_hybrid_script() function
        run_hybrid_script(hybrid_script_content)
        time.sleep(5)
        messagebox.showinfo("Success!", "Microsoft Edge script has been executed successfully")
        time.sleep(10)
        os.remove("./scripts/rmmsedge.bat")
        os.removedirs("./scripts")
    else:
        os.remove("./scripts/rmmsedge.bat")
        os.removedirs("./scripts")

def removecortana():
    os.mkdir("./scripts")
    response = messagebox.askyesno("Confirmation", "Do you want to remove Cortana?")
    download_script(remove_cortana_script_url, remove_cortana_script)
    if response == True:
        try:
            # Execute the PowerShell script using subprocess.run()
            result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', remove_cortana_script],
                                    capture_output=True, text=True, check=True)

            # If the script runs successfully, show a system dialog
            messagebox.showinfo("Success!", "Successfully removed Cortana!")
            os.remove("./scripts/rmcortana.ps1")
            os.removedirs("./scripts")

        except subprocess.CalledProcessError as e:
            # If the script encounters an error, show an error message dialog
            messagebox.showerror("Error", f"Error executing PowerShell script:\n{e.stderr}")
            os.remove("./scripts/rmcortana.ps1")
            os.removedirs("./scripts")

    else:
        os.remove("./scripts/rmcortana.ps1")
        os.removedirs("./scripts")

def distelemetry():
    os.mkdir("./scripts")
    response = messagebox.askyesno("Confirmation", "Do you want to disable Telemetry?")
    download_script(disable_telemetry_script_url, disable_telemetry_script)
    if response == True:
        try:
            # Execute the PowerShell script using subprocess.run()
            result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', disable_telemetry_script],
                                    capture_output=True, text=True, check=True)

            # If the script runs successfully, show a system dialog
            messagebox.showinfo("Success!", "Successfully disabled Telemetry!!")
            os.remove("./scripts/telemetry.ps1")
            os.removedirs("./scripts")

        except subprocess.CalledProcessError as e:
            # If the script encounters an error, show an error message dialog
            messagebox.showerror("Error", f"Error executing PowerShell script:\n{e.stderr}")
            os.remove("./scripts/telemetry.ps1")
            os.removedirs("./scripts")

    else:
        os.remove("./scripts/telemetry.ps1")
        os.removedirs("./scripts")

def contextmenu():
    os.mkdir("./scripts")
    download_script(classic_context_script_url, classic_context_script)
    try:
            # Execute the PowerShell script using subprocess.run()
        result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', classic_context_script],
                                    capture_output=True, text=True, check=True)

            # If the script runs successfully, show a system dialog
        messagebox.showinfo("Success!", "Successfully restored old Context Menu!")
        os.remove("./scripts/contextmenu.ps1")
        os.removedirs("./scripts")

    except subprocess.CalledProcessError as e:
            # If the script encounters an error, show an error message dialog
            messagebox.showerror("Error", f"Error executing PowerShell script:\n{e.stderr}")
            os.remove("./scripts/contextmenu.ps1")
            os.removedirs("./scripts")

def fileextension():
    os.mkdir("./scripts")
    download_script(fileextension_script_url, fileextension_script)
    try:
            # Execute the PowerShell script using subprocess.run()
        result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', fileextension_script],
                                    capture_output=True, text=True, check=True)

            # If the script runs successfully, show a system dialog
        messagebox.showinfo("Success!", "Successfully enbaled show file extensions!")
        os.remove("./scripts/fileextension.ps1")
        os.removedirs("./scripts")

    except subprocess.CalledProcessError as e:
            # If the script encounters an error, show an error message dialog
            messagebox.showerror("Error", f"Error executing PowerShell script:\n{e.stderr}")
            os.remove("./scripts/fileextension.ps1")
            os.removedirs("./scripts")

def disstickeykeys():
    os.mkdir("./scripts")
    download_script(dis_stickeykeys_script_url, dis_stickeykeys_script)
    try:
            # Execute the PowerShell script using subprocess.run()
        result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File',dis_stickeykeys_script],
                                    capture_output=True, text=True, check=True)

            # If the script runs successfully, show a system dialog
        messagebox.showinfo("Success!", "Successfully disabled Sticky Hotkeys!")
        os.remove("./scripts/stickykeys.ps1")
        os.removedirs("./scripts")

    except subprocess.CalledProcessError as e:
            # If the script encounters an error, show an error message dialog
            messagebox.showerror("Error", f"Error executing PowerShell script:\n{e.stderr}")
            os.remove("./scripts/stickykeys.ps1")
            os.removedirs("./scripts")

def temp():
    execute_batch_file("""cd /d "%TEMP%"
del /f /q *.* > nul 2>&1""")

def recycle():
    execute_batch_file("rd /s /q C:\$Recycle.Bin")

def prefetch():
    response = messagebox.askyesno("Confirmation", "If you delete the prefetch files, the next boot might be longer.")
    if response == "Yes":
        execute_batch_file("""del /F /Q "%SystemRoot%\Prefetch\*.pf""")
    else:
        pass

window = tk.Tk()
window.title("Windows Optimizer Tool")
window.geometry("1000x600")
icon_path = os.path.abspath("icon.png")
window.iconphoto(True, tk.PhotoImage(file=icon_path))
window.configure(bg="grey")

title_label = tk.Label(window, text="Windows Optimizer Tool", font=("Helvetica", 18, "bold", "underline"), bg="grey", fg="white")
title_label.pack(pady=20)

button_frame = tk.Frame(window, bg="grey")
button_frame.pack(pady=10)

# Create the buttons and use the grid geometry manager
junk_label = tk.Label(button_frame, text="Microsoft JUNK Removal Tools", font=("Helvetica", 12, "bold"), bg="grey", fg="white")
junk_label.grid(row=0, column=0, pady=5, columnspan=4)

remove_bloatware = tk.Button(button_frame, text="Remove Bloatware", bg="white", fg="black", width=20, height=2, command=removebloatware)
remove_bloatware.grid(row=1, column=0, padx=5, pady=5)

remove_msedge = tk.Button(button_frame, text="Delete Microsoft Edge", bg="white", fg="black", width=20, height=2, command=removeedge)
remove_msedge.grid(row=1, column=1, padx=5, pady=5)

remove_cortana = tk.Button(button_frame, text="Remove Cortana", bg="white", fg="black", width=20, height=2, command=removecortana)
remove_cortana.grid(row=1, column=2, padx=5, pady=5)

remove_telemetry = tk.Button(button_frame, text="Disable Telemetry", bg="white", fg="black", width=20, height=2, command=distelemetry)
remove_telemetry.grid(row=1, column=3, padx=5, pady=5)

fix_label = tk.Label(button_frame, text="Fix Windows 11", font=("Helvetica", 12, "bold"), bg="grey", fg="white")
fix_label.grid(row=2, column=0, pady=10, columnspan=4)

classic_context = tk.Button(button_frame, text="Restore Classic Context Menu", bg="white", fg="black", width=25, height=2, command=contextmenu)
classic_context.grid(row=3, column=0, padx=5, pady=5)

fileextension_btn = tk.Button(button_frame, text="Show File Extensions", bg="white", fg="black", width=20, height=2, command=fileextension)
fileextension_btn.grid(row=3, column=1, padx=5, pady=5)

sticky_keys = tk.Button(button_frame, text="Disable Sticky Keys", bg="white", fg="black", width=20, height=2, command=disstickeykeys)
sticky_keys.grid(row=3, column=2, padx=5, pady=5)

storage_label = tk.Label(button_frame, text="Save up some storage!", font=("Helvetica", 12, "bold"), bg="grey", fg="white")
storage_label.grid(row=4, column=0, pady=10, columnspan=4)

temp = tk.Button(button_frame, text="Delete Temporary Files", bg="white", fg="black", width=20, height=2, command=temp)
temp.grid(row=5, column=0, padx=5, pady=5)

recyclebin = tk.Button(button_frame, text="Delete The Recycling Bin", bg="white", fg="black", width=20, height=2, command=recycle)
recyclebin.grid(row=5, column=1, padx=5, pady=5)

prefetch = tk.Button(button_frame, text="Delete The Prefetch Files", bg="white", fg="black", width=20, height=2, command=prefetch)
prefetch.grid(row=5, column=2, padx=5, pady=5)

def verify_version(url, window):
    try:
        # Send an HTTP GET request to download the text file
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful

        # Read the content of the downloaded file
        content = response.text.strip().lower()

        # Perform actions based on the content of the file
        if content == "yes":
            version_text = tk.Label(window, text=version, bg="green", fg="white", font=("Helvetica", 12))
            version_text.pack(side=tk.BOTTOM, anchor=tk.SW)
        elif content == "partially":
            version_text = tk.Label(window, text=version, bg="yellow", fg="grey", font=("Helvetica", 12))
            version_text.pack(side=tk.BOTTOM, anchor=tk.SW)
        elif content == "no":
            version_text = tk.Label(window, text=version, bg="red", fg="white", font=("Helvetica", 12))
            version_text.pack(side=tk.BOTTOM, anchor=tk.SW)
        else:
            messagebox.showwarning("Contact the developer", "The version file, didn't contain anything the program needed to verify.\nPlease raise an issue on Github.")
            version_text = tk.Label(window, text=f"Version file had inappropriate content! Please raise an issue on Github! ({version})", bg="red", fg="white", font=("Helvetica", 12))
            version_text.pack(side=tk.BOTTOM, anchor=tk.SW)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An unexpected error occurred while trying to retrieve version.\nCurrent version {version}")
        version_text = tk.Label(window, text=f"{version} (not verified)", bg="grey", fg="white", font=("Helvetica", 12))
        version_text.pack(side=tk.BOTTOM, anchor=tk.SW)

url = f"https://wp.matepaz.repl.co/optimizer/{version}.txt"
verify_version(url, window)

window.mainloop()
