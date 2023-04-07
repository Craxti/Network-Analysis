**Network and Security Analysis Tool**

This tool provides various functionalities to perform network and security analysis. The tool utilizes argparse module to allow users to select the desired functionality through command-line arguments.


**Installation**

1. Clone the repository:

`git clone https://github.com/exampleuser/security-scanner.git`

2. Install the required packages:

`pip install -r requirements.txt`

**Usage**

To run the security scanner, use the following command:

`python main.py [options]`

Options

    -h, --help: Show the help message and exit.
    --scan: Select the scan to perform. Available options: hibp, greynoise, alienvault, securitytrails.
    --email: The email address to scan (required for hibp scan).
    --ip: The IP address to scan (required for greynoise and alienvault scans).
    --subdomain: The subdomain to scan (required for securitytrails scan).
    --ip_geolocation: The IP address to geolocate using the ipstack API.

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