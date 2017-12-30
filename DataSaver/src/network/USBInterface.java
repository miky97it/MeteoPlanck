package network;

import model.Data;

/**This Class permits to create a data stream from USB 
	 * <a href="https://github.com/nyholku/purejavahidapi"> inspired to</a>*/
public class USBInterface {
	Data data;
	public Data getData(bolean debug){
		data=new data(/*add here the USB listener*/);
		return data;
	}
}
