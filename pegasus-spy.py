from modules import (get_bitcoin_data, get_ciphers, heart_bleed,
                     get_company_detail, fetch_email, get_device, ip_details, VirusTotal)


def display_menu():
    print("""
    ############################################
    #        OSINT-Pegasus Spy Command Menu    #
    ############################################
    1. Get latest bitcoin block info
    2. Get bitcoin block info by date (e.g., 20190614)
    3. Get info of any bitcoin wallet address
    4. List out supported SSL ciphers used by any domain
    5. Check whether server is vulnerable to heart bleed
    6. Perform domain recon
    7. Perform email recon
    8. Explore the Internet of Things (IoT)
    9. WHOIS IP Lookup
    10. Send files to VirusTotal for malware analysis
    11. Exit
    """)


def get_user_choice():
    try:
        choice = int(input("Enter your choice (1-11): "))
        if 1 <= choice <= 11:
            return choice
        else:
            print("Invalid choice! Please select a valid option.")
            return get_user_choice()
    except ValueError:
        print("Invalid input! Please enter a number.")
        return get_user_choice()


def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            url = 'https://chain.api.btc.com/v3/block/latest'
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            get_bitcoin_data(url, json_output)

        elif choice == 2:
            date = input("Enter the date (YYYYMMDD): ").strip()
            url = f'https://chain.api.btc.com/v3/block/date/{date}'
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            get_bitcoin_data(url, json_output)

        elif choice == 3:
            address = input("Enter the bitcoin wallet address: ").strip()
            url = f'https://chain.api.btc.com/v3/address/{address}'
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            get_bitcoin_data(url, json_output)

        elif choice == 4:
            server = input("Enter the domain to check SSL ciphers: ").strip()
            get_ciphers(server)

        elif choice == 5:
            server = input("Enter the server to check for Heart Bleed: ").strip()
            heart_bleed(server)

        elif choice == 6:
            domain = input("Enter the domain for recon: ").strip()
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            get_company_detail(domain, json_output)

        elif choice == 7:
            email_id = input("Enter the email for recon: ").strip()
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            fetch_email(email_id, json_output)

        elif choice == 8:
            device_name = input("Enter the IoT device name (e.g., opensips, juniper): ").strip()
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            get_device(device_name, json_output)

        elif choice == 9:
            ip = input("Enter the IP for WHOIS Lookup: ").strip()
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            ip_details(ip, json_output)

        elif choice == 10:
            mal_path = input("Enter the file path for malware analysis: ").strip()
            json_output = input("Show output in JSON format? (y/n): ").strip().lower() == 'y'
            api = VirusTotal()
            api.send_malware(mal_path, json_output)

        elif choice == 11:
            print("Exiting OSINT-Pegasus Spy. Goodbye!")
            break


if __name__ == "__main__":
    main()
