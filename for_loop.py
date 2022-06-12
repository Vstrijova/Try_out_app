import streamlit as st
from PIL import Image
from gtts import gTTS
from googletrans import Translator
translator = Translator()
from transliterate import translit, get_available_language_codes

st.title("Італійський розмовник для дітей - Итальянский разговорник для детей")
st.write( """ -  UK: Цей додаток має на меті допомогти українським дітям, як російською, так і українською мовою, вивчити та використовувати деякі корисні фрази італійською""")
st.write(""" -  RU: Это приложение нацелено на то, чтобы помочь украинским и русскоязычным детям выучить и использовать некоторые полезные фразы на итальянском языке""")
purpose = st.checkbox('Click here if you want to know the purpose of this app in another language')
if purpose:
  lang = st.text_input("Insert the code of a language in which you want to know the purpose of the app:", 'it', help= "en for English, de for German, it for Italian, es for Spanish, pt for Portuguese")
  translation = translator.translate('The purpose of this app is to help Ukrainian children, both native speakers of Russian and Ukrainian, learn some useful phrases for interacting with their peers in different contexts. ', src='en', dest=lang)
  purposetext = translation.text
  st.write(purposetext)
else:
  pass


language = st.radio( "Виберіть мову - Выберите язык" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин канцтоваров'))
  places = ['Площадка для игр', 'Школа', 'Магазин канцтоваров']
  images = ['playground.jpg', 'school.jpg', 'stationary_shop.jpg']
  for place, image in zip(places, images):
    if place == placechoice:
      st.image(image)
  cola, colb, colc, cold = st.columns(4)
  with cola:
    st.subheader("Полезные выражения")
  with colb:
    st.subheader("Итальянский перевод")
  with colc:
    st.subheader("Вот как это звучит")
  with cold:
    st.subheader("На кириллице")
      
  phrases_ru = {'Площадка для игр': [{'Пойдем в парк' : 'Andiamo al parco'},
                                   {'Давай играть в прятки' : 'Giochiamo a nascondino'},
                                   {'Давай покатаемся на качелях' : "Andiamo sull'altalena"},
                                   {'Пойдем на горку' : 'Andiamo sullo scivolo'},
                                   {'Давайте прыгать на скакалке' : 'Saltiamo la corda'}],
              'Школа': [{'Потом поиграем вместе?' : 'Dopo giochiamo insieme?'},
                         {'Давай сделаем пазл' : 'Facciamo un puzzle'},
                         {'Давай рисовать' : 'Disegnamo?'},
                         {'Пойдём в сад?' : 'Andiamo in giardino?'},
                         {'Могу ли я взять твой фломастер?' : 'Mi presti il tuo pennarello?'}],
              'Магазин канцтоваров': [{' Добрый день' : 'Buongiorno'},
                                      {'Мне нужны тетради' : 'Mi servirebbero dei quaderni'},
                                      {'Мне нужна линейка' : 'Avrei bisogno di un righello'},
                                      {'Мне нужны цветные карандаши' : 'Mi servirebbero le matite colorate'},
                                      {'Сколько это стоит?' : 'Quanto costa?'}]
                        }
  phrase_list_place = phrases_ru[placechoice]
  for phrasecouple in phrase_list_place:
    for rus, ita in phrasecouple.items():
      col1, col2, col3, col4 = st.columns(4)
      with col1:
        st.write(rus)
      with col2:
        translation = translator.translate(rus, dest= 'it')
        translated_text= translation.text
        if translated_text != ita:
          translated_text = ita
        else:
          pass
        st.write(translated_text)
      with col3:
        tts1=gTTS(translated_text, lang = 'it')
        tts1.save('your_file.mp3')
        audio_file = open('your_file.mp3', 'rb')
        st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      with col4:
        transliterated_text = translit(translated_text, 'ru')
        st.write(transliterated_text)
  else:
    pass
  
if language == 'Yкраїнський':
  placechoice = st.selectbox("Куди ти хочеш піти сьогодні? Bыбери одно з вказаних місць:", ('Майданчик для ігор', 'Школа', 'Магазин канцтоварів'))
  places = ['Майданчик для ігор', 'Школа', 'Магазин канцтоварів']
  images = ['playground.jpg', 'school.jpg', 'stationary_shop.jpg']
  for place, image in zip(places, images):
    if place == placechoice:
      st.image(image)
    else:
      pass
  cola, colb, colc, cold = st.columns(4)
  with cola:
    st.subheader("Корисні вирази")
  with colb:
    st.subheader("Італійський переклад")
  with colc:
    st.subheader("От як це звучить")
  with cold:
    st.subheader("На кирилиці")
  
  phrases_ukr = {'Майданчик для ігор': [{'Підемо в парк' : 'Andiamo al parco'},
                                   {'Давай пограємо в хованки' : 'Giochiamo a nascondino'},
                                   {'Xодімо на гойдалки' : "Andiamo sull'altalena"},
                                   {'Підемо на гірку' : 'Andiamo sullo scivolo'},
                                   {'Давайте стрибати на скакалці' : 'Saltiamo la corda'}],
              'Школа': [{'Потім пограємось разом?' : 'Dopo giochiamo insieme?'},
                         {'Давай зробимо пазл' : 'Facciamo un puzzle'},
                         {'Давай малювати' : 'Disegnamo?'},
                         {'Підемо в сад?' : 'Andiamo in giardino?'},
                         {'Чи можу я узяти твій фломастер?' : 'Mi presti il tuo pennarello?'}],
              'Магазин канцтоварів': [{'Доброго ранку' : 'Buongiorno'},
                                      {'Мені потрібні зошити' : 'Mi servirebbero dei quaderni'},
                                      {'Мені потрібна лінійка' : 'Avrei bisogno di un righello'},
                                      {'Мені потрібні кольорові олівці' : 'Mi servirebbero le matite colorate'},
                                      {'Скільки це коштує?' : 'Quanto costa?'}]
                        }
  phrase_list_place = phrases_ukr[placecoiche]
  for phrasecouple in phrase_list_place:
    for ukr, ita in phrasecouple.items():
      col1, col2, col3, col4 = st.columns(4)
      with col1:
        st.write(ukr)
      with col2:
        translation = translator.translate(rus, dest= 'it')
        translated_text= translation.text
        if translated_text != ita:
          translated_text = ita
        else:
          pass
        st.write(translated_text)
      with col3:
        tts1=gTTS(translated_text, lang = 'it')
        tts1.save('your_file.mp3')
        audio_file = open('your_file.mp3', 'rb')
        st.audio(data=audio_file, format="audio/mp3", start_time = 0)
      with col4:
        transliterated_text = translit(translated_text, 'uk')
        st.write(transliterated_text)
  else:
    pass

  with st.expander("See credits"):
     st.write("""- For images: https://unsplash.com/ """)
     st.write("""- For googletrans: https://pypi.org/project/googletrans/ """)
     st.write("""- For google-transliterate-api: https://pypi.org/project/google-transliteration-api/ """)
     st.write("""- For text-to-speech: https://pypi.org/project/SpeechRecognition/""")
