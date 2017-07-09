class Movie {
  String title;
  String genre;
  int rating;
  
  void playIt(){
    System.out.println("Playing the Movie "+ title + " of genre as " + genre + ". It got the rating of "+ rating);
  }
}

public class Main{
  public static void main(String[] args){
    Movie one = new Movie();
    one.title = "Gone with the Stock";
    one.genre = "Tragic";
    one.rating = 2;
    one.playIt();
    Movie two = new Movie();
    two.title = "Lost in Cubicle space";
    two.genre = "Comedy";
    two.rating = 5;
    two.playIt();
    Movie three = new Movie();
    three.title = "Byte Club";
    three.genre = "Tragic but ultimately lifting";
    three.rating = 127;
    three.playIt();
  }
}
