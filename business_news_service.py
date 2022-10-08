import json
from google.cloud import storage



storage_client = storage.Client()
bucket = storage_client.bucket("buba_news_data")
obj = {
    'authors': ['Саша Кириллова', 'Https', 'Img-Cdn.Tinkoffjournal.Ru I Width Height Bmc', 
    'Вячеслав Дмитриевич', 'Маша Романова', 'Скажи', 'Даниил Смирнов', 'Алёна Игоревна', 'Женщина С Кошкой', 'Алексей Н'], 
    'date_download': '2022-10-08 00:27:44', 
    'date_modify': None, 
    'date_publish': '2022-05-16 14:14:55', 
    'description': '«Макдональдс» объявил об уходе из России спустя два месяца после приостановки работы. Компания собирается продать все рестораны местному покупателю.. Новости по тэгам: покупки, бизнес, еда, актуальное', 
    #'filename': 'https%3A%2F%2Fjournal.tinkoff.ru%2Fnews%2Fmcdonalds-the-end%2F.json', 
    'image_url': 'http://img-cdn.tinkoffjournal.ru/-/mcdonalds-the-end-fb-3pvvo7f.uwvkxg.png', 
    'language': 'ru', 
    'localpath': None, 
    'maintext': 'Саша Кириллова больше не закажет макзавтрак Профиль автора\n«Макдональдс» объявил об уходе из России спустя два месяца после приостановки работы. Компания собирается продать все рестораны местному покупателю.\nНовый владелец не сможет использовать название, логотип, брендинг и меню в ресторанах в России, но «Макдональдс» сохранит в стране свои товарные знаки. В компании пообещали оставить зарплаты работникам до завершения сделки.\nПокупатель сети неизвестен. Под каким названием будут работать рестораны после сделки, пока тоже неясно.\nГендиректор «Макдональдса» Крис Кемпчински заявил, что компания «гордится сотрудниками, поставщиками и местными франчайзи», но поддерживать бизнес в России «нерентабельно и не соответствует идеалам компании».\n«Макдональдс» закрыт в России с 14 марта, но часть ресторанов продолжает работать по франшизе. Всего в стране насчитывается 850 заведений, в них работали 62 тысячи сотрудников.', 
    'source_domain': 'journal.tinkoff.ru', 
    'text': None, 
    'title': '"Макдональдс" уходит из России и продает бизнес', 
    'title_page': None, 
    'title_rss': None, 
    'url': 'https://journal.tinkoff.ru/news/mcdonalds-the-end/',
    'id': "mcdonalds-the-end"
}
blob = bucket.blob(obj["source_domain"] + "/" + obj["id"])
blob.upload_from_string(json.dumps(obj, ensure_ascii=False))
blob.download_to_filename(obj["id"] + ".json")