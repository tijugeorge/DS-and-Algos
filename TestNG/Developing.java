package InterfaceConcept;

public class Developing implements BankingClient {

	public static void main(String[] args){
		Developing d = new Developing();

		d.paycreditcard();
		d.transferbalance();
	}

	@Override
	public void paycreditcard() {
		System.out.println("paycredit implemented");
	}

	@Override
	public void transferbalance() {
		System.out.println("transfer balance implemented");
	}

	@Override
	public void checkingbalance(){
		System.out.println("checking balance implemented");
	}
}
