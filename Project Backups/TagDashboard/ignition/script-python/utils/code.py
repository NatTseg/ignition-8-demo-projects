def getGradientPaint(color1, color2):
	import system
	from com.inductiveautomation.ignition.client.util.gui.paints import RelativeLinearGradientPaint
	from com.inductiveautomation.ignition.client.util.gui.paints.MultipleGradientPaint import CycleMethod
	from com.inductiveautomation.ignition.client.util.gui.paints.MultipleGradientPaint import ColorSpaceType 
	from java.awt import Color
	from java.awt.geom import Point2D
	from java.awt.geom import AffineTransform
	
	color1Parts = color1.split(",")
	if len(color1Parts) == 3:
		color1 = Color(int(color1Parts[0]), int(color1Parts[1]), int(color1Parts[2]))
	else:
		color1 = Color(int(color1Parts[0]), int(color1Parts[1]), int(color1Parts[2]), int(color1Parts[3]))
		
	color2Parts = color2.split(",")
	if len(color2Parts) == 3:
		color2 = Color(int(color2Parts[0]), int(color2Parts[1]), int(color2Parts[2]))
	else:
		color2 = Color(int(color2Parts[0]), int(color2Parts[1]), int(color2Parts[2]), int(color2Parts[3]))
	
	return RelativeLinearGradientPaint(Point2D.Double(0.4375, 0.004000000189989805), Point2D.Double(0.4375, 0.9959999918937683), [0.0, 1.0], [color1, color2], CycleMethod.NO_CYCLE, ColorSpaceType.SRGB, AffineTransform(1.0, 0.0, 0.0, 1.0, 0.0, 0.0))
	
def loadSettings():
	import system
	
	system.tag.write("[Client]Selected Tag Path", None)
	
	try:
		username = system.security.getUsername()
		settings = system.db.runScalarPrepQuery("SELECT settings FROM tb_user_settings WHERE username = ?", [username])
		if settings != None:
			settings = system.util.jsonDecode(settings)
			for tagPath in settings.keys():
				system.tag.write(tagPath, settings[tagPath])
	except:
		pass
	
def addSetting(settingsMap, tagPath):
	import system
	settingsMap[tagPath] = system.tag.read(tagPath).value
	
def saveSettings(event):
	import system
	#import project
	
	username = system.security.getUsername()
	settingsMap = {}
		
	addSetting(settingsMap, "[Client]Settings/Tag Mode")
	addSetting(settingsMap, "[Client]Settings/Folders Only")
	addSetting(settingsMap, "[Client]Settings/Allow Add History")
	addSetting(settingsMap, "[Client]Settings/Allow Add Alarms")
	addSetting(settingsMap, "[Client]Settings/Sparkline Duration")
	addSetting(settingsMap, "[Client]Settings/Alarm Panel Height")
	addSetting(settingsMap, "[Client]Settings/Tag History Panel Height")
	addSetting(settingsMap, "[Client]Theme/Alarm Color 1")
	addSetting(settingsMap, "[Client]Theme/Alarm Color 2")
	addSetting(settingsMap, "[Client]Theme/Alternate Background Color")
	addSetting(settingsMap, "[Client]Theme/Background Color")
	addSetting(settingsMap, "[Client]Theme/Disabled Text Color")
	addSetting(settingsMap, "[Client]Theme/Header Background Color")
	addSetting(settingsMap, "[Client]Theme/Header Color")
	addSetting(settingsMap, "[Client]Theme/Sparkline Color")
	addSetting(settingsMap, "[Client]Theme/Sparkline Last Marker Color")
	addSetting(settingsMap, "[Client]Theme/Stroke Color")
	addSetting(settingsMap, "[Client]Theme/Text Color")
	addSetting(settingsMap, "[Client]Theme/Window Background Color")
	addSetting(settingsMap, "[Client]Theme/Window Background Color 2")
	
	settings = system.util.jsonEncode(settingsMap)
	
	try:
		system.db.runScalarQuery("SELECT id FROM tb_user_settings LIMIT 1")
	except:
		system.db.runPrepUpdate("""CREATE TABLE `tb_user_settings` (
								    `id` INT NOT NULL AUTO_INCREMENT,
								    `username` VARCHAR(45) NOT NULL,
								    `settings` TEXT NOT NULL,
								  PRIMARY KEY (`id`))""")
								  
	id = system.db.runScalarPrepQuery("SELECT id FROM tb_user_settings WHERE username = ?", [username])
	if id == None:
		system.db.runPrepUpdate("INSERT INTO tb_user_settings (username, settings) VALUES (?,?)", [username, settings])
	else:
		system.db.runPrepUpdate("UPDATE tb_user_settings SET settings = ? WHERE id = ?", [settings, id])
		
	refreshTagBrowser()
		
	system.gui.messageBox("Settings saved for '%s'" % username)
	
def refreshTagBrowser():
	import system
	
	try:
		win = system.gui.getWindow("Tag Dashboard")
		system.db.refresh(win.getRootContainer().getComponent("Tag Browser").getLoadedTemplate().getComponent("Template Canvas"), "templates")
	except:
		pass
	
def getHistoryProviders():
	import system
	
	data = []
	res = system.dataset.toPyDataSet(system.db.getConnections())
	for row in res:
		data.append([row["Name"]])

	return system.dataset.toDataSet(["Name"], data)	