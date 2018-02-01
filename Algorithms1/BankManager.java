

public class BankManager {
	String account;
	double balance;
	double limit = 1000;
	public static void main(String [] args) {
		CheckingAccount checkingAccount = new CheckingAccount();
		SavingsAccount savingsAccount = new SavingsAccount();
		COD cod = new COD();
		System.out.println(checkingAccount.limit + "\t" + checkingAccount.account + "\t" + checkingAccount.balance);
		System.out.println(savingsAccount.transfers + "\t" + savingsAccount.account + "\t" + savingsAccount.balance);
		System.out.println(cod.expires + "\t" + cod.account + "\t" + cod.balance);
	}
}

class CheckingAccount extends BankManager {
	//double limit;
	public CheckingAccount(){
		this.limit = 1200;
		account = "ABCD12345HGS";
		balance = 1100;
	}
}

class SavingsAccount extends BankManager{
	double transfers;
	public SavingsAccount(){
		transfers = 1000;
		account = "1234553387686";
		balance = 5000;
	}
}

class COD extends BankManager {
	String expires;
	public COD(){
		expires = "01-01-2019";
		account = "FFYFYF87878787";
		balance = 2000;
	}
}
