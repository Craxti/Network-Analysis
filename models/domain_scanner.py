import os
import dns.resolver


def scan_domain(domain_name, query_type='A', save_results=False):
    try:
        answers = dns.resolver.resolve(domain_name, query_type)
    except dns.resolver.NoAnswer:
        result = f"No records found for {domain_name}"
    except dns.resolver.NXDOMAIN:
        result = f"{domain_name} does not exist"
    else:
        records = [answer.to_text() for answer in answers]
        result = {"Domain Name": domain_name, "Records": records}

        if save_results:
            with open(f"{domain_name}_{query_type}.txt", "w") as f:
                f.write("\n".join(records))

    return result


def enum_subdomains(domain_name, save_results=False):
    subdomains = []

    wordlist_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wordlists", "subdomains.txt")
    with open(wordlist_path, "r") as f:
        subdomain_list = [line.strip() for line in f.readlines()]

    for subdomain in subdomain_list:
        try:
            dns.resolver.resolve(f"{subdomain}.{domain_name}", "A")
            subdomains.append(f"{subdomain}.{domain_name}")
        except dns.resolver.NXDOMAIN:
            pass

    if save_results:
        with open(f"{domain_name}_subdomains.txt", "w") as f:
            f.write("\n".join(subdomains))

    return subdomains
