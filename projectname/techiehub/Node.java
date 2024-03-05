import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "AC221ca32b1a5350b9823cb32ceb6cecd6";
    public static final String AUTH_TOKEN = "239ebf18d85aa398dc3aa100704ea148";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);

        // Corrected the placement of create() method and its associated closing parenthesis
        Message message = Message.creator(
                new PhoneNumber("whatsapp:+919791126625"),
                new PhoneNumber("whatsapp:+14155238886"),
                "TEST"
        ).create();

        System.out.println(message.getSid());
    }
}
