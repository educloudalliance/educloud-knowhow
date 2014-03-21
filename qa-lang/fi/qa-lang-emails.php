<?php
/*
	Swedish Translation for Question2Answer 1.6.1 http://www.question2answer.org/
	
	(c) 2013, Anders Hellman
	Please submit any translation improvements or comments via:
	http://www.vilkenapp.se/feedback	
	or
	ziah75 (at) gmail dot com
	
	File: sv/qa-lang-emails.php
	Version: 1.1
	Date: 2013-07-15
	Description: Language phrases for email notifications

	This program is free software; you can redistribute it and/or
	modify it under the terms of the GNU General Public License
	as published by the Free Software Foundation; either version 2
	of the License, or (at your option) any later version.
	
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	More about this license: http://www.question2answer.org/license.php
*/

	return array(

		'a_commented_body' => "Ditt svar på ^site_title har en ny kommentar skriven av ^c_handle:\n\n^open^c_content^close\n\nDitt svar:\n\n^open^c_context^close\n\nDu kan svara genom att skriva en egen kommentar:\n\n^url\n\nMvh\n\n^site_title",
		'a_commented_subject' => 'Ditt svar på ^site_title har en ny kommentar',
		'a_followed_body' => "Ditt svar på ^site_title har en ny relaterad fråga skriven av ^q_handle:\n\n^open^q_title^close\n\nDitt svar:\n\n^open^a_content^close\n\nKlicka nedan för att besvara den nya frågan:\n\n^url\n\nMvh\n\n^site_title",
		'a_followed_subject' => 'Ditt svar på ^site_title har en ny relaterad fråga',
		'a_selected_body' => "Grattis! Ditt svar på ^site_title har blivit utvalt som det bästa av ^s_handle:\n\n^open^a_content^close\n\nFrågan:\n\n^open^q_title^close\n\nKlicka nedan för att läsa ditt svar:\n\n^url\n\nMvh\n\n^site_title",
		'a_selected_subject' => 'Utvalt svar på ^site_title',
		'c_commented_body' => "En ny kommentar har skrivits av ^c_handle efter din kommentar på ^site_title:\n\n^open^c_content^close\n\nDiskussionen:\n\n^open^c_context^close\n\nDu kan svara genom att skriva en till kommentar:\n\n^url\n\nMvh\n\n^site_title",
		'c_commented_subject' => 'Ny kommentar till inlägg som du kommenterat, på ^site_title ',
		'confirm_body' => "Vänligen klicka nedan för att bekräfta din email adress för ^site_title.\n\n^url\n\nMvh\n^site_title",
		'confirm_subject' => '^site_title - Email adress bekräftelse',
		'feedback_body' => "Kommentarer:\n^message\n\nNamn:\n^name\n\nEmail:\n^email\n\nFöregående sida:\n^previous\n\nAnvändare:\n^url\n\nIP-address:\n^ip\n\nWebbläsare:\n^browser",
		'feedback_subject' => '^ feedback',
		'new_password_body' => "Ditt nya lösenord till ^site_title finns nedan.\n\nLösenord: ^password\n\nVi rekommenderar att du byter ditt lösenord när du har loggat in.\n\nMvh\n^site_title\n^url",
		'new_password_subject' => '^site_title - Ditt nya lösenord',
		'q_answered_body' => "Din fråga på ^site_title har besvarats av ^a_handle:\n\n^open^a_content^close\n\nDin fråga:\n\n^open^q_title^close\n\nOm du gillar svaret, så kan du välja ut det som det bästa:\n\n^url\n\nMvh\n\n^site_title",
		'q_answered_subject' => 'Din fråga på ^site_title har besvarats',
		'q_commented_body' => "Din fråga på ^site_title har en ny kommentar skriven av ^c_handle:\n\n^open^c_content^close\n\nDin fråga:\n\n^open^c_context^close\n\nDu kan svara genom att skriva en egen kommentar:\n\n^url\n\nMvh\n\n^site_title",
		'q_commented_subject' => 'Din fråga på ^site_title har en ny kommentar',
		'q_posted_body' => "En ny fråga har ställts av ^q_handle:\n\n^open^q_title\n\n^q_content^close\n\nKlicka nedan för att läsa frågan:\n\n^url\n\nMvh\n\n^site_title",
		'q_posted_subject' => 'Ny fråga på ^site_title',
		'reset_body' => "Vänligen klicka nedan för att återställa ditt lösenord på ^site_title.\n\n^url\n\nEller så kan du skriva in koden nedan i fältet.\n\nKod: ^code\n\nOm du inte har bett om återställning av lösenordet, vänligen bortse från detta meddelande.\n\nMvh\n^site_title",
		'reset_subject' => '^site_title - Återställning av glömt lösenord',
		'welcome_body' => "Tack för att du registrerat dig på ^site_title.\n\n^custom^confirmDina inloggningsuppgifter är enligt följande:\n\nEmail: ^email\nLösenord: ^password\n\nSpara denna information på en säker plats, oåtkomlig för andra.\n\nMvh\n\n^site_title\n^url",
		'welcome_confirm' => "Vänligen klicka nedan för att bekräfta din email adress.\n\n^url\n\n",
		'welcome_subject' => 'Välkommen till ^site_title!',
		//Additions for 1.5 below
		//1.6.1 changed format here
		'flagged_body' => "Ett inlägg från ^p_handle har fått ^flags:\n\n^open^p_context^close\n\nKlicka nedan för att läsa inlägget:\n\n^url\n\n\nKlicka nedan för att granska alla flaggade inlägg:\n\n^a_url\n\n\nTack,\n\n^site_title",
		'flagged_subject' => "^site_title har ett skräprapporterat inlägg",
		'moderate_body' => "Ett inlägg från ^p_handle väntar på ditt godkännande:\n\n^open^p_context^close\n\nKlicka nedan för att godkänna eller underkänna inlägget:\n\n^url\n\nTack,\n\n^site_title",
		//1.6.1 changed format here
		'moderate_body' => "Ett inlägg från ^p_handle väntar på ditt godkännande:\n\n^open^p_context^close\n\nKlicka nedan för att godkänna eller underkänna inlägget::\n\n^url\n\n\nKlicka nedan för att granska alla inlägg i granskningskön:\n\n^a_url\n\n\nTack,\n\n^site_title",
		'moderate_subject' => "^site_title moderering",
		'private_message_body' => "Du har fått ett privat meddelande från ^f_handle på ^site_title:\n\n^open^message^close\n\n^moreTack,\n\n^site_title\n\n\nFör att stänga av privata meddelanden, surfa till dina kontoinställningar:\n^a_url",
		'private_message_info' => "Mer information om ^f_handle:\n\n^url\n\n",
		'private_message_reply' => "Klicka nedan för att svara ^f_handle via privat meddelande:\n\n^url\n\n",
		'private_message_subject' => "Meddelande från ^f_handle på ^site_title",
		'to_handle_prefix' => "^,\n\n",
		//Additions from 1.6.1
		'remoderate_body' => "Ett ändrat inlägg av ^p_handle kräver ditt godkännande:\n\n^open^p_context^close\n\nKlicka nedan för att godkänna eller dölja det ändrade inlägget:\n\n^url\n\n\nKlicka nedan för att granska alla inlägg i kön:\n\n^a_url\n\n\nTack,\n\n^site_title",
		'remoderate_subject' => "^site_title moderering",
		'u_registered_body' => "En ny användare har registrerat sig som ^u_handle.\n\nKlicka nedan för att visa användarens profil:\n\n^url\n\nTack,\n\n^site_title",
		'u_to_approve_body' => "En ny användare har registrerat sig som ^u_handle.\n\nKlicka nedan för att godkänna användaren:\n\n^url\n\nKlicka nedan för att granska alla användare som väntar på godkännande:\n\n^a_url\n\nTack,\n\n^site_title",
		'u_registered_subject' => "^site_title har en ny registrerad användare",
		'u_approved_body' => "Du kan se din nya användarprofil här:\n\n^url\n\nTack,\n\n^site_title",
		'u_approved_subject' => "Din ^site_title användare har godkänts",
		'wall_post_subject' => "Inlägg på din ^site_title vägg",
		'wall_post_body' => "^f_handle har skrivit på din vägg på ^site_title:\n\n^open^post^close\n\nDu kan svara på inlägget här:\n\n^url\n\nTack,\n\n^site_title",
	);
	
/*

	Omit PHP closing tag to help avoid accidental output
	
*/
