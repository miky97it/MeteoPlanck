package network.test;
import java.io.IOException;
import java.util.List;

import purejavahidapi.*;
public class USBTests {

	public static void main(String[] args) {
	System.out.println("Device List:");
		List<HidDeviceInfo> devList = PureJavaHidApi.enumerateDevices();
		int cont=0;
		for (HidDeviceInfo info : devList) {
			System.out.printf("[%d] VID = 0x%04X PID = 0x%04X Manufacturer = %s Product = %s Path = %s\n", //
				cont++,
				info.getVendorId(), //
				info.getProductId(), //
				info.getManufacturerString(), //
				info.getProductString(), //
				info.getPath());
			HidDevice dev = null;
			try {
				dev = PureJavaHidApi.openDevice(info);
				dev.setInputReportListener(new InputReportListener() {
					@Override
					public void onInputReport(HidDevice source, byte Id, byte[] data, int len) {
						System.out.printf("onInputReport: id %d len %d data ", Id, len);
						for (int i = 0; i < len; i++)
							System.out.printf("%02X ", data[i]);
						System.out.println();
						}
					});
			} catch (IOException e) {
				// TODO Auto-generated catch block
				System.err.println("Problems to open the device with PureJavaHidApi");
				e.printStackTrace();
			}
		}
	}
}
