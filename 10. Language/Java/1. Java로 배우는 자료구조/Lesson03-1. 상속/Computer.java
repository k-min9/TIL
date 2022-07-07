package section01;

public class Computer {

	public String manufacturer;
	public String processor;
	public int ramSize;
	public int diskSize;
	public double processorSpeed;
	
	public Computer(String manufacturer, String processor, int ramSize, int diskSize, double processorSpeed) {
		super();
		this.manufacturer = manufacturer;
		this.processor = processor;
		this.ramSize = ramSize;
		this.diskSize = diskSize;
		this.processorSpeed = processorSpeed;
	}
	
	public double computerPower() {
		return ramSize * processorSpeed;
	}
	
	// java 파일 선택 후 우클릭으로 getter/setter 제네레이트 가능
	public String getManufacturer() {
		return manufacturer;
	}

	public void setManufacturer(String manufacturer) {
		this.manufacturer = manufacturer;
	}

	public String getProcessor() {
		return processor;
	}

	public void setProcessor(String processor) {
		this.processor = processor;
	}

	public double getRamSize() {
		return ramSize;
	}

	public void setRamSize(int ramSize) {
		this.ramSize = ramSize;
	}

	public int getDiskSize() {
		return diskSize;
	}

	public void setDiskSize(int diskSize) {
		this.diskSize = diskSize;
	}

	public double getProcessorSpeed() {
		return processorSpeed;
	}

	public void setProcessorSpeed(double processorSpeed) {
		this.processorSpeed = processorSpeed;
	}
	
	
	
}
