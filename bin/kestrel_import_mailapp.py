import plistlib

# http://mechanicalcat.net/richard/log/Python/OS_X_Mail_app_rules_to_sieve_filters

p = plistlib.readPlist('/Users/idm/Library/Mail/V2/MailData/MessageRules.plist')

print '''
require ["fileinto", "reject"];
'''
stmt = 'if'
def handle(header, expression, mbox):
    global stmt
    if header in ('To', 'Cc', 'From', 'Sender', 'reply-to'):
        print stmt, 'address :contains ["%s"]  "%s" { fileinto "INBOX.%s"; }' % (header, expression, mbox)
    elif header == 'Subject':
        print stmt, 'header :matches "Subject" ["*%s*"] { fileinto "INBOX.%s"; }' % (expression, mbox)
    elif header == 'SenderIsMemberOfGroup':
        print "#", header, ':', expression, '->', mbox
    elif header == 'DateReceived':
        print "#", header, expression, mbox
    else:
        raise ValueError(header)
    stmt = 'elsif'

for rule in p['rules']:
    if 'Mailbox' not in rule: continue
    mbox = rule['Mailbox'].split('/')[-1].split('.')[0]
    print "\n#", rule['RuleName'], '->', mbox
    for criteria in rule['Criteria']:
        if criteria['Header'] == 'AnyRecipient':
            handle('To', criteria['Expression'], mbox)
            handle('Cc', criteria['Expression'], mbox)
        elif 'Expression' in criteria:
            handle(criteria['Header'], criteria['Expression'], mbox)
        else:
            print '#', criteria

print '''
else {
     keep;
}
'''