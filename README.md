# Ignition 8 Demo Projects - Version 5.0.0

This resource includes a zip file with the following files from our Ignition 8 Online Demo Project:

+ Gateway Backup 
+ Project Files
+ Tag Exports
+ Database Schemas
+ Translations
+ Images
+ CSS Themes

The Building Management System Demo can be downloaded here: https://inductiveautomation.com/exchange/2312

## Installation

### Custom Instructions
Welcome to the Ignition Demo Projects by Inductive Automation.

The purpose of these demo projects is to give you an idea of what can be configured in Ignition.

We want you to take these demos apart and use various pieces in your project.

It is also perfect for hosting your very own online demo project for Ignition.
 
The username/password for the Ignition Gateway Backup is:

Username: admin

Password: password
 
**Required Ignition Version:**

+ 
8.1.25 or higher


 
**Ignition Modules Used in Demos:**

+ 
OPC-UA

+ 
OPC Drivers

+ 
Perspective

+ 
Vision

+ 
Mobile

+ 
Reporting

+ 
SQL Bridge

+ 
Tag Historian

+ 
SFC

+ 
Alarm Notification

+ 
Web Browser

+ 
WebDev

+ 
MQTT Engine* (only necessary for MQTT specific features of the demo)


 
**Simulated Devices Used (Included with all Ignition Installs): **

+ 
Dairy: Dairy Demo

+ 
Generic: Generic

+ OilAndGasDailyData: Programmable Device Simulator (csv file included)
+ OilAndGasData: Programmable Device Simulator (csv file included)
+ Prepared Foods Line: Programmable Device Simulator (csv file included)
+ 
SLC: SLC

+ Sample_Device: Programmable Device Simulator (csv file included)
+ 
Simulator: Dairy Demo


 
**Included Files: **


+ 
Demo Images: Icons and other images used throughout the demo projects.

+ Programmable Device Simulators: CSV files of custom simulator function-driven values.
+ Project Backups: Project exports of Perspective and Vision projects.
+ Tags: JSON files of all Tags and UDTs used within the Online Demo project.
+ 
Themes: CSS files that can be copied into your Perspective themes directory to provide some enhancements specific to these demos.

+ 
Translations: XML files that can be imported into the Designer's Translation Manager to provide translations specific to these demos.

+ 
Ignition Demo VM Backup_Ignition-backup.gwbk: The Gateway backup that you can use to help preconfigure your Gateway to work on the demo projects.

+ all_databases.sql: SQL export to import into MySQL Workbench containing all schemes used in both projects.



**Within Project Backups Folder:**

+ 
global.zip: Global project file with settings that can be used across all projects associated with the Gateway.

+ 
OnlineDemo.zip: Perspective demo project export to be imported into your designer.

+ 
IADemo.zip: Vision demo project export to be imported into your designer.

+ 
TagDashboard.zip: IIoT demo project that can be imported into your designer.

+ samplequickstart.zip: Ignition Quick Start project that can be imported into your designer.

**Within Tags folder:**

+ 
PerspectiveDemoUDTTags.json: UDT tags from the Perspective demo project to import into the tag provider called default.

+ 
PerspectiveDemoTags.json: Tags from the Perspective demo project to import into the tag provider called default.

+ LocalTags.json: Tags from the Perspective demo project to import into the tag provider called local.
+ IIoTDemoTags.json: Tags from the IIoT Demo project to import into the tag provider called IIoT.
+ VisionProviderUDTTags.json: UDT tags from the Vision demo project to import into the tag provider called VisionProvider.


+ 
VisionProviderTags.json: Tags from the Vision demo project to import into the tag provider called VisionProvider.

+ QuickstartTags.json: Tags from the Quick Start demo project to import into the tag provider called Sample_Tags.

 
**Instructions to Install Both the Perspective and Vision Demos: **

