import random

def simulate_phishing():
    # List of simulated phishing emails
    phishing_simulations = [
        {
            "email": """
Subject: Urgent: IT Support - Password Reset Required
From: it.support@yourcompnay.com

Dear Employee,

We’ve detected a security issue with your account. To resolve this, please reset your password immediately by clicking the link below:

http://yourcompnay-security.com/reset

Failure to reset within 24 hours will result in account suspension.

Regards,
IT Support Team
""",
            "red_flags": [
                "Misspelled domain in the sender’s email ('yourcompnay.com' instead of 'yourcompany.com').",
                "Suspicious link ('yourcompnay-security.com' is not the official company domain).",
                "Urgent language ('reset within 24 hours' and 'account suspension') to pressure you.",
                "Generic greeting ('Dear Employee') instead of your name."
            ]
        },
        {
            "email": """
Subject: Action Required: Update Your Payroll Information
From: hr@yourcompany.com

Dear Team Member,

We’re updating our payroll system. Please click the link below to confirm your details by end of day:

http://payroll-update.net/confirm

Failure to update will delay your next paycheck.

Best,
HR Department
""",
            "red_flags": [
                "Suspicious link ('payroll-update.net' isn’t your company’s official domain).",
                "Urgent deadline ('by end of day') to create pressure.",
                "Generic greeting ('Dear Team Member') instead of your name.",
                "Threat of delayed payment to incite panic."
            ]
        },
        {
            "email": """
Subject: Quick Request - Need Project Files
From: john.doe@yourcompany.com

Hey [Your Name],

I’m in a meeting and need the Q3 project files ASAP. Please upload them here:

http://fileshare-secure.com/upload

Thanks,
John
""",
            "red_flags": [
                "Unusual request from a colleague—always verify such requests.",
                "Suspicious link ('fileshare-secure.com' is not a company-approved domain).",
                "Urgent language ('ASAP') to pressure you into acting quickly.",
                "Check the email address for slight variations (e.g., 'john.doe@yourcompnay.com')."
            ]
        },
        {
            "email": """
Subject: Security Alert: Verify Your Account Now
From: security@yourcompany.com

Dear Employee,

We’ve detected unusual activity on your account. Verify your identity by clicking the link below:

http://yourcompany-secure-login.com/verify

Failure to verify will lock your account.

Regards,
Security Team
""",
            "red_flags": [
                "Suspicious link ('yourcompany-secure-login.com' isn’t the official domain).",
                "Urgent language ('verify now' and 'lock your account') to create panic.",
                "Generic greeting ('Dear Employee') instead of your name.",
                "Unusual security alert—verify with IT directly."
            ]
        },
        {
            "email": """
Subject: Invoice Due: Immediate Payment Required
From: billing@yourcompany.com

Dear Employee,

You have an outstanding invoice due today. Please pay immediately by clicking the link below:

http://billing-portal.net/pay

Failure to pay will result in penalties.

Best,
Billing Department
""",
            "red_flags": [
                "Suspicious link ('billing-portal.net' isn’t the company’s domain).",
                "Urgent language ('due today' and 'immediate payment') to pressure you.",
                "Generic greeting ('Dear Employee') instead of your name.",
                "Unexpected invoice—verify with the billing department directly."
            ]
        }
    ]

    # Randomly select one simulated email
    simulation = random.choice(phishing_simulations)

    # Display the simulation
    print("--- Simulated Phishing Email ---")
    print("Below is a simulated email. Can you spot the phishing signs?\n")
    print(simulation["email"])
    print("--- End of Simulated Email ---\n")

    # Display the red flags
    print("Red Flags Identified:")
    for i, flag in enumerate(simulation["red_flags"], 1):
        print(f"{i}. {flag}")

    # Provide next steps
    print("\nWhat to Do Next:")
    print("- If you spotted these red flags, great job! Test your skills further with the quiz:")
    print("  python src/phishing_quiz.py")
    print("- If you missed some red flags, review the awareness guide for more tips:")
    print("  Open docs/phishing_awareness.md")
    print("- Practice more by running this simulation again to see a different email.")

if __name__ == "__main__":
    simulate_phishing()