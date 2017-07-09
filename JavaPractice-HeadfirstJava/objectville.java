
class Dog {
  int size;
  String breed;
  String name;
  
  void bark() {
    System.out.println("Ruff! Ruff!");
  }
  void output() {
    System.out.println("The breed is "+ breed +" and the size of the dog is "+size);
  }
}

class Main {
  public static void main(String[] args){
    Dog d = new Dog();
    d.size = 40;
    d.breed = "Dalmatian";
    d.bark();
    d.output();
  }
}
