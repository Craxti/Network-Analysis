import argparse

from models.scan_network import scan_network
from models.check_asn import check_asn
from models.threat_analysis import threat_analysis
from models.ip_geolocation import ip_geolocation, geolocate_ip
from models.check_breaches import check_breaches
from models.extract_metadata import extract_metadata
from models.scan_ip import scan_ip
from models.api_search import shodan_scan, hibp_breach, greynoise_ip, alienvault_ip, securitytrails_subdomain
from models.crypto_check import get_bitcoin_address, get_ethereum_address
from models.domain_scanner import scan_domain, enum_subdomains

# create the parser
parser = argparse.ArgumentParser(description='Tool for network and security analysis')

# add the arguments
parser.add_argument('-s', '--scan_network', metavar='CIDR_ADDRESS', help='Scan a network for open ports')
parser.add_argument('-c', '--check_asn', metavar='ASN', help='Check information about an ASN')
parser.add_argument('-t', '--threat_analysis', metavar='IP_ADDRESS', help='Perform threat analysis on an IP address')
parser.add_argument('-geo', '--ip_geolocation', metavar='IP_ADDRESS', help='Perform threat analysis on an IP address')
parser.add_argument('-g', '--geolocate_ip', metavar='IP_ADDRESS', help='Geolocate an IP address')
parser.add_argument('-b', '--check_breaches', metavar='EMAIL', help='Check if an email has been involved in a data breach')
#extract_metadata
parser.add_argument('-e', '--extract_metadata', metavar='DIRECTORY', help='Extract metadata from files in a directory')
parser.add_argument('-f', '--format', metavar='FORMAT', help='Output format (csv, json, etc.)')
parser.add_argument('-i', '--include', metavar='FIELD', nargs='+', help='Include only specified metadata fields')
parser.add_argument('-r', '--recursive', action='store_true', help='Process files in subdirectories')


parser.add_argument('-p', '--scan_ip', metavar='IP_ADDRESS', help='Scan an IP address for open ports')
parser.add_argument('--hibp', action='store_true', help='Check if email has been breached using HIBP API')
parser.add_argument('--greynoise', action='store_true', help='Get information on IP address using GreyNoise API')
parser.add_argument('--alienvault', action='store_true', help='Get information on IP address using AlienVault API')
parser.add_argument('--securitytrails', action='store_true', help='Get information on subdomain using SecurityTrails API')
parser.add_argument('-a', '--api_search', metavar='SEARCH_TERM', help='Search various security APIs for information')
parser.add_argument('-n', '--crypto_check', metavar='ADDRESS', help='Check if an address is a valid Bitcoin or Ethereum address')
parser.add_argument('-d', '--domain_scanner', metavar='DOMAIN', help='Scan a domain and enumerate subdomains')
parser.add_argument('--scan', choices=['hibp', 'greynoise', 'alienvault', 'securitytrails'], help='Choose a scan to run')


# parse the arguments
args = parser.parse_args()

# call the appropriate function based on the argument passed
if args.scan_network:
    results = scan_network(args.scan_network)
    print(results)
elif args.check_asn:
    results = check_asn(args.check_asn)
    print(results)
elif args.threat_analysis:
    results = threat_analysis(args.threat_analysis)
    print(results)
elif args.geolocate_ip:
    results = geolocate_ip(args.geolocate_ip)
    print(results)
elif args.check_breaches:
    results = check_breaches(args.check_breaches)
    print(results)
elif args.extract_metadata:
    results = extract_metadata(args.extract_metadata, args.format, args.include, args.recursive)
    print(results)
elif args.scan_ip:
    results = scan_ip(args.scan_ip)
    print(results)
elif args.api_search:
    results = shodan_scan(args.api_search)
    print(results)
elif args.crypto_check:
    results = get_bitcoin_address(args.crypto_check)
    print(results)
    results = get_ethereum_address(args.crypto_check)
    print(results)
elif args.domain_scanner:
    results = scan_domain(args.domain_scanner)
    print(results)
    results = enum_subdomains(args.domain_name)
    print(results)
elif args.scan == 'hibp' and args.email:
    hibp_breach(args.email)
elif args.scan == 'greynoise' and args.ip:
    greynoise_ip(args.ip)
elif args.scan == 'alienvault' and args.ip:
    alienvault_ip(args.ip)
elif args.scan == 'securitytrails' and args.subdomain:
    securitytrails_subdomain(args.subdomain)
elif args.ip_geolocation:
    result = ip_geolocation(args.ip_geolocation)
else:
    parser.print_help()