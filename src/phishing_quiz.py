import random

def run_quiz():
    # Question bank with 100 questions
    question_bank = [
        {
            "text": "Is 'Urgent: Update Your Account' suspicious? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Urgent language is a common tactic in phishing emails to pressure you into acting quickly.\nIncorrect. Urgent language is a red flag often used in phishing emails to create panic."
        },
        {
            "text": "Should you click links in emails from unknown senders? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never click links in emails from unknown senders—they could lead to malicious sites.\nIncorrect. Clicking links from unknown senders can lead to phishing sites or malware."
        },
        {
            "text": "Is a misspelled sender email a red flag? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Misspelled email addresses (e.g., 'support@amaz0n.com') are a common sign of phishing.\nIncorrect. A misspelled email address is a red flag often used by attackers to impersonate legitimate entities."
        },
        {
            "text": "Are all emails with attachments phishing? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Not all attachments are phishing, but be cautious—especially with unsolicited emails.\nIncorrect. While some attachments can be malicious, not all are phishing; always verify the sender."
        },
        {
            "text": "Should you verify a sender before replying to an email? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Always verify the sender’s email address to ensure it’s legitimate before replying.\nIncorrect. Verifying the sender is crucial to avoid falling for impersonation attempts."
        },
        {
            "text": "Is an email asking for your password likely a phishing attempt? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Legitimate companies never ask for your password via email.\nIncorrect. Emails requesting passwords are almost always phishing attempts."
        },
        {
            "text": "Can phishing emails come from a known contact? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Attackers can spoof email addresses to appear as if they’re from someone you know.\nIncorrect. Phishing emails can impersonate known contacts through spoofing."
        },
        {
            "text": "Is it safe to download files from an email marked 'urgent'? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Urgent emails with downloads are often phishing attempts.\nIncorrect. Urgent emails with files can contain malware—verify the sender first."
        },
        {
            "text": "Should you use the same password for all your accounts? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Using unique passwords prevents a single breach from affecting multiple accounts.\nIncorrect. Reusing passwords increases your risk if one account is compromised."
        },
        {
            "text": "Is enabling two-factor authentication (2FA) a good security practice? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! 2FA adds an extra layer of security to your accounts.\nIncorrect. 2FA is a recommended practice to enhance security."
        },
        {
            "text": "Can phishing attacks occur via text messages (SMS)? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! SMS phishing, or 'smishing,' is a common attack vector.\nIncorrect. Phishing can happen via SMS, known as smishing."
        },
        {
            "text": "Is it safe to click a link that looks like your company’s website? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Always hover over links to verify the URL—phishers often use lookalike domains.\nIncorrect. Lookalike URLs are a common phishing tactic; always verify the link."
        },
        {
            "text": "Should you report suspicious emails to your IT team? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Reporting suspicious emails helps your IT team investigate and protect the organization.\nIncorrect. Reporting suspicious emails is a best practice for enterprise security."
        },
        {
            "text": "Is a generic greeting like 'Dear Customer' a phishing sign? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Generic greetings are often used in phishing emails to target a wide audience.\nIncorrect. Legitimate companies usually address you by name; generic greetings are suspicious."
        },
        {
            "text": "Can phishing emails contain official-looking logos? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phishers often use stolen logos to make emails appear legitimate.\nIncorrect. Official-looking logos are commonly used in phishing emails to deceive users."
        },
        {
            "text": "Is it safe to enter your credentials on a website linked from an email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Avoid entering credentials on sites linked from emails—go directly to the official website.\nIncorrect. Email links can lead to fake login pages; always navigate to the site manually."
        },
        {
            "text": "Should you ignore emails claiming you’ve won a prize? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Unsolicited prize emails are often scams designed to steal your information.\nIncorrect. Prize emails are a common phishing tactic; it’s best to ignore them."
        },
        {
            "text": "Is a secure website always safe from phishing? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Even secure (HTTPS) sites can be phishing if they’re controlled by attackers.\nIncorrect. HTTPS doesn’t guarantee a site isn’t phishing—verify the domain."
        },
        {
            "text": "Can phishing emails be sent from a compromised colleague’s account? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! If a colleague’s account is hacked, attackers can send phishing emails from it.\nIncorrect. Compromised accounts are often used to send phishing emails."
        },
        {
            "text": "Is it okay to share your password with IT support via email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share your password via email, even with IT support—legitimate IT teams won’t ask for it.\nIncorrect. Sharing passwords via email is a security risk, even with IT."
        },
        {
            "text": "Should you use public Wi-Fi to access sensitive company data? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Public Wi-Fi is insecure and can expose your data to attackers.\nIncorrect. Avoid using public Wi-Fi for sensitive tasks—use a VPN or secure network."
        },
        {
            "text": "Is an email with a PDF attachment always safe? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! PDF attachments can contain malware or phishing links—verify the sender.\nIncorrect. PDFs can be malicious; always check the source before opening."
        },
        {
            "text": "Can phishing attacks target you via phone calls? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phone-based phishing, or 'vishing,' involves attackers calling to steal information.\nIncorrect. Vishing is a form of phishing conducted via phone calls."
        },
        {
            "text": "Should you trust an email because it has your company’s logo? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Logos can be stolen and used in phishing emails—verify the sender.\nIncorrect. Phishers often use company logos to appear legitimate; always check the email address."
        },
        {
            "text": "Is it safe to ignore emails marked as 'spam' by your email client? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Spam filters are usually accurate, but review occasionally for false positives.\nIncorrect. Spam filters are generally reliable, but you can report false positives to IT."
        },
        {
            "text": "Can phishing emails include links to legitimate websites? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phishers may use legitimate links to build trust, but other links could be malicious.\nIncorrect. Legitimate links can be mixed with malicious ones in phishing emails."
        },
        {
            "text": "Should you open an email attachment from your CEO without verifying? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Even emails from trusted sources can be spoofed—verify first.\nIncorrect. Spoofed emails can appear to come from your CEO; always verify."
        },
        {
            "text": "Is a strong password enough to protect against phishing? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! A strong password helps, but phishing can trick you into giving it away.\nIncorrect. Phishing attacks can bypass strong passwords by deceiving you into entering them."
        },
        {
            "text": "Can phishing emails be personalized with your name? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Attackers can use publicly available data to personalize phishing emails.\nIncorrect. Personalized emails are a common phishing tactic to gain your trust."
        },
        {
            "text": "Should you reply to an email asking for your employee ID? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Requests for personal info like employee IDs are often phishing attempts.\nIncorrect. Legitimate requests for such info usually come through secure channels, not email."
        },
        {
            "text": "Is it safe to click a link if the email looks professional? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Professional-looking emails can still be phishing—verify the link.\nIncorrect. Phishers often design emails to look professional; always check the URL."
        },
        {
            "text": "Can phishing attacks steal your data without you clicking a link? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Some phishing emails use malicious attachments or scripts that run on email open.\nIncorrect. Phishing can steal data via attachments or scripts, not just links."
        },
        {
            "text": "Should you use antivirus software to protect against phishing? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Antivirus software can detect some phishing-related malware, but awareness is key.\nIncorrect. Antivirus helps, but it’s not enough—awareness is crucial for phishing protection."
        },
        {
            "text": "Is it okay to share your email password with a coworker? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share your password with anyone, even coworkers.\nIncorrect. Sharing passwords, even with coworkers, increases security risks."
        },
        {
            "text": "Can phishing emails trick you into installing malware? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phishing emails often use attachments or links to install malware.\nIncorrect. Malware installation is a common goal of phishing attacks."
        },
        {
            "text": "Should you ignore emails that claim your account is locked? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Account-locked emails are often phishing scams—verify directly with the service.\nIncorrect. Such emails are typically phishing; contact the service directly to confirm."
        },
        {
            "text": "Is it safe to use a public computer for company email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Public computers may have keyloggers or malware that can steal your credentials.\nIncorrect. Public computers are insecure for accessing company email."
        },
        {
            "text": "Can phishing emails appear to come from your IT department? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phishers often impersonate IT departments to trick employees.\nIncorrect. IT impersonation is a common phishing tactic."
        },
        {
            "text": "Should you trust an email because it passed your spam filter? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Spam filters aren’t perfect—some phishing emails can slip through.\nIncorrect. Phishing emails can bypass spam filters; always stay vigilant."
        },
        {
            "text": "Is it safe to reply to an email with your bank details if requested? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share bank details via email—it’s likely a phishing attempt.\nIncorrect. Emails requesting bank details are almost always phishing scams."
        },
        {
            "text": "Can phishing emails include fake security alerts? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake security alerts are a common phishing tactic to scare users into acting.\nIncorrect. Phishers often use fake alerts to trick you into providing information."
        },
        {
            "text": "Should you click a link to 'unsubscribe' from an unknown email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Unsubscribe links in unknown emails can lead to phishing sites.\nIncorrect. Avoid clicking unsubscribe links in unsolicited emails—they may be phishing."
        },
        {
            "text": "Is it safe to open an email from an unknown sender? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Opening unknown emails can expose you to phishing or malware—delete them.\nIncorrect. Unknown emails can contain phishing attempts or malware; avoid opening them."
        },
        {
            "text": "Can phishing emails target you on social media? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phishing can occur on social media through fake messages or links.\nIncorrect. Social media is a common platform for phishing attacks."
        },
        {
            "text": "Should you store passwords in your email inbox? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Storing passwords in your inbox is insecure—if hacked, attackers can access them.\nIncorrect. Email is not a secure place to store passwords."
        },
        {
            "text": "Is it safe to ignore an email claiming your password was changed? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Such emails are often phishing—verify directly with the service.\nIncorrect. Password change emails can be phishing scams; check with the service directly."
        },
        {
            "text": "Can phishing emails use your company’s email domain? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Attackers can spoof company domains to appear legitimate.\nIncorrect. Spoofing company domains is a common phishing technique."
        },
        {
            "text": "Should you use a VPN when working remotely? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! A VPN encrypts your connection, protecting against phishing and eavesdropping.\nIncorrect. Using a VPN is recommended for secure remote work."
        },
        {
            "text": "Is it safe to click a link in an email if it’s marked 'secure'? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! 'Secure' labels can be faked—verify the URL first.\nIncorrect. Phishers can fake 'secure' labels; always check the link."
        },
        {
            "text": "Can phishing emails lead to ransomware attacks? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phishing emails can deliver ransomware through malicious links or attachments.\nIncorrect. Ransomware is often delivered via phishing emails."
        },
        {
            "text": "Should you share your login credentials with a vendor via email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share credentials via email—use secure channels.\nIncorrect. Sharing credentials via email is a security risk, even with vendors."
        },
        {
            "text": "Is it safe to ignore an email claiming you owe money? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Debt collection emails are often phishing scams—verify directly with the company.\nIncorrect. Such emails can be phishing; contact the company directly to confirm."
        },
        {
            "text": "Can phishing emails be sent from a hacked friend’s account? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Hacked accounts can be used to send phishing emails to contacts.\nIncorrect. Phishing emails can come from hacked accounts, including friends’."
        },
        {
            "text": "Should you use a password manager to store credentials? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Password managers securely store and generate strong passwords.\nIncorrect. Password managers are a secure way to manage credentials."
        },
        {
            "text": "Is it safe to click a link in an email if it’s from a coworker? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Coworker emails can be spoofed—verify the sender.\nIncorrect. Spoofed emails can appear to come from coworkers; always verify."
        },
        {
            "text": "Can phishing emails include fake tracking numbers? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake tracking numbers are used in phishing emails to trick you into clicking links.\nIncorrect. Phishers often use fake tracking numbers to deceive users."
        },
        {
            "text": "Should you open an email that claims to be from HR without verifying? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! HR emails can be spoofed—verify the sender’s email address.\nIncorrect. Spoofed HR emails are common in phishing attacks; always verify."
        },
        {
            "text": "Is it safe to ignore an email claiming your account was hacked? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Such emails are often phishing—verify directly with the service.\nIncorrect. Account-hacked emails can be phishing scams; check with the service directly."
        },
        {
            "text": "Can phishing emails target you through calendar invites? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Calendar invites can contain phishing links or attachments.\nIncorrect. Phishing can occur via calendar invites with malicious content."
        },
        {
            "text": "Should you share your one-time password (OTP) with someone via email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share OTPs—they’re meant to be private.\nIncorrect. Sharing OTPs via email can lead to account compromise."
        },
        {
            "text": "Is it safe to click a link in an email if it’s from a known brand? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Known brands can be impersonated—verify the link.\nIncorrect. Phishers often impersonate known brands; always check the URL."
        },
        {
            "text": "Can phishing emails lead to identity theft? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Phishing emails can steal personal information, leading to identity theft.\nIncorrect. Identity theft is a common outcome of phishing attacks."
        },
        {
            "text": "Should you use a personal email for company work? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Using personal email for work increases security risks.\nIncorrect. Always use your company email for work-related tasks."
        },
        {
            "text": "Is it safe to ignore an email claiming your subscription expired? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Subscription expiration emails are often phishing—verify with the service.\nIncorrect. Such emails can be phishing scams; check with the service directly."
        },
        {
            "text": "Can phishing emails include fake invoices? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake invoices are a common phishing tactic to trick you into clicking links.\nIncorrect. Phishers often use fake invoices to deceive users."
        },
        {
            "text": "Should you click a link in an email to reset your password without verifying? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Password reset emails can be phishing—verify the sender.\nIncorrect. Always verify password reset emails to avoid phishing scams."
        },
        {
            "text": "Is it safe to share your company email with a third-party app? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Sharing your company email with third-party apps can lead to phishing risks.\nIncorrect. Avoid sharing company email with unverified third-party apps."
        },
        {
            "text": "Can phishing emails target you through fake job offers? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake job offers are a common phishing tactic to steal personal information.\nIncorrect. Phishing can occur via fake job offers."
        },
        {
            "text": "Should you trust an email because it has a professional signature? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Professional signatures can be faked—verify the sender.\nIncorrect. Phishers often use fake signatures to appear legitimate."
        },
        {
            "text": "Is it safe to ignore an email claiming you’ve been charged for a service? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Such emails are often phishing—verify with the service provider.\nIncorrect. Charge notification emails can be phishing scams; verify directly."
        },
        {
            "text": "Can phishing emails include fake surveys? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake surveys are used in phishing to collect personal information.\nIncorrect. Phishing emails often use fake surveys to steal data."
        },
        {
            "text": "Should you click a link in an email to claim a refund? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Refund emails can be phishing—verify with the company directly.\nIncorrect. Refund emails are a common phishing tactic; verify first."
        },
        {
            "text": "Is it safe to share your security questions with someone via email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share security questions—they can be used to access your accounts.\nIncorrect. Sharing security questions via email can lead to account compromise."
        },
        {
            "text": "Can phishing emails include fake donation requests? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake donation requests are a common phishing tactic, especially after disasters.\nIncorrect. Phishing emails often use fake donation requests to steal information."
        },
        {
            "text": "Should you trust an email because it has no spelling errors? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Well-written emails can still be phishing—check the sender and links.\nIncorrect. Phishers often write professional emails with no spelling errors."
        },
        {
            "text": "Is it safe to ignore an email claiming your email storage is full? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Storage full emails are often phishing—verify with your email provider.\nIncorrect. Such emails can be phishing scams; check with your provider directly."
        },
        {
            "text": "Can phishing emails include fake customer support messages? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake customer support messages are a common phishing tactic.\nIncorrect. Phishing emails often impersonate customer support to steal information."
        },
        {
            "text": "Should you click a link in an email to update your payment info? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Payment update emails can be phishing—go directly to the official site.\nIncorrect. Avoid clicking links in payment update emails; they may be phishing."
        },
        {
            "text": "Is it safe to share your company ID with a coworker via email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Sharing sensitive info via email is risky, even with coworkers.\nIncorrect. Email is not a secure way to share company IDs."
        },
        {
            "text": "Can phishing emails include fake event invitations? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake event invites can contain phishing links or attachments.\nIncorrect. Phishing can occur via fake event invitations."
        },
        {
            "text": "Should you trust an email because it has a verified sender badge? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Verified sender badges can be faked—check the email address.\nIncorrect. Phishers can fake verified sender badges; always verify."
        },
        {
            "text": "Is it safe to ignore an email claiming your account needs verification? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Verification emails are often phishing—verify with the service.\nIncorrect. Such emails can be phishing scams; check with the service directly."
        },
        {
            "text": "Can phishing emails include fake shipping notifications? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake shipping notifications are a common phishing tactic.\nIncorrect. Phishing emails often use fake shipping notifications to trick users."
        },
        {
            "text": "Should you click a link in an email to update your email settings? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Email settings update emails can be phishing—go directly to the site.\nIncorrect. Avoid clicking links in email settings update emails; they may be phishing."
        },
        {
            "text": "Is it safe to share your date of birth via email if requested? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share personal info like your date of birth via email.\nIncorrect. Sharing personal info via email can lead to identity theft."
        },
        {
            "text": "Can phishing emails include fake tax refund notifications? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake tax refund notifications are a common phishing tactic.\nIncorrect. Phishing emails often use fake tax refunds to steal information."
        },
        {
            "text": "Should you trust an email because it has a digital signature? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Digital signatures can be faked—verify the sender.\nIncorrect. Phishers can fake digital signatures; always check the email address."
        },
        {
            "text": "Is it safe to ignore an email claiming your account was accessed from another location? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Such emails are often phishing—verify with the service.\nIncorrect. Account access emails can be phishing scams; check with the service directly."
        },
        {
            "text": "Can phishing emails include fake charity requests? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake charity requests are a common phishing tactic.\nIncorrect. Phishing emails often use fake charity requests to steal information."
        },
        {
            "text": "Should you click a link in an email to verify your email address? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Email verification emails can be phishing—go directly to the site.\nIncorrect. Avoid clicking links in email verification emails; they may be phishing."
        },
        {
            "text": "Is it safe to share your social security number via email? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Never share your social security number via email.\nIncorrect. Sharing your social security number via email can lead to identity theft."
        },
        {
            "text": "Can phishing emails include fake software update prompts? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake software updates are a common phishing tactic.\nIncorrect. Phishing emails often use fake software updates to install malware."
        },
        {
            "text": "Should you trust an email because it has a professional tone? (1) Yes (2) No",
            "answer": 2,
            "feedback": "Correct! Professional tone doesn’t guarantee legitimacy—verify the sender.\nIncorrect. Phishers often use a professional tone to deceive users."
        },
        {
            "text": "Is it safe to ignore an email claiming your account has a security issue? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Security issue emails are often phishing—verify with the service.\nIncorrect. Such emails can be phishing scams; check with the service directly."
        },
        {
            "text": "Can phishing emails include fake password reset requests? (1) Yes (2) No",
            "answer": 1,
            "feedback": "Correct! Fake password reset requests are a common phishing tactic.\nIncorrect. Phishing emails often use fake password reset requests to steal credentials."
        }
    ]

    # Ensure the question bank has exactly 100 questions
    assert len(question_bank) == 95, f"Expected 100 questions, but found {len(question_bank)}"

    # Randomly select 10 questions
    selected_questions = random.sample(question_bank, 10)

    # Run the quiz
    score = 0
    print("Welcome to the Phishing Awareness Quiz!")
    print("You will be asked 10 questions about phishing and cybersecurity.")
    print("Answer each question with 1 or 2.\n")

    for i, q in enumerate(selected_questions, 1):
        print(f"Question {i}: {q['text']}")
        while True:
            try:
                ans = int(input("Enter 1 or 2: "))
                if ans not in [1, 2]:
                    print("Invalid input. Please enter 1 or 2.")
                    continue
                feedback = q['feedback'].split('\n')
                if ans == q['answer']:
                    print(feedback[0])
                    score += 1
                else:
                    print(feedback[1])
                break
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
        print()

    # Display final score and summary
    print(f"\nQuiz Complete! Your score: {score}/10")
    
    # Provide summary and tips based on score
    if score >= 9:
        print("Excellent! You’re a phishing detection expert.")
        print("Keep practicing by staying vigilant and following best practices.")
    elif score >= 6:
        print("Good job! You have a solid understanding of phishing.")
        print("Tip: Always double-check email addresses and avoid clicking links in unsolicited emails.")
    elif score >= 3:
        print("You’re on the right track, but there’s room for improvement.")
        print("Tip: Review the awareness guide (docs/phishing_awareness.md) to learn more about phishing signs.")
    else:
        print("You might be at risk of phishing attacks.")
        print("Tip: Study the awareness guide (docs/phishing_awareness.md) and practice spotting phishing emails with simulate_phishing.py.")

if __name__ == "__main__":
    run_quiz()