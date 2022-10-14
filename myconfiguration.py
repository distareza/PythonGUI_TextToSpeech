import configparser
config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

voicerss_api = config.get("voicerss.org", "api_key")
xrapid_api = config.get("voicerss.org", "x_rapid_api_key")
xrapid_host = config.get("voicerss.org", "x_rapid_host")
voicerss_url = config.get("voicerss.org", "voicerss_url")