+ 
Download and install Ignition 8.1.25 or higher. Make sure you install the required modules in the above &ldquo;Ignition Modules Used in Demos&rdquo; section otherwise certain features of the demo project will not work. During the installation process, make sure to select "Custom" during the Installation Options section and include Web Browser and WebDev modules. You can also download the modules from: https://inductiveautomation.com/downloads/ and install them on the Gateway.

+ 
Download and install MySQL 5.7.23 or higher. You can get it here: http://dev.mysql.com/downloads/mysql/

+ 
Import the file all_databases.sql in MySQL. Use MySQL Workbench and refer to MySQL user manual for further instructions.


+ 
NOTE: This will create the required schema, tables, and import all data into MySQL.


+ 
Restore the Ignition Demo VM Backup_Ignition-backup.gwbk in Ignition. **The Gateway credentials are admin/password. **

+ 
Fix the MySQL database connection in Ignition by changing the root password to yours. Log into the Ignition Gateway configuration page and select "Database &gt; Connections". Click "edit" next to each stored database connection. Click "Change Password" and enter in your MySQL's root password. Click "Save Changes" and the connection should be valid.

+ 
Restart Ignition (restart the Windows or Linux service). This is to make sure everything starts up correctly with the databases configured correctly now.


 
**Setting up the Designer:**

+ 
Download and run the Designer Launcher


+ 
The Designer Launcher can be found in the Gateway homepage


+ 
In the Designer Launcher add a new entry for your Gateway using the Add Designer button


 
**Finishing Installation:**

+ 
Inside the designer, under tools select image management and import the files inside /Project Backups/Demo Images/

+ 
Inside the Tag Browser expand the folder named All Providers:


+ 
Import the file PerspectiveDemoUDTTags.json into the tag provider named default

+ 
Import the file PerspectiveDemoTags.json into the tag provider named default

+ 
Import the file VisionProviderTags.json into the tag provider named VisionProvider


+ 
Inside the designer, open up the Translation Manager under the tab Tools &gt; Translation Manager and import the translation .xml files located at /Project Backups/Translations/


 
**Setting up the Vision Client Launcher:**

+ 
Download and run the Vision Client Launcher


+ 
The Vision Client Launcher can be found in the Gateway homepage


+ 
In the Vision Client Launcher add a new entry for your Vision projects using the Add Application(s) button


 
**How to Merge the Demos into an Existing Ignition Gateway:**


+ 
Launch the Designer for your Gateway from the Designer Launcher.

+ 
Create a new project or open an existing one.

+ Create the Device Simulators on the Gateway under Config &gt; OPC UA &gt; Device Connections:

+ "Dairy" using the simulator: Dairy Demo.
+ "Generic" using the simulator: Generic.
+ "OilAndGasDailyData" and import the file 'OilAndGasDailyData.csv'.
+ "OilAndGasData" and import the file 'OilAndGasData.csv'.
+ "Prepared Foods Line" and import the file 'Prepared Foods Line.csv'.
+ "SLC" using the simulator: SLC.
+ "Sample_Device" and import the file 'Sample_Device.csv'.
+ "Simulator" using the simulator: Dairy Demo.


+ 
Import the desired project(s) into your Designer:


+ Global Project: global.zip
+ 
Perspective Demo Project: OnlineDemo.zip

+ 
Vision Demo Project: IADemo.zip

+ 
IIoT Demo Project: TagDashboard.zip

+ Quick Start Project: samplequickstart.zip

+ 
Navigate to the Tag Browser and import the following files into the appropriate tag providers:


+ 
Perspective Demo Project: Import the file PerspectiveDemoUDTTags.json first and then PerspectiveDemoTags.json into the tag provider named default.

+ 
Vision Demo Project: Import the file VisionProviderUDTTags.json first and then VisionProviderTags.json into the tag provider named VisionProvider.

+ 
IIoT Demo Project: Import the file IIoTDemoTags into the tag provider named IIoT.

+ 
Quick Start Demo Project: Import the file QuickstartTags.json into the tag provider named Sample_Tags.


+ 
Inside the designer, under tools select Image Management and import the Images inside the Demo Images folder.

