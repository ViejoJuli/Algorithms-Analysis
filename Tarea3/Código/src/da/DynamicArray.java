//Tarea 3: Dynamic Array
package da;
import java.time.Clock;
import java.util.Arrays;

public class DynamicArray {

	private int size=0;
	private int[] numbers=new int[0];
	private double increaseFactor;
	
	public DynamicArray(double factor) {
		increaseFactor = factor;
	}
	
	
	public void add(int number) {
		if(size<numbers.length) {
			numbers[size]=number;
			size++;
		}else{
			int newC = (int)Math.ceil((numbers.length+0.0000001)*increaseFactor);
			numbers = Arrays.copyOf(numbers, newC);
		}
	}
	
	public void StressCharge(int stress) {
		Clock clock = Clock.systemDefaultZone();
		long m1=clock.millis();
		for (int i = 0; i < stress; i++) {
			add((int) Math.random()*5);
		}
		long m2=clock.millis();
		long time = m2 - m1;
		System.out.println("Time elapsed: "+time+ " ms");
	}
	
	public static void main(String[] args) {
		
		int [] stress = {100000000};
		double[] factors = {2, 1.5, 1.01};
		for (int i = 0; i < factors.length; i++) {
			for (int j = 0; j < stress.length; j++) {
				System.out.println("For Increase factor "+factors[i]+ " and charge "+stress[j]+":");
				try {
					DynamicArray da = new DynamicArray(factors[i]);
					da.StressCharge(stress[j]);
				}catch(OutOfMemoryError oome) {
					System.out.println("Heap Exceeded, please increase memory to test case");
				}
			}
		}
		

	}
	
}
