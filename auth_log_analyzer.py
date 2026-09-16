#!/usr/bin/env python3

log_file = '/var/log/auth.log'
ip_counts = {}

# Open the file to read it
with open(log_file, 'r') as file:
    for line in file:
       
        # 1. Look for the specific failure phrase
        if "Failed password" in line:
           
            # 2. Break the line into a list of individual words
            words = line.split()
           
            # 3. Find the word "from" and grab the next word (which is the IP)
            if "from" in words:
                ip = words[words.index("from") + 1]
               
                # 4. Add the IP to our tally, or update the count if it's already there
                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1

# 5. Print the final results
print("--- Failed SSH Logins ---")
for ip, count in ip_counts.items():
    print(f"Target IP: {ip} | Failed Attempts: {count}")
