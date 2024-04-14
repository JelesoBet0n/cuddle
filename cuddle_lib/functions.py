from cuddle_lib import simple_logger as logger

SimpleLogger = logger.SimpleLogger


class Functions:
    def __init__(self, telebot, bot):
        self.telebot = telebot
        self.bot = bot

    def send(self, chat_id, text, markup=None):
        msg = self.bot.send_message(chat_id, text, reply_markup=markup)
        SimpleLogger.server(f"sent >>> {text}")
        return msg

    def send_audio(self, chat_id, audio_dir, text=None):
        audio = open(f"{audio_dir}", "rb")
        self.bot.send_audio(chat_id, audio, text)
        SimpleLogger.server(f"{audio_dir} sent")

    def send_photo(self, chat_id, photo_dir):
        photo = open(f"{photo_dir}", "rb")
        self.bot.send_photo(chat_id, photo)
        SimpleLogger.server(f"{photo_dir} sent")

    def send_document(self, chat_id, document_dir):
        doc = open(f"{document_dir}", "rb")
        self.bot.send_document(chat_id, doc)
        SimpleLogger.server(f"{document_dir} sent")

    def send_sticker(self, chat_id, sti_dir):
        sti = open(f"{sti_dir}", "rb")
        self.bot.send_sticker(chat_id, sti)
        SimpleLogger.server(f"{sti_dir} sent")

    def send_video(self, chat_id, video_dir):
        video = open(f"{video_dir}", "rb")
        self.bot.send_sticker(chat_id, video)
        SimpleLogger.server(f"{video_dir} sent")

    def edit(self, text, chat_id, message_id):
        self.bot.edit_message_text(text, chat_id, message_id)
        SimpleLogger.server(f"{message_id} edited to {text}")

    def reply(self, message, text, markup=None):
        self.bot.reply_to(message, text, reply_markup=markup)
        SimpleLogger.server(f"replied {text} to {message.message_id}")

    def next_step(self, message, func):
        self.bot.register_next_step_handler(message, func)

    def delete(self, chat_id, message_id):
        self.bot.delete_message(chat_id, message_id)
        SimpleLogger.server(f"{message_id} deleted")

    @staticmethod
    def read(message):
        return message.text

    @staticmethod
    def read_reply(message):
        if message.reply_to_message:
            return message.text
        else:
            return "Not reply"

    def inline_button(self, text="text", callback=None, url=None, empty=False):
        markup = self.telebot.types.InlineKeyboardMarkup()
        if not empty:
            button = self.telebot.types.InlineKeyboardButton(text, callback_data=f"{callback}", url=url)
            markup.add(button)

        return markup

    def reply_keyboard(self, text=None, texts=None, is_keyboard_resizeable=True):
        markup = self.telebot.types.ReplyKeyboardMarkup(resize_keyboard=is_keyboard_resizeable)
        if text is None and texts is not None:
            for text in texts:
                markup.row(text)
        elif text is not None and texts is None:
            button = self.telebot.types.KeyboardButton(text)
            markup.add(button)
        elif text is not None and texts is not None:
            print("Can't make button! Can take only 'text' or only 'texts'.")
        else:
            print("Can't make button! Parameters 'text' and 'texts' are empty.")

    def open_webapp(self, markup, text, url):
        markup.add(self.telebot.types.InlineKeyboardButton(
            text=text, web_app=self.telebot.types.WebAppInfo(url=url)))

        SimpleLogger.server(f"webapp sent: {text}, {url}")
        return markup

    def invoice(self, chat_id, name, description, provider_token, currency, label, price, invoice="invoice"):
        self.bot.send_invoice(chat_id, name, description, invoice,
                              provider_token, currency, [self.telebot.types.LabeledPrice(label, price * 100)])
        SimpleLogger.server(f"invoice on {name} sent")
