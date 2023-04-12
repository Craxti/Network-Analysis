**Network and Security Analysis Tool**

This tool provides various functionalities to perform network and security analysis. The tool utilizes argparse module to allow users to select the desired functionality through command-line arguments.


**Installation**

1. Clone the repository:

`git clone https://github.com/exampleuser/security-scanner.git`

2. Install the required packages:

`pip install -r requirements.txt`

**Usage**

To use this tool, you can run the main.py script from the command line. The tool accepts a number of command-line arguments, which are described below:

`main.py [-h] [-s CIDR_ADDRESS] [-c ASN] [-t IP_ADDRESS] [-geo IP_ADDRESS] [-b EMAIL_OR_USERNAME] [-e DIRECTORY] [-f FORMAT] [-i FIELD [FIELD ...]] [-r] [-p IP_ADDRESS]
               [--hibp] [--greynoise] [--alienvault] [--securitytrails] [-a SEARCH_TERM] [-n ADDRESS] [-d DOMAIN] [--scan {hibp,greynoise,alienvault,securitytrails}]`

Options

    `
    -h, --help            show this help message and exit
      -s CIDR_ADDRESS, --scan_network CIDR_ADDRESS
                            Scan a network for open ports
      -c ASN, --check_asn ASN
                            Check information about an ASN
      -t IP_ADDRESS, --threat_analysis IP_ADDRESS
                            Perform threat analysis on an IP address
      -geo IP_ADDRESS, --ip_geolocation IP_ADDRESS
                            Perform geolocation on an IP address
      -b EMAIL_OR_USERNAME, --check_breaches EMAIL_OR_USERNAME
                            Check if an email or username has been involved in a data breach
      -e DIRECTORY, --extract_metadata DIRECTORY
                            Extract metadata from files in a directory
      -f FORMAT, --format FORMAT
                            Output format (csv, json, etc.)
      -i FIELD [FIELD ...], --include FIELD [FIELD ...]
                            Include only specified metadata fields
      -r, --recursive       Process files in subdirectories
      -p IP_ADDRESS, --scan_ip IP_ADDRESS
                            Scan an IP address for open ports
      --hibp                Check if email has been breached using HIBP API
      --greynoise           Get information on IP address using GreyNoise API
      --alienvault          Get information on IP address using AlienVault API
      --securitytrails      Get information on subdomain using SecurityTrails API
      -a SEARCH_TERM, --api_search SEARCH_TERM
                            Search various security APIs for information
      -n ADDRESS, --crypto_check ADDRESS
                            Check if an address is a valid Bitcoin or Ethereum address
      -d DOMAIN, --domain_scanner DOMAIN
                            Scan a domain and enumerate subdomains
      --scan {hibp,greynoise,alienvault,securitytrails}`

**Examples**

Scan an email address with HIBP

`python main.py --scan hibp --email john.doe@example.com`
    
Scan an IP address with GreyNoise

`python main.py --scan greynoise --ip 8.8.8.8`

Scan an IP address with AlienVault

`python main.py --scan alienvault --ip 8.8.8.8`

Scan a subdomain with SecurityTrails

`python main.py --scan securitytrails --subdomain example.com`

Geolocate an IP address

`python main.py --ip_geolocation 8.8.8.8`

Check if a given Bitcoin or Ethereum address has been involved in any known scams or hacks

`python crypto_check.py --address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
python crypto_check.py --address 0x742d35Cc6634C0532925a3b844Bc454e4438f44e`

Perform searches on various APIs

`python api_search.py --query shodan --ip 192.168.1.1
python api_search.py --query hibp --email user@example.com`


**Contributing**

Contributions are welcome! If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.