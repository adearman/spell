# Made with ❤ by @adearman
# Join tele channel for update t.me/ghalibie
import requests
import time
from colorama import Fore, Style, init
import re
import json
import urllib.parse
import argparse
def extract_names(encoded_text):
    # Decode the URL-encoded string
    decoded_text = urllib.parse.unquote(encoded_text)

    # Define regex patterns to extract first name and last name
    first_name_pattern = r'"first_name":"(.*?)"'
    last_name_pattern = r'"last_name":"(.*?)"'

    # Search for the patterns in the decoded text
    first_name_match = re.search(first_name_pattern, decoded_text)
    last_name_match = re.search(last_name_pattern, decoded_text)

    # Extract the matched values
    first_name = first_name_match.group(1) if first_name_match else None
    last_name = last_name_match.group(1) if last_name_match else None

    return first_name, last_name
# Initialize Colorama
init(autoreset=True)

# Function to get authorizations from file
def get_authorizations_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to create headers
def create_headers(authorization):
    return {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'tma ' + authorization,
        'content-type': 'application/json',
        'origin': 'https://wallet.spell.club',
        'referer': 'https://wallet.spell.club/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

# Function to handle GET requests
def make_get_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.HTTPError as errh:
        if errh.response.status_code == 400:
           return response.json()   
        else:
            print(Fore.RED + f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(Fore.RED + f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(Fore.RED + f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(Fore.RED + f"Oops: Something Else {err}")
    except ValueError as errj:
        print(Fore.RED + f"JSON Error: {errj}")
    return None

def make_get_request_login(url, headers, first_name, last_name):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.HTTPError as errh:
        if errh.response.status_code == 400:
           return response.json()   
        else:
            print(Fore.RED + f"[ {first_name} {last_name} ] HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(Fore.RED + f"[ {first_name} {last_name} ] Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(Fore.RED + f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(Fore.RED + f"Oops: Something Else {err}")
    except ValueError as errj:
        print(Fore.RED + f"JSON Error: {errj}")
    return None

# Function to handle POST requests
def make_post_request(url, headers, data=None):
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        if errh.response.status_code == 400:
            return response.json()  
        else:
            print(Fore.RED + f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(Fore.RED + f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(Fore.RED + f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(Fore.RED + f"Oops: Something Else {err}")
    except ValueError as errj:
        print(Fore.RED + f"JSON Error: {errj}")
    return None

# Function to get balance
def get_balance(authorization, first_name, last_name):
    url = 'https://wallet-api.spell.club/user'
    headers = create_headers(authorization)
    response = make_get_request_login(url, headers, first_name, last_name)
    # print(response)
    if response:
        return response
    return None

# Function to attempt claim

def attempt_claim(authorization):
    url = 'https://wallet-api.spell.club/claim?batch_mode=true'
    headers = create_headers(authorization)
    return make_post_request(url, headers)

def upgrade_booster(authorization):
    url = 'https://wallet-api.spell.club/upgrade?batch_mode=true'
    headers = create_headers(authorization)
    payload = {"upgrade_type": "booster"}
    data = json.dumps(payload)
    return make_post_request(url, headers, data=data)
# Function to get tasks

def join_clan(authorization):
    url = 'https://wallet-api.spell.club/clan/join?batch_mode=true'
    headers = create_headers(authorization)
    payload = {"clan_address": "sei1x5qp3awdh8fxl0m8l96gd4cm374j476xz4e9xj3ue6nwmp0mdy6qvc52u7"}
    data = json.dumps(payload)
    return make_post_request(url, headers, data=data)

def get_tasks(authorization):
    url = 'https://wallet-api.spell.club/get_tasks'
    headers = create_headers(authorization)
    return make_post_request(url, headers)

def claim_quest(authorization, id_quest):
    url = f'https://wallet-api.spell.club/quest/step/{id_quest}/complete'
    headers = create_headers(authorization)
    response = requests.post(url, headers=headers)
    # print(response)
    try:
        response.raise_for_status()
        # Periksa apakah respons memiliki konten sebelum mengurai sebagai JSON
        if response.text:
            return response.json()
        else:
            # Mengembalikan objek JSON kustom jika respons kosong tetapi statusnya 200 OK
            return None
    except requests.exceptions.HTTPError as err:
        if response.status_code == 400:
            error_info = response.json()  # Mendapatkan informasi kesalahan dari JSON
            return error_info
        else:
            print(Fore.RED + f"Kesalahan HTTP: {err}")
        return None

def get_clan_info(clan_address, authorization):
    url = f'https://wallet-api.spell.club/clan/{clan_address}'
    headers = create_headers(authorization)
    response = make_get_request(url, headers)
    if response:
        return response
    return None

def get_quest(authorization):
    url = f'https://wallet-api.spell.club/quest/1'
    headers = create_headers(authorization)
    response = make_get_request(url, headers)
    if response:
        return response
    return None

def parse_arguments():
    parser = argparse.ArgumentParser(description='Blum BOT')
    parser.add_argument('--upgrade', type=str, choices=['y', 'n'], help='Upgrade Booster (y/n)')
    args = parser.parse_args()

    if args.upgrade is None:
        # Jika parameter --upgrade tidak diberikan, minta input dari pengguna
        upgrade_input = input("Apakah Anda ingin upgrade booster? (y/n, default n): ").strip().lower()
        # Jika pengguna hanya menekan enter, gunakan 'n' sebagai default
        args.upgrade = upgrade_input if upgrade_input in ['y', 'n'] else 'n'

    return args

args = parse_arguments()
cek_upgrade_enable = args.upgrade
# Main logic
def main():
    print_welcome_message()
    authorizations = get_authorizations_from_file('tma.txt')
   

    while True:  # Loop selamanya
        for idx, auth in enumerate(authorizations, start=1):
            first_name, last_name = extract_names(auth)
            balance = get_balance(auth, first_name, last_name)
            # print(balance)
            if balance is not None:
                address = balance.get('address')
                clan = balance.get('clan_address')
                balance = balance.get('balance') / 1000000
    
                
                print(Fore.CYAN + Style.BRIGHT + f"\n===== [ Akun {idx} | {first_name} {last_name} ] =====")
                print(Fore.YELLOW + Style.BRIGHT + f"[ Address ] : {address}")
                print(Fore.YELLOW + Style.BRIGHT + f"[ Balance ] : {balance:.2f}")
                print(Fore.YELLOW + Style.BRIGHT + f"[ Welcome Quest ] : Checking ...", end="", flush=True)


                quest_response = get_quest(auth)
                if quest_response:
                    time.sleep(2)
                    quest_status = quest_response.get('is_claimed')
                    if quest_status == False:
                        print(Fore.GREEN + Style.BRIGHT + f"\r[ Welcome Quest ] : Not Claimed       ", flush=True)
                        print(Fore.YELLOW + Style.BRIGHT + f"\r[ Welcome Quest ] : Trying to claim...", end="", flush=True)  
                        q1 = claim_quest(auth, 1)
                        time.sleep(5)
                        if q1 == None:
                            print(Fore.GREEN + Style.BRIGHT + f"\r[ Welcome Quest ] : Follow the telegram channel completed ", flush=True)
                        else:
                            if q1.get('message') == 'already_exist':
                                print(Fore.GREEN + Style.BRIGHT + f"\r[ Welcome Quest ] : Follow the telegram channel already completed ", flush=True)
                        q2 = claim_quest(auth,2)
                        time.sleep(5)
                        if q2 == None:
                            print(Fore.GREEN + Style.BRIGHT + f"[ Welcome Quest ] : Follow @spell_club on X completed ", flush=True)
                        else:
                            if q2.get('message') == 'already_exist':
                                print(Fore.GREEN + Style.BRIGHT + f"[ Welcome Quest ] : Follow @spell_club on X already completed ", flush=True)
                        q3 = claim_quest(auth,5)
                        time.sleep(5)
                        if q3 == None:
                            print(Fore.GREEN + Style.BRIGHT + f"[ Welcome Quest ] : Like @spell_club on X completed ", flush=True)
                        else:
                            if q3.get('message') == 'already_exist':
                                print(Fore.GREEN + Style.BRIGHT + f"[ Welcome Quest ] : Like @spell_club on X already completed ", flush=True)
                        q4 = claim_quest(auth,6)
                        time.sleep(5)
                        if q4 == None:
                            print(Fore.GREEN + Style.BRIGHT + f"[ Welcome Quest ] : Retweet @spell_club on X completed ", flush=True)
                        else:
                            if q4.get('message') == 'already_exist':
                                print(Fore.GREEN + Style.BRIGHT + f"[ Welcome Quest ] : Retweet @spell_club on X already completed ", flush=True)
                        tasks_response = get_tasks(auth)
                        if tasks_response:
                            print(Fore.CYAN + Style.BRIGHT + f"[ Welcome Quest ] : Claimed all task", flush=True)
                    elif quest_status == True:
                        print(Fore.GREEN + Style.BRIGHT + f"\r[ Welcome Quest ] : Claimed         ", flush=True)
                    
                    

                print(Fore.YELLOW + Style.BRIGHT + f"\r[ Clan ] : Checking clan...", end="", flush=True)
                if clan:
                    clan_info = get_clan_info(clan, auth)
                    if clan_info:
                        print(Fore.CYAN + Style.BRIGHT + f"\r[ Clan ] : {clan_info.get('name')} | Member : {clan_info.get('member_count')}", flush=True)
                    else:
                        print(Fore.GREEN + Style.BRIGHT + f"\r[ Clan ] : Error {clan_info}          ", flush=True)
                else:
                    print(Fore.GREEN + Style.BRIGHT + f"\r[ Clan ] : Dont Have Clan                         ", flush=True)
             
                if not clan:
                    print(Fore.YELLOW + Style.BRIGHT + f"\r[ Clan ] : No Clan, Try to join SGB-ID...", end="", flush=True)
                    join_attempts = 0
                    while join_attempts < 3:
                        join_response = join_clan(auth)
                        if join_response and join_response.get('id'):
                            print(Fore.GREEN + Style.BRIGHT + f"\r[ Clan ] : Success to apply SGB-ID! ID: {join_response.get('id')}", flush=True)
                            print(Fore.GREEN + Style.BRIGHT + f"\r[ Clan ] : Checking status join...", flush=True)
                            
                            tasks_response = get_tasks(auth)
                            if tasks_response:
                                for task in tasks_response:
                                    if task.get('type') == 'joinClan' and task.get('status') == 'pending':
                                        print(Fore.BLUE + Style.BRIGHT + f"\r[ Clan ] : Clan Join Pending. Try to check again",  flush=True)
                                        time.sleep(10)
                                        tasks_response = get_tasks(auth)
                                        if tasks_response:
                                            for task in tasks_response:
                                                if task.get('joinClan') == 'success':
                                                    print(Fore.GREEN + Style.BRIGHT + f"\r[ Clan ] : Joined!", flush=True)
                                                    break
                                                elif tasks_response == None:
                                                    print(Fore.RED + Style.BRIGHT + f"\r[ Clan ] : Joined", flush=True)
                                                else:
                                                    if task.get('joinClan') == 'pending':
                                                        print(Fore.BLUE + Style.BRIGHT + f"\r[ Clan ] : Clan Join Pending. Try to check again",  flush=True)
                                                        time.sleep(10)
                                                    # else:
                         
                                                    #     print(Fore.RED + Style.BRIGHT + f"\r[ Clan ] : Clan Join Status {tasks_response}", flush=True)
                       
                        elif join_response and join_response.get('message') == 'NotAllowed': 
                            print(Fore.RED + Style.BRIGHT + f"\r[ Clan ] : Already Apply SGB-ID                         ", flush=True)
                            break  
                        elif join_response and join_response.get('message') == 'user_not_exist': 
                            print(Fore.RED + Style.BRIGHT + f"\r[ Clan ] : AKUN BELUM AKTIF                     ", flush=True)
                            break  
                        join_attempts += 1
                        print(Fore.RED + Style.BRIGHT + f"\r[ Clan ] : Failed to join, Retrying... ({join_attempts}) {join_response}", flush=True)
                    if join_attempts == 3:
                        print(Fore.RED + Style.BRIGHT + f"\r[ Clan ] : Failed to join after 3 attempts.", flush=True)
                    

                
                        
                        
                        
                print(Fore.YELLOW + Style.BRIGHT + f"\r[ Mana Production ] : Checking...", end="", flush=True)
                while True:  # Loop untuk mencoba klaim
                    claim_response = attempt_claim(auth)
                    if claim_response:
                        if claim_response.get("message") == "NothingToClaim":
                            print(Fore.GREEN + Style.BRIGHT + f"\r[ Mana Production ] : Already Claimed", flush=True)
                            break  # Keluar dari loop klaim jika tidak ada yang bisa diklaim
                        else:
                            print(Fore.GREEN + Style.BRIGHT + f"\r[ Mana Production ] : Ready to claim: {claim_response}", flush=True)
                            time.sleep(2)
                            print(Fore.BLUE + Style.BRIGHT + f"\r[ Mana Production ] : Claiming mana..", end="", flush=True)
                            tasks_response = get_tasks(auth)
                            break
                            # print(tasks_response)
                            # if tasks_response:
                            #     for task in tasks_response:
                            #         if task.get('type') == 'claim' and task.get('status') == 'pending':
                            #             print(Fore.BLUE + Style.BRIGHT + f"\r[ Mana Production ] : Pending, Claiming again..",  flush=True)
                            #             break
                if cek_upgrade_enable == 'y':
                    print(Fore.YELLOW + Style.BRIGHT + f"\r[ Upgrade Booster ] : Checking...", end="", flush=True)
                    upgrade_response = upgrade_booster(auth)
                    if upgrade_response:
                        if upgrade_response.get('message') == 'not_enough_balance':
                            print(Fore.RED + Style.BRIGHT + f"\r[ Upgrade Booster ] : Not enough balance", flush=True)
                        else:
                            print(Fore.GREEN + Style.BRIGHT + f"\r[ Upgrade Booster ] : Success to upgrade {upgrade_response}", flush=True)
                        
                    else:
                        print(Fore.RED + Style.BRIGHT + f"\r[ Upgrade Booster ] : Failed to upgrade {upgrade_response}", flush=True)
                    
                    tasks_response = get_tasks(auth)
                    if tasks_response:
                        for task in tasks_response:
                            if task.get('type') == 'upgrade' and task.get('status') == 'pending':
                                print(Fore.BLUE + Style.BRIGHT + f"\r[ Upgrade Booster ] : Pending, check again..",  flush=True)
                                time.sleep(10)
                                tasks_response = get_tasks(auth)
                                if tasks_response:
                                    for task in tasks_response:
                                        if task.get('type') == 'upgrade' and task.get('status') == 'success':
                                            print(Fore.GREEN + Style.BRIGHT + f"\r[ Upgrade Booster ] : Upgrade successful!", flush=True)
                                            break  # Keluar dari loop klaim jika klaim berhasil
                                        elif tasks_response == None:
                                            print(Fore.RED + Style.BRIGHT + f"\r[ Upgrade Booster ] : Upgrade successful!", flush=True)
                                        else:
                                            if task.get('type') == 'upgrade' and task.get('status') == 'pending':
                                                print(Fore.BLUE + Style.BRIGHT + f"\r[ Upgrade Booster ] : Pending, check again..",  flush=True)
                                            else:
                                                print(Fore.RED + Style.BRIGHT + f"\r[ Upgrade Booster ] : Upgrade status {tasks_response}", flush=True)
            time.sleep(2)  # Delay untuk mencegah rate limiting
        print(Fore.BLUE + Style.BRIGHT + f"\n==========SEMUA AKUN TELAH DI PROSES==========\n",  flush=True)    
        animate_energy_recharge(300) 

def print_welcome_message():
    print(r"""
          
█▀▀ █░█ ▄▀█ █░░ █ █▄▄ █ █▀▀
█▄█ █▀█ █▀█ █▄▄ █ █▄█ █ ██▄
          """)
    print(Fore.GREEN + Style.BRIGHT + "Onchain BOT")
    print(Fore.CYAN + Style.BRIGHT + "Update Link: https://github.com/adearman/onchain")
    print(Fore.YELLOW + Style.BRIGHT + "Free Konsultasi Join Telegram Channel: https://t.me/ghalibie")
    print(Fore.BLUE + Style.BRIGHT + "Buy me a coffee :) 0823 2367 3487 GOPAY / DANA")
    print(Fore.RED + Style.BRIGHT + "NOT FOR SALE ! Ngotak dikit bang. Ngoding susah2 kau tinggal rename :)\n\n")

def animate_energy_recharge(duration):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        for frame in frames:
            print(f"\rMenunggu waktu claim berikutnya {frame} - Tersisa {remaining_time} detik         ", end="", flush=True)
            time.sleep(0.25)
    print("\rMenunggu waktu claim berikutnya selesai.                            ", flush=True)     

if __name__ == "__main__":
    main()
