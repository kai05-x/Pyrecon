import tkinter as tk
import requests

def whois_lookup(domain_name, api_key):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName={domain_name}&outputFormat=JSON"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def print_whois_info_to_file(data):
    with open("who_is_result.txt", "w") as file:
        file.write("Domain Name: {}\n".format(data['WhoisRecord']['domainName']))
        file.write("Created Date: {}\n".format(data['WhoisRecord']['createdDate']))
        file.write("Updated Date: {}\n".format(data['WhoisRecord']['updatedDate']))
        file.write("Expires Date: {}\n\n".format(data['WhoisRecord']['expiresDate']))

        file.write("Registrant:\n")
        registrant = data['WhoisRecord']['registrant']
        file.write("    Name: {}\n".format(registrant.get('name', 'N/A')))
        file.write("    Organization: {}\n".format(registrant.get('organization', 'N/A')))
        file.write("    Street: {}\n".format(registrant.get('street1', 'N/A')))
        file.write("    City: {}\n".format(registrant.get('city', 'N/A')))
        file.write("    State: {}\n".format(registrant.get('state', 'N/A')))
        file.write("    Postal Code: {}\n".format(registrant.get('postalCode', 'N/A')))
        file.write("    Country: {}\n".format(registrant.get('country', 'N/A')))
        file.write("    Email: {}\n\n".format(registrant.get('email', 'N/A')))

        file.write("Administrative Contact:\n")
        administrative_contact = data['WhoisRecord']['administrativeContact']
        file.write("    Name: {}\n".format(administrative_contact.get('name', 'N/A')))
        file.write("    Organization: {}\n".format(administrative_contact.get('organization', 'N/A')))
        file.write("    Street: {}\n".format(administrative_contact.get('street1', 'N/A')))
        file.write("    City: {}\n".format(administrative_contact.get('city', 'N/A')))
        file.write("    State: {}\n".format(administrative_contact.get('state', 'N/A')))
        file.write("    Postal Code: {}\n".format(administrative_contact.get('postalCode', 'N/A')))
        file.write("    Country: {}\n".format(administrative_contact.get('country', 'N/A')))
        file.write("    Email: {}\n\n".format(administrative_contact.get('email', 'N/A')))

        file.write("Technical Contact:\n")
        technical_contact = data['WhoisRecord']['technicalContact']
        file.write("    Name: {}\n".format(technical_contact.get('name', 'N/A')))
        file.write("    Organization: {}\n".format(technical_contact.get('organization', 'N/A')))
        file.write("    Street: {}\n".format(technical_contact.get('street1', 'N/A')))
        file.write("    City: {}\n".format(technical_contact.get('city', 'N/A')))
        file.write("    State: {}\n".format(technical_contact.get('state', 'N/A')))
        file.write("    Postal Code: {}\n".format(technical_contact.get('postalCode', 'N/A')))
        file.write("    Country: {}\n".format(technical_contact.get('country', 'N/A')))
        file.write("    Email: {}\n\n".format(technical_contact.get('email', 'N/A')))

        file.write("Name Servers:\n")
        for name_server in data['WhoisRecord']['nameServers']['hostNames']:
            file.write("    {}\n".format(name_server))

def fetch_and_display_info():
    domain_name = domain_entry.get()
    api_key = "at_XHXqYRtQlO1W7Yqv0oa2Cj7ciGhUj"

    result = whois_lookup(domain_name, api_key)
    if result:
        print_whois_info_to_file(result)
        info_text = print_whois_info_to_file(result)

def main1():
    root = tk.Tk()
    root.geometry("300x200")
    root.configure(bg="black")
    root.title("WHOIS Lookup")
    root.resizable( False, False)

    label = tk.Label(root, text="Enter Domain:", fg="white", bg="black")
    label.pack(pady=10)

    global domain_entry
    domain_entry = tk.Entry(root, width=30)
    domain_entry.pack(pady=10)

    search_button = tk.Button(root, text="Search", bg="light blue", command=fetch_and_display_info)
    search_button.pack(pady=5)


    root.mainloop()

if __name__ == "__main__":
    main1()
