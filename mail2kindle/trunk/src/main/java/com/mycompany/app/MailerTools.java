package com.mycompany.app;
 
import java.io.IOException;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import java.util.logging.Logger;
import java.util.regex.Pattern;

import javax.mail.Authenticator;
import javax.mail.BodyPart;
import javax.mail.Folder;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Multipart;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Store;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;



public class MailerTools {
	
	Properties props = new Properties();
	Session session = null;
	final static Logger log = Logger.getLogger(MailerTools.class .getName());

	public void setUp() {
 		props.put("mail.smtp.auth", "true");
		props.put("mail.smtp.starttls.enable", "true");
		props.put("mail.smtp.host", "smtp.gmail.com");
		props.put("mail.smtp.port", "587");
	}
	

	private class MyPopupAuthenticator extends Authenticator {
		public PasswordAuthentication getPasswordAuthentication(String username, String password) {
			return new PasswordAuthentication(username, password);
		}	
	}
	
	public void connect(String username, String password, Properties props) {
		Authenticator passwordAuthentication = new MyPopupAuthenticator();
		this.session = Session.getInstance(props, passwordAuthentication);
	}
	
	public void sendSimpleMailWithHtmlAttachment(String senderAddress, String recipientAddress, 
				String attachmentSubject, String dataLoad) throws MessagingException {
			try {
				String subject = "Mail from kindle mail forwarder at " + new Date();
				MimeMessage message = 
			      new MimeMessage(session);
			    message.setFrom(
			      new InternetAddress(senderAddress));
			    message.addRecipient(
			      Message.RecipientType.TO, 
			      new InternetAddress(recipientAddress));
			    message.setSubject(subject);
			    // Email main block
			    Multipart multipart = new MimeMultipart();
			    // Part one is the message 
			    MimeBodyPart messageBodyPartMain = new MimeBodyPart();
			    // Fill message
			    messageBodyPartMain.setText(subject);
			    // Add part One
			    multipart.addBodyPart(messageBodyPartMain);

			    // Part two is attachment			    
			    MimeBodyPart attachmentElement = new MimeBodyPart();
			    attachmentElement.setContent(dataLoad, "text/html");
			    attachmentElement.setFileName(attachmentSubject + ".html");
			    // Add part Two
			    multipart.addBodyPart(attachmentElement);			    
			    // Put parts in message
			    message.setContent(multipart);
			    // Send the message
			    Transport.send(message);
			} catch (MessagingException e) {
				log.severe("Mail with attachment can't be sent, " + e.getClass().getName() + ": " + e.getMessage());
				throw e;
			}
	}
	public Message[] readMailFolder(String folderName, String userName, String password) {
		try {		
			Store store = this.session.getStore("imaps");
			store.connect("imap.gmail.com", userName, password);
			Folder folder = store.getFolder(folderName);
			folder.open(Folder.READ_WRITE);
			Message[] messages = folder.getMessages();
			log.info("Number of messages: " + messages.length);
			
			for(int i = 0; i < messages.length; i++) {
				Message message = messages[i];
				log.info("["+i+"]" + " :" + message.getSubject());
			}
			
			// log.info("Subject of last mail: " + message[message.length - 1].getSubject());
			return messages;
		} catch (MessagingException e) {
			throw new RuntimeException(e);
		}
	}
	
	// "text/html"
	public String findConent(Message message, String searchedContentType) throws MessagingException, IOException  {
		Object content = message.getContent();
		log.info("Message type: " + content.getClass().getName());
		if (content instanceof Multipart) {
		    Multipart mp = (Multipart) content;
		    for (int i = 0; i < mp.getCount(); i++) {
		        BodyPart bp = mp.getBodyPart(i);
		        if (Pattern
		                .compile(Pattern.quote(searchedContentType),
		                        Pattern.CASE_INSENSITIVE)
		                .matcher(bp.getContentType()).find()) {
		            return (String) bp.getContent();
		        }
		    }
		} else if(content instanceof String) {
			return (String) content;
		}
		return null;
	}
	
	public Map<Integer, String[]> parseEmail(Message message) throws MessagingException, IOException {
		Map<Integer, String[]> emailParsed = new HashMap<Integer, String[]>();
		Object content = message.getContent();
		String contentType = message.getContentType();
		log.info(contentType + ": " + message.getSubject());
		if (content instanceof Multipart) {
		    Multipart mp = (Multipart) content;
		    for (int i = 0; i < mp.getCount(); i++) {
		        BodyPart bp = mp.getBodyPart(i);
		        log.info(bp.getContentType() + " : " + bp.getContent());
		        String[] array = {bp.getContentType(), (String) bp.getContent()};
		        emailParsed.put(i,array);
		    }
		}
		return emailParsed;
	}
}

/*public static void main2(String[] args) {

final String username = "abednarski79@gmail.com";
final String password = "2be34ever";

Properties props = new Properties();
props.put("mail.smtp.auth", "true");
props.put("mail.smtp.starttls.enable", "true");
props.put("mail.smtp.host", "smtp.gmail.com");
props.put("mail.smtp.port", "587");

Session session = Session.getInstance(props,
  new javax.mail.Authenticator() {
	protected PasswordAuthentication getPasswordAuthentication() {
		return new PasswordAuthentication(username, password);
	}
  });

try {

	Message message = new MimeMessage(session);
	message.setFrom(new InternetAddress("abednarski79@gmail.com"));
	message.setRecipients(Message.RecipientType.TO,
		InternetAddress.parse("abednarski79@gmail.com"));
	message.setSubject("Testing Subject");
	message.setText("Dear Mail Crawler,"
		+ "\n\n No spam to my email, please!");

	Transport.send(message);

	System.out.println("Done");

} catch (MessagingException e) {
	throw new RuntimeException(e);
}
}*/


/*public void sendSimpleMail() {
try {
	 
	Message message = new MimeMessage(this.session);
	message.setFrom(new InternetAddress("abednarski79@gmail.com"));
	message.setRecipients(Message.RecipientType.TO,
		InternetAddress.parse("abednarski79@gmail.com"));
	message.setSubject("Testing Subject");
	message.setText("Dear Mail Crawler,"
		+ "\n\n No spam to my email, please!");

	Transport.send(message);

	System.out.println("Done");

} catch (MessagingException e) {
	throw new RuntimeException(e);
}
}*/

/*public void sendHtmlMail(String subject, String body) {
try {			
	Message message = new MimeMessage(this.session);
	message.setFrom(new InternetAddress("abednarski79@gmail.com"));
	message.setRecipients(Message.RecipientType.TO,
		InternetAddress.parse("abednarski79@kindle.com"));
	message.setSubject(subject);
	message.setText(body);
	Transport.send(message); 
} catch (MessagingException e) {
	throw new RuntimeException(e);
}		
}*/