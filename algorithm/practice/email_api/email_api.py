def get_emails(emails):
    email_set = set()
    for email in emails:
        email_list = []
        for letter in email:
            if letter == ".":
                continue
            elif letter == "+" or letter == "@":
                break
            else:
                email_list.append(letter)
        email_set.add("".join(email_list))
    return len(email_set)


#test
emails = ["test@yahoo.com", "test.2@yahoo.com", "test+3@yahoo.com", "test@gmail.com", "test2@gmail.com",
         "test4@yahoo.com"]
get_emails(emails)