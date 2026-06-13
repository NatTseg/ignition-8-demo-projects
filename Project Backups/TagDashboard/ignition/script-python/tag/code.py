def addHistory(tagPath, provider, scanClass, deadband, deadbandMode, valueMode):
	import system
	
	#attributes = {}
	#attributes["HistoryEnabled"] = True
	#attributes["PrimaryHistoryProvider"] = provider
	#attributes["HistoricalScanclass"] = scanClass
	#attributes["HistoricalDeadband"] = deadband
	#attributes["HistoricalDeadbandMode"] = deadbandMode
	#attributes["InterpolationMode"] = valueMode

	tagConfig = system.tag.getConfiguration(tagPath, False)
	tagConfig[0]['historyEnabled'] = True
	tagConfig[0]['historyProvider'] = provider
	tagConfig[0]['historicalDeadbandStyle'] = valueMode
	tagConfig[0]['historicalDeadbandMode'] = deadbandMode
	tagConfig[0]['historicalDeadband'] = deadband
	if scanClass == 'OnChange':
		tagConfig[0]['sampleMode'] =  'OnChange'
	else:
		tagConfig[0]['historyTagGroup'] =  scanClass
		tagConfig[0]['sampleMode'] =  'TagGroup'

	
	#system.tag.editTag(tagPath=tagPath, attributes=attributes)
	system.tag.configure(tagPath, tagConfig, 'o')
	utils.refreshTagBrowser()
	
def addAlarms(tagPath, alarms):
	import system
	
	alarmConfig = {}
	for alarm in system.dataset.toPyDataSet(alarms):
		name = alarm["alarm"]
		config = alarm["config"]
		
		alarmProps = []
		for prop in system.dataset.toPyDataSet(config):
			alarmProps.append([prop[0], "Value", prop[1]])
		
		alarmConfig[name] = alarmProps
	
	system.tag.editTag(tagPath=tagPath, alarmConfig=alarmConfig)
	utils.refreshTagBrowser()
	
def read(path):
	return system.tag.read(path).value
	
def readAll(path):
	tag = {}
	tag['value'] = system.tag.read(path).value
	return tag