"""Email verification service with SMTP checking"""
import smtplib
import dns.resolver
import re
from typing import Dict, Any
from email.utils import parseaddr

class EmailVerifier:
    """Real SMTP email verification service"""
    
    def __init__(self):
        self.disposable_domains = [
            'tempmail.com', 'guerrillamail.com', '10minutemail.com',
            'mailinator.com', 'throwaway.email', 'temp-mail.org'
        ]
    
    def verify_smtp(self, email: str) -> Dict[str, Any]:
        """
        Verify email using SMTP protocol
        
        Args:
            email: Email address to verify
            
        Returns:
            Dictionary with verification results
        """
        try:
            # Basic email format validation
            if not self._is_valid_format(email):
                return {
                    "email": email,
                    "status": "invalid",
                    "smtp_valid": False,
                    "disposable": False,
                    "breach_found": False,
                    "error": "Invalid email format"
                }
            
            # Extract domain
            _, domain = email.split('@')
            
            # Check if disposable
            is_disposable = domain.lower() in self.disposable_domains
            
            # Check MX records
            mx_records = self._get_mx_records(domain)
            if not mx_records:
                return {
                    "email": email,
                    "status": "invalid",
                    "smtp_valid": False,
                    "disposable": is_disposable,
                    "breach_found": False,
                    "error": "No MX records found"
                }
            
            # Try SMTP verification
            smtp_valid = self._check_smtp(email, mx_records[0])
            
            return {
                "email": email,
                "status": "valid" if smtp_valid else "unknown",
                "smtp_valid": smtp_valid,
                "disposable": is_disposable,
                "breach_found": False,
                "details": {
                    "mx_records": mx_records,
                    "domain": domain
                }
            }
            
        except Exception as e:
            return {
                "email": email,
                "status": "unknown",
                "smtp_valid": False,
                "disposable": False,
                "breach_found": False,
                "error": str(e)
            }
    
    def _is_valid_format(self, email: str) -> bool:
        """Check if email has valid format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def _get_mx_records(self, domain: str) -> list:
        """Get MX records for domain"""
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            return [str(r.exchange).rstrip('.') for r in mx_records]
        except Exception:
            return []
    
    def _check_smtp(self, email: str, mx_host: str) -> bool:
        """
        Check email via SMTP
        Note: Many servers block SMTP verification, so this may return False even for valid emails
        """
        try:
            # Connect to mail server
            server = smtplib.SMTP(timeout=10)
            server.connect(mx_host)
            server.helo(server.local_hostname)
            server.mail('verify@example.com')
            code, _ = server.rcpt(email)
            server.quit()
            
            # 250 = success, 251 = user not local (but valid)
            return code in [250, 251]
        except Exception:
            # If SMTP check fails, we can't determine validity
            return False

# Global instance
email_verifier = EmailVerifier()
