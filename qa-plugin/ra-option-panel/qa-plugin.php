<?php

/*
	Plugin Name: Ra Theme Options
	Plugin URI: http://rahularyan.com
	Plugin Description: RA theme option panel for customizing theme by RahulAryan
	Plugin Version: 3.0
	Plugin Date: 2013-10-9
	Plugin Author: Rahul Aryan
	Plugin Author URI: http://www.rahularyan.com/
	Plugin License: GPLv3
	Plugin Minimum Question2Answer Version: 1.5
	Plugin Update Check URI: 
*/


	if (!defined('QA_VERSION')) { // don't allow this page to be requested directly from browser
		header('Location: ../../');
		exit;
	}



	qa_register_plugin_module('module', 'ra-option-admin.php', 'ra_option_admin', 'ra_theme_option');
	qa_register_plugin_layer('ra-option-layer.php', 'RA Option Layer');
	
	


/*
	Omit PHP closing tag to help avoid accidental output
*/