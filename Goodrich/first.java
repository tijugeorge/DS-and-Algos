//Code Fragment 1.2:
public class Counter { 2 private int count; // a simple integer instance variable
 public Counter( ) { } // default constructor (count is 0)
 public Counter(int initial) { count = initial; } // an alternate constructor
 public int getCount( ) { return count; } // an accessor method
 public void increment( ) { count++; } // an update method
 public void increment(int delta) { count += delta; } // an update method
 public void reset( ) { count = 0; } // an update method
 }


//Code Fragment 1.3:
public class CounterDemo { 2 public static void main(String[ ] args) { 3 Counter c; // declares a variable; no counter yet constructed
 c = new Counter( ); // constructs a counter; assigns its reference to c
 c.increment( ); // increases its value by one
 c.increment(3); // increases its value by three more
 int temp = c.getCount( ); // will be 4
 c.reset( ); // value becomes 0
 Counter d = new Counter(5);// declares and constructs a counter having value 5
 d.increment( ); // value becomes 6
 Counter e = d; // assigns e to reference the same object as d
 temp = e.getCount( ); // will be 6 (as e and d reference the same counter)
 e.increment(2); // value of e (also known as d) becomes 8
 } }

