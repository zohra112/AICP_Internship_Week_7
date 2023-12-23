#Internship Task 7, Charity Donation system 

class Charity:
    def __init__(self, name, total):
        self.name = name
        self.total = total


def display_charities(charities):
    print(f"{'Charity Number':<25}{'Charity Name':<25}")
    for i, charity in enumerate(charities, start=1):
        print(f"{i:<25}{charity.name:<25}")


def display_totals(charities):
    print("\nCharity Totals (Descending Order):\n")
    print(f"{'Charity Name':<25}{'Total Donated':<25}")

    # Sort charities based on total donation in descending order
    sorted_charities = sorted(charities, key=lambda x: x.total, reverse=True)
    for charity in sorted_charities:
        print(f"{charity.name:<25}{'$':<25}{charity.total:.2f}")


def main():
    # Initialize Charity objects
    charities = [Charity("Charity 1", 0.0), Charity("Charity 2", 0.0), Charity("Charity 3", 0.0)]
    shopping_bill, donation, choice = 0.0, 0.0, 0
    grand_total = 0.0

    print("Welcome to the Charity Donation System!\n")

    # Collect names for each charity
    for charity in charities:
        charity.name = input(f"Enter the name of {charity.name}: ")

    while True:
        print()
        display_charities(charities)

        # User input for charity choice
        choice = int(input("\nEnter your choice (1, 2, 3) or -1 to show totals: "))

        if choice == -1:
            print()
            display_totals(charities)

            # Calculate grand total and donation from total
            grand_total = sum(charity.total for charity in charities)
            donation_from_total = 0.01 * grand_total

            print(f"\nGRAND TOTAL DONATED TO CHARITIES: ${grand_total:.2f}")
            print(
                f"Your donation also contributes to the grand total. From the total amount, ${donation_from_total:.2f} will be donated to all charities collectively.\n")

            break

        # Validate and process user choice
        if not 1 <= choice <= 3:
            print("Invalid choice. Please choose 1, 2, 3, or -1 to show totals.\n")
            continue

        # Collect user shopping bill and calculate donation
        shopping_bill = float(input("Enter your shopping bill amount: $"))
        donation = 0.01 * shopping_bill

        # Update charity total donation
        charities[choice - 1].total += donation

        print(f"\nThank you for your donation of ${donation:.2f} to {charities[choice - 1].name}.\n")


if __name__ == "__main__":
    main()
#Code by zohra Batool
