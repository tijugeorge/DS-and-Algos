/**
 * Created by tijum on 1/27/2018.
 */
class Contact {
    String name;
    String email;
    String phoneNumber;
}

class ContactsManager {
    //Fields or Instance variables
    Contact [] myFriends;
    int friendsCount;

    //Constructor default
    ContactsManager(){
        this.friendsCount = 0;
        this.myFriends = new Contact[500];
    }

    //methods
    void addContact(Contact contact) {
        myFriends[friendsCount] = contact;
        friendsCount++;
    }

    Contact searchContact(String searchName){
        for(int i = 0; i < friendsCount; i++){
            if(myFriends[i].name.equals(searchName)){
                return myFriends[i];
            }
        }
        return null;
    }
}

public class ContactBook {
    public static void main(String [] args){
        System.out.println("Hello World");
        // Create the ContactsManager object
        ContactsManager myContactsManager = new ContactsManager();
        // Create a new Contact object for George
        Contact friendGeorge = new Contact();
        //Set the fields or instance variables
        friendGeorge.name = "George";
        friendGeorge.phoneNumber = "0012223333";
        // Add George Contact to the ContactsManager
        myContactsManager.addContact(friendGeorge);
        // Create a new Contact object for Cezanne
        Contact friendCezanne = new Contact();
        //Set the fields or instance variables
        friendCezanne.name = "Cezanne";
        friendCezanne.phoneNumber = "987654321";
        //Add Cezanne Contact to the ContactsManager
        myContactsManager.addContact(friendCezanne);
        // Create a new Contact object for Jessica
        Contact friendJessica = new Contact();
        // Set the fields
        friendJessica.name = "Jessica";
        friendJessica.phoneNumber = "5554440001";
        // Add Jessica Contact to the ContactsManager
        myContactsManager.addContact(friendJessica);

        // Now let's try to search of a contact and display their phone number
        Contact result = myContactsManager.searchContact("Jessica");
        System.out.println(result.phoneNumber);
        System.out.println(result.email);
    }
}
