package control;

import network.USBInterface;
	/**
	 *1 debug 
	 */
public class main {
	USBInterface USBI;
	boolean debug=true;//false;
	public void main(String[] args) {
	if (args[1].compareTo("1")==0) {
		debug=true;
	}
	USBI=new USBInterface();
	while(true){
		if (debug) {
			
		}
		data=USBI.getData;//this wait data
	}
	//add a external script that if this process isn't running restart the raspberry
	}

}
