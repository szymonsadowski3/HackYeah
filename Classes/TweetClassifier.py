from textblob.classifiers import NaiveBayesClassifier


LIST_OF_TERMS = ["Lokata", "Obligacja", "Kredyt", "Ubezpieczenie", "Oszczędzanie", "Ubezpieczenie",
                 "Fundusz inwestycyjny", "Budżet", "Odsetki", "Zadłużenie",
                 "Inwestycja", "Inflacja"]


class TweetClassifier(object):
    def __init__(self):
        train_data = [
            ('Basia wpłaciła do banku pewną kwotę na lokatę roczną oprocentowaną 3% w skali roku.'
             'Jaką kwotę wpłaciła Basia jeżeli po roku +', 'Lokata'),
            ('jaka lokate polecacie gdzie mozna co miesiac przelewac jakas stala sume?', 'Lokata'),
            ('Depozyty bankowe | Jaką wybrać lokatę, żeby zarobić ponad inflację', 'Lokata'),
            ('ja z dziadkiem obliczaliśmy jaką miałbym emeryturę gdybym to co oddaję do ZUSu sam odkładał na lokate.eh.', 'Lokata'),
            ('Jaka lokata jest najlepsza: Jak wybierać lokatę bankową? Depozyty bankowe różnią się nie tylko oprocentowaniem, ale…', 'Lokata'),

            ('Ale obligacje są zbywalne na rynku. Więc to jest foema przechowywania kapitału. Oprocentowana. '
             'Po co trzymać kapitał w gotówce? Naciąga Pan.', 'Obligacja'),
            ('To były obligacje ,w 100% zapisy z kont OFE przeniesiono na nasze konta w ZUS, '
             'gdzie co roku w lipcu są waloryzowane o wskaźnik inflacji.', 'Obligacja'),
            ('I jeszcze sumuje dług zapominając źe są co roku obligacje któte naleźy wykupić..'
             'to jest tak źe jedno narasta a drugie maleje...', 'Obligacja'),
            ('A to nie tak, że kupują faktycznie za euro te obligacje i przez co '
             'narażeni są na inflację w strefie i na różnice kursowe?', 'Obligacja'),

            ('No to co mam robić? Zmienić poglądy wziąć kredyt i emigrować. '
             'Myślę to co myślałem i jestem tam gdzie byłem.', 'Kredyt'),
            ('Gdzie wziąć kredyt na firmę?', 'Kredyt'),
            ('Gdzie najlepiej wziąć 5k pożyczki na 16 rat? Może byc to kredyt konsolidacyjny?', 'Kredyt'),
            ('z nami dowiesz się gdzie i jak wziąć kredyt, doradzamy i wspieramy. Zadzwoń!', 'Kredyt'),
            ('Fajne rzeczy w tych reklamach. W jednej namawiają, żeby wziąć kredyt na suknię ślubną, a w drugiej tłumaczą, gdzie się zgłosić z długami.', 'Kredyt'),

            ('To może czas zająć się tym na co pieniądze ze składek są przejadane.Poza tym sam pisałeś,że nawet biedny może mieć ubezpieczenie, jego wola.', 'Ubezpieczenie'),
            ('No i kolejny człowiek zorientował się że "ubezpieczenie od utraty pracy" nie chroni jego interesów tylko interes banku.', 'Ubezpieczenie'),
            ('Co m-c na ubezpieczenie zdrowotne płacę jakieś 540 zł. Do lekarza nie chodzę. I tak przez lata. Mało kasy?', 'Ubezpieczenie'),
            ('bardzo prosto taniej wyskrobac  a np  ubezpieczenie wypadkowym OC podstawowa skladka zapewnia tylko ze wypuszcza ciebie  zywego ze szpitala', 'Ubezpieczenie'),
            ('Miałem nieprzyjemność być dawno temu klientem Urzędu Pracy, stracony czas. Ludzie tam przychodzili tylko żeby mieć ubezpieczenie zdrowotne', 'Ubezpieczenie'),
            ('Całe szczęście, choć wolałbym wiedzieć na ile to realne ubezpieczenie. ;) Rocznie to ponad 350zł.', 'Ubezpieczenie'),
            ('Lekarze zaproponowali podniesienie składki na ubezpieczenie zdrowotne Premier powiedziała,  nie!  a ja mowie spadajcie', 'Ubezpieczenie'),

            ('Jak ograniczyć zużycie prądu i obniżyć rachunki? Podpowiadamy!', 'Oszczędzanie'),
            ('Szwajcaria Polacy : Zapotrzebowanie na tanie mieszkanie : to w Szwajcarii najbardziej skuteczne oszczędzanie :', 'Oszczędzanie'),
            ('SYMPTOMY złego gospodarowania własnym budżetem', 'Oszczędzanie'),
            ('Czy znasz sposoby na oszczędzanie energii w domu? Warto o tym pomyśleć już na etapie planowania budowy:', 'Oszczędzanie'),
            ('Sztuka zarządzania budżetem domowym', 'Oszczędzanie'),
            ('wg prezesa GPW: dziś patriotyzm to zachęcanie ludzi do inwestowania na GPW. Kluczowe jest oszczędzanie na emeryturę', 'Oszczędzanie'),
            ('Ubezpieczyciele wyszli na plus na #ubezpieczenie #oc. Mimo to kolejne podwyżki składek są prawdopodobne. Dlaczego?:', 'Ubezpieczenie'),

            ('#kara za brak #oc pow. 14 dni w 2018 to najpewniej 4200 zł. Nie chcesz tyle płacić? Znajdź tanie ubezpieczenie:', 'Ubezpieczenie'),
            ('Piątek 13? Nie ma się czego bać – z #ubezpieczenie.m w pech nie będzie taki straszny', 'Ubezpieczenie'),
            ('Ubiegając się o ubezpieczenie na życie nie unikniesz szeregu pytań odnośnie swojego stanu zdrowia', 'Ubezpieczenie'),
            ('Poznaj korzyści płynące z ubezpieczenia i przestań się martwić o swoje mienie! ', 'Ubezpieczenie'),

            (' inwestycja  zwróci się za ile lat ?? brak odp 100 lat ? ', 'Inwestycja'),
            ('Wielka inwestycja budowlana? Nie ma problemu, zajmiemy się tym! ', 'Inwestycja'),
            ('Dziś otwarcie osiedla ma Nowym Świecie - pierwszej od wielu lat inwestycji mieszkaniowej w Mikołowie', 'Inwestycja'),
            ('Prezes: Inwestycja zakłada wdrażanie innowacji będących dźwignią rozwoju przemysłu chemicznego i całej polskiej gospodarki', 'Inwestycja'),

            ('To co się teraz dzieje to nie inflacja. Raczej to popyt i podaż. Ludzie mają kasę to więcej schodzi i ceny idą w górę bo i tak zejdzie', 'Inflacja'),
            ('Poniższy wykres pokazuje jak rosnąca inflacja zżera wszelkie oszczędności. ', 'Inflacja'),
            ('Ceny żywności rosną ponad dwa razy szybciej niż inflacja bazowa - obydwa wsk. są w trendzie wzrostowym ', 'Inflacja'),
        ]

        self.classifier = NaiveBayesClassifier(train_data)

    def classify_tweet(self, tweet):
        return self.classifier.classify(tweet)
