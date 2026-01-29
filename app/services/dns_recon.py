import dns.resolver

class DNSRecon:
    def get_records(self, domain: str):
        results = {}
        for record_type in ['A', 'MX', 'TXT', 'NS']:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                results[record_type] = [str(r) for r in answers]
            except:
                results[record_type] = []
        return results

dns_recon = DNSRecon()