package simple;

import java.util.Scanner;

public class First_java {
	public static void main(String args[])
	{
		Scanner sc =new Scanner(System.in);
		System.out.print("helllowewewewe");
		System.out.print("Plase enter the number:");
		int number=sc.nextInt();
		if(number%2==0)
		{
			if(number>2 & number<5)
			{
				System.out.print("Not Weired");
			}
			if(number>6 & number<20)
			{
				System.out.print("Weired");
			}
			if(number>20)
			{
				System.out.print("Not Werid");
			}
		}
		else
		{
			System.out.println("Werid");
			
		}
		
	}

}
