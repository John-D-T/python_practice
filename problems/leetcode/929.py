class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # local_name  domain name
        # ignoring everything after the plus sign in the first part
        # ignoring periods in the first part


        # 1. parse the local_name

        # 2. parse the domain name

        # adding this to a hashmap to see if it exists there

        valid_emails = list()

        for email in emails:
            local_name, domain_name = email.split('@')[0], email.split('@')[1]

            local_name_refined = local_name.split('+')[0].replace('.', '')

            email_refined = local_name_refined + '@' + domain_name

            if email_refined not in valid_emails:
                valid_emails.append(email_refined)

        return len(valid_emails)