import Bot
from dotenv import dotenv_values

if __name__ == "__main__":
	vk_bot = Bot.Bot(dotenv_values("val.env")['token'])

	vk_bot.do_auth()
	vk_bot.run_bot()

	#url = dotenv_values("val.env")['url']
	#get_request.GetRequest(url)
	#html_text = get_request.GetHTMLCodeEncoding('iso-8859-1', 'utf-8')
	#parser_text.ParsingHTMLCode(html_text = html_text, tag = 'h1')