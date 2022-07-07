package section01;

public class Notebook extends Computer {


	public double screenSize;
	public double weight;
	
	// Alt + Shift + S 로 Constructor 만들기
	public Notebook(String manufacturer, String processor, int ramSize, int diskSize, double processorSpeed,
			double screenSize, double weight) {
		super(manufacturer, processor, ramSize, diskSize, processorSpeed);
		this.screenSize = screenSize;
		this.weight = weight;
	}
	
	
	
	
	
	
}
