package simple;

import java.time.LocalDate;

public class second_problem {
	public static String getDay(String d,String y,String m)
	{
		int day= Integer.parseInt(d);
		int year=Integer.parseInt(y);
		int month=Integer.parseInt(m);
		LocalDate lt= LocalDate.of(year,month,day);
	
	}
	return lt.getDayOfWeek().name();

public static void main(String[] args){
	second_problem obj = new second_problem();
	
	
}}}