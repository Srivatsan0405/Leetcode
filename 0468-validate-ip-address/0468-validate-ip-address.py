class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if part[0] == '0' and len(part) != 1:
                    return False
            return True

        def isIPv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            hex_digits = '0123456789abcdefABCDEF'
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return False
                if not all(c in hex_digits for c in part):
                    return False
            return True

        if '.' in queryIP and isIPv4(queryIP):
            return "IPv4"
        elif ':' in queryIP and isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
