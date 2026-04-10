class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        _set = set()

        for email in emails:
            email = email.strip()
            name, domain = email.split('@')

            #ignore everything after first '+'
            name = name.split('+')[0]

            name = ''.join(name.split('.'))

            _set.add(name+'@'+domain)
        
        return len(_set)

            
