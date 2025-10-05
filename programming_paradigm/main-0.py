import sys
from bank_account import BankAccount

def _format_amount(amount):
    """Same formatting logic as in BankAccount to match expected output."""
    try:
        a = float(amount)
    except (TypeError, ValueError):
        return str(amount)
    return str(int(a)) if a.is_integer() else f"{a:.2f}"

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]
    parts = command_input.split(':')
    command = parts[0]
    amount = float(parts[1]) if len(parts) > 1 and parts[1] != "" else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${_format_amount(amount)}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${_format_amount(amount)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
