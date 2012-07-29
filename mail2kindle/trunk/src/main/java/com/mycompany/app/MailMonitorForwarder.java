package com.mycompany.app;

import java.io.IOException;
import java.util.Properties;

import javax.mail.Flags;
import javax.mail.Message;
import javax.mail.MessagingException;


public class MailMonitorForwarder {
	
	private String monitoredAccountName = null;
	private String monitoredAccountPassoword = null;
	private Properties monitoredAccountProperties = null;
	private String recipientAccount = null;
	private Message[] emailsToForward = null;
	private MailerTools mailerTools = null;
	
	public static void main(String[] args) {		
		MailMonitorForwarder mailForwarder = new MailMonitorForwarder();
		mailForwarder.forwardEmails();
	}
	
	public void forwardEmails() {
		this.mailerTools = new MailerTools();
		this.setupMonitoredAccount();
		this.setupRecipientAccount();
		this.fetchAllMailsFromMonitoredAccount();
		this.forwardAllMailsToRecipientAccount();
		/*this.deleteAllMailFromMonitoredAccount();*/		
	}
	
	public void setupMonitoredAccount() {
		this.monitoredAccountProperties = new Properties();
		this.monitoredAccountProperties.put("mail.smtp.auth", "true");
		this.monitoredAccountProperties.put("mail.smtp.starttls.enable", "true");
		this.monitoredAccountProperties.put("mail.smtp.host", "smtp.gmail.com");
		this.monitoredAccountProperties.put("mail.smtp.port", "587");
		this.monitoredAccountName = "studenttest0003@gmail.com";		
		this.monitoredAccountPassoword = "studenttest";
		this.mailerTools.connect(this.monitoredAccountName, this.monitoredAccountPassoword, this.monitoredAccountProperties);
	}
	
	public void setupRecipientAccount() {
		this.recipientAccount = "studenttest0002@gmail.com";
	}
	
	public void fetchAllMailsFromMonitoredAccount() {
		this.emailsToForward = this.mailerTools.readMailFolder("INBOX", this.monitoredAccountName, this.monitoredAccountPassoword);		
	}
	
	public void forwardAllMailsToRecipientAccount() {
		String forwardedMailConent = null;
		String forwardedMailSubject = null;
		for(Message message: this.emailsToForward) {
			try {
				forwardedMailSubject = message.getSubject();
				forwardedMailConent = this.mailerTools.findConent(message, "text/html");	
				this.mailerTools.sendSimpleMailWithHtmlAttachment(this.monitoredAccountName, this.recipientAccount, forwardedMailSubject, forwardedMailConent);
			} catch (MessagingException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}  			
		}
	}
	
	public void deleteAllMailFromMonitoredAccount() {
		for(Message message: this.emailsToForward) {
			try {
				message.setFlag(Flags.Flag.DELETED, true);
			} catch (MessagingException e) {
				e.printStackTrace();
			}
		}
	}	
}