+ Inside the designer, under tools select Translation Manager and import the Translation files. 
+ 
Import the all_databases.sql file into your MySQL database.


+ 
NOTE: This will create the required schema, tables, and import all data into MySQL.

+ Create the MySQL database connections on your Gateway (Database Connection Name / Database for Connection URL):

+ Automotive / automotive
+ Demo / demo
+ IADemo / iademo
+ IIoT / iiot
+ OilSimData / oil
+ RFID / rfid
+ Sample_Database / quickstart
+ WaterSimData / water
+ telecom / telecom





### Common Instructions

**Gateway Backups (.gwbk)**  
Gateway backups are all inclusive and backup everything relating to an Ignition installation while Project exports are simply a backup of individual projects. Restoring a Gateway backup is just as easy as backing it up and can also be done from the Gateway Webpage.

When you perform a Gateway Restore, ALL of the server's current configuration will be permanently lost! Restoring a Gateway backup overwrites all of the existing settings including your projects. There is no merge option for a Gateway backup. We recommend you always make a backup of the existing server immediately before performing a Gateway Restore.
The Gateway restore is located in:
Ignition Gateway > Configuration > System >Backup/Restore > Restore Tab

**Project (.zip/.proj)**  
Project backup and restoring from a project backup is referred to as Project Export and Import. Projects are exported individually, and only include project-specific elements visible in the Project Browser in the Ignition Designer. They do not include Gateway resources, like database connections, Tag Providers, Tags, and images. The exported file (.zip or .proj) is used to restore / import a project.

.zip = Ignition 8+
.proj = Ignition 7+

There are two primary ways to export and import a project:

Gateway Webpage - exports and imports the entire project.
Designer -  exports and imports only those resources that are selected.

When you restore / import a project from an exported file in the Gateway Webpage, it will be merged into your existing Gateway.

The import is located in:
Ignition Gateway > Configuration > System > Projects > Import Project Link

If there is a naming collision, you have the option of renaming the project or overwriting the project. Project exports can also be restored / imported in the Designer. Once the Designer is opened you can choose File > Import from the menu. This will even allow you to select which parts of the project import you want to include and will merge them into the currently open project.

**Tags (.json/.xml/.csv)**  
Ignition can export and import Tag configurations to and from the JSON (JavaScript Object Notation) file format. You can import XML (Extensible Markup Language) or CSV (Comma Separated Value) file formats as well, but Ignition will convert them to JSON format. Tag exports are imported in the Designer. Once the Designer is opened you can click on the import button in the Tag Browser panel.

**Images (.png/.jpg/.gif)**  
Images such as PNGs, JPGs, or GIFs can be uploaded to the Image Management tool and used inside of windows in Ignition. Once uploaded, these images may be used on windows and in templates. The Image Manager tool, available from the Tools > Image Management in the Ignition Designer, provides an interface to upload, download, or select images.

**SQL Backups (.sql)**  
A SQL file is a backup of a SQL database, full or partial. Refer to your database provider on instructions to import. Typically, you open the SQL management tool or workbench, open the .sql backup, and run the queries against your database.

### Requirements

**Modules**

+ Alarm Notification
+ OPC UA Server
+ Reporting
+ SQL Bridge
+ Web Browser
+ Sequential Function Charts
+ Perspective
+ Web Development
+ Vision
+ Tag Historian

## Release Notes
Updated to Ignition 8.1.25 with new features

## Authors and Acknowledgment
Built for the [Ignition Exchange](https://inductiveautomation.com/exchange) by IA Sales Engineering

## Support
View [Ignition 8 Demo Projects](https://inductiveautomation.com/exchange/110) for more information, and other [versions](https://inductiveautomation.com/exchange/110/versions)

## License
+ [MIT](https://choosealicense.com/licenses/mit/)
+ [Terms & Conditions](https://inductiveautomation.com/exchange/terms)
+ [Acceptable Use](https://inductiveautomation.com/exchange/use)
