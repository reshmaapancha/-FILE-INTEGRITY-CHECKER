# -FILE-INTEGRITY-CHECKER

Company : CODTECH IT SOLUTION 

NAME : RESHMA PANCHAL 

Intern ID : CITS0D652

Domain : Cyber Security & Ethical Hacking

Duration : 4 WEEKS 

Mentror : NEELA SANTOSH 

DESCRIPTION : File Integrity Checker
Overview
The File Integrity Checker is a Python-based security tool developed to monitor and verify the integrity of files by calculating and comparing their cryptographic hash values. This tool plays a crucial role in detecting unauthorized or accidental modifications in critical system or application files. By regularly checking and validating file hashes, users can be alerted if any file has been altered, tampered with, or corrupted.

This project is especially useful for students, cybersecurity learners, and system administrators who want a simple and effective way to track changes to sensitive files. It provides a hands-on understanding of how cryptographic hashing can be used in real-world security scenarios, such as intrusion detection, malware identification, or system file monitoring.

What is File Integrity Checking?
File integrity checking is the process of ensuring that a file has not been changed from its original state. It typically involves generating a hash (a fixed-length string generated from data using a mathematical algorithm) for each file, saving that hash, and later recalculating the hash to detect any differences.

If even a single bit in a file is changed, the hash will be entirely different. This makes hashing a reliable technique for detecting any unauthorized or unintended modifications to a file.

Features
Hash Generation: Generates secure SHA-256 hash values for selected files.

Comparison Functionality: Compares the current hash with a previously saved hash to detect changes.

User-Friendly: Simple interface and prompts for beginners to use easily.

Lightweight: Runs from any Python environment like IDLE or terminal without heavy system requirements.

Cross-Platform: Works on Windows, Linux, and macOS.

Technologies Used
Python 3.x: Core language used for scripting.

hashlib: Used to generate secure SHA-256 hashes.

os: Interacts with the operating system to access files.

time: Used to record or log file modification times (optional).

How It Works
Hash Calculation: The tool reads the contents of the file and calculates its hash using the SHA-256 algorithm.

Save Hash: The original hash can be saved in a separate file for future comparison.

Check Integrity: When the tool is run again, it recalculates the file's current hash and compares it with the previously saved one.

Report Changes: If the hash values do not match, it means the file has been changed. If they match, the file is intact.

How to Use
Run the script in Python (IDLE or terminal).

Choose the file whose integrity you want to monitor.

The tool will generate a hash and save it to a file (e.g., file_hash.txt).

In the future, run the script again and it will compare the current file’s hash with the saved one.

The tool will inform whether the file has been modified or remains unchanged.
