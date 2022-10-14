"""
	https://rapidapi.com/voicerss/api/text-to-speech-1

"""
import requests
import myconfiguration
import urllib.parse
from playsound import playsound

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key": myconfiguration.voicerss_api}

def convertToSpeech(text:str):
	"""
	:param text:
	:return:
	"""
	payload = f"src={urllib.parse.quote(text)}&hl=en-us&r=0&c=mp3&f=8khz_8bit_mono"
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": myconfiguration.xrapid_api,
		"X-RapidAPI-Host": myconfiguration.xrapid_host
	}

	return requests.request("POST", url, data=payload, headers=headers, params=querystring)

def saveToFile(text:str, file_path:str):
	"""
	:param text:
	:param file_path:
	:return:
	"""
	response = convertToSpeech(text)
	with open(file_path, 'wb') as f:
		f.write(response.content)
		f.close()

	print(f"save to {file_path}")

def play_sound(text:str):
	file_to_save = "test.mp3"
	saveToFile(text, file_to_save)

	playsound(file_to_save)

#saveToFile("Hello World", "C:/tmp/helloworld.mp3")

#play_sound("ini reza lagi test")

