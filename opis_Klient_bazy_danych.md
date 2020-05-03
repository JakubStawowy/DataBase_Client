# DataBase_Client

Temat projektu: Klient Bazy Danych

Autor: Jakub Stawowy

Link do projektu na platformie github: https://github.com/JakubStawowy/DataBase_Client

Opis projektu:
Jest to program udający prostą bazę danych. Pozwala on na tworzenie prostych tabel, zapis oraz wyszukiwanie w nich danych. 
-Każda tabela może zawierać dowolną ilość kolumn i wierszy. Ilość, nazwę oraz typ danych w kolumnie deklaruje się podczas procesu tworzenia nowej tabeli (później nie ma już możliwości zmiany ilośći kolumn), natomiast wiersze dodajemy przy edytowaniu tabeli lub używając funkcji "Dodaj wiersz".
-Tabela może zawierać dane o następujących typach:
  -int
  -int (Auto-increment)
  -float
  -str
-Program jest oparty na wzorcu architektonicznym MVC (Model-View-Controller) i jest      
 podzielony na:
  -Moduł ProjectModel.py zawierający Klasę ProjectModel przechowującą strukturę tabel (tableStructure) oraz zawierającą wszelkie metody operujące na tabelach (dodawanie tabeli do struktury, usuwanie tabeli ze struktury, dodawanie rekordu do tabeli, wyszukiwanie tabeli, przeszukiwanie tabeli, wyszukiwanie rekordu w tabeli, zapis/odczyt z pliku)
  -Moduł ProjectController.py zawierający Klasę ProjectController przechowującą metody kontrolujące dane wprowadzane przez użytkownika (nazwy tabel, nazwy kolumn, typ kolumn, typ danych w kolumnach)
  -Moduł ProjectGUI.py zawierający wszelkie klasy dziedziczące po klasach z biblioteki QT (QMainWindow, QDialog).
  -Moduł Table.py zawierający klasę Table przechowującą podstawową strukturę tabeli (Nazwa tabeli, ilość kolumn, ilość wierszy, słownik nazw i typów kolumn, kontent tabeli) oraz podstawowe metody operujące na danych (dodaj/usuń wiersz, dodaj kolumne, ustawianie poszczgólnych parametrów)
  -Moduł MyLabel.py przechowujący klasę MyLabel która zawiera metodę tworzącą etykietę w danym oknie (metaklasie)
  -Moduł MyButton.py przechowujący klasę MyButton która zawiera metodę tworzącą przycisk w danym oknie (metaklasie)
-Główne okno (MainWindow) zawiera przyciski: "Dodaj tabelę", "Usuń tabelę", "Edytuj tabelę", "Usuń wiersz", "Edytuj wiersz", "Wyszukaj" oraz dwie listy (QComboBox - pierwsza zawiera wylistowane nazwy tabel, druga zaś po wyborze tabeli listuje jej rekordy)
-Okno dodawania tabeli zawiera przyciski: "Dodaj kolumnę", "Dodaj tabelę" oraz "Anuluj". Zawiera również pole tekstowe pozwalające na wpisanie nazwy tabeli oraz etykietę wyświetlającą ilość kolumn w tworzonej tabeli. Jeżeli nazwa tabeli jest pusta albo ilość kolumn jest równa zero - za sprawą kontrolera rzucany jest odpowiedni wyjątek (wyświetlaja się okienko ostrzegawcze)
-Okno dodawania kolumny zawiera przyciski: "Dodaj kolumnę", "Anuluj". Zawiera również pole tekstowe pozwalające na wpisanie nazwy kolumny oraz listę z której użytkownik może wybrać typ danych w kolumnie. Jeżeli nazwa kolumny jest pusta lub typ nie został wybrany - rzucany jest odpowiedni wyjątek (wyświetla się okienko ostrzegawcze)
-Okno edytowania tabeli wyświetla wybraną tabelę wraz z jej zawartością i pozwala na edytowanie jej danych. Zawiera również następujące przyciski: "Dodaj wiersz" oraz "Zapisz tabelę"
-Okno dodawania wiersza jest bardzo podobne do okna edytowania tabeli, jednak pozwala na dodanie tylko jednego wiersza. Zawiera przyciski: "Dodaj wiersz", "Anuluj"
-Okno edytowania wiersza jest bardzo podobne do okna dodawania wiersza, jednak wyświetla wybrany przez nas wiersz i pozwala na edytowanie jego danych. Zawiera przyciski: "Zapisz wiersz", "Anuluj"
-Okno wyszukiwania zawiera pole tekstowe pozwalące na wpisanie odpowiedniego wyrażenia-lambda na którego podstawie sprawdzane są dane w wybranej przez nas tabeli (jeśli klient nie wie jak wygląda wyrażenie-lambda - jest możliwość wyświetlenia przykładu z objaśnieniem działania). Wyniki wyszukiwania wyświetlane są w nowym oknie w postaci tabeli zawierającej tylko te rekordy, dla których wyrażenie zwróciło wartość true.
-Przy zamykaniu programu klient ma możliwość zapisu tabel w postaci struktury wpisanej w plik z rozszerzeniem '.txt'. Jest również możliwość wczytywania takiego pliku za pomocą przycisku "Otwórz plik". Okno otwierania pliku zawiera pole tekstowe, do którego należy wpisać ścieżkę lokalizacji pliku.

Testy

1) Utworzenie tabeli "test1" z kolumnami liczbową "ID" (typ int), dwoma tekstowymi "imię" oraz "nazwisko" oraz liczbową "wzrost" (typ float).
2) Dodanie wiersza do tabeli "test1" z danymi "1","Roch","Przyłbipięt","1.50" - oczekiwane powodzenie.
3) Dodanie wiersza do tabeli "test1" z danymi "2","Ziemniaczysław","Bulwiasty", "1.91" - oczekiwane powodzenie.
4) Dodanie wiersza do tabeli "test1" z danymi "cztery", "bla","bla","-90" - oczekiwane niepowodzenie (dane tekstowe w polu liczbowym).
5) Dodanie wiersza do tabeli "test1" z danymi "3.14","pi","ludolfina","314e-2" - oczekiwane niepowodzenie (liczba rzeczywista w kolumnie z liczbą całkowitą).
6) Wyświetlenie zawartości tabeli "test1"
7) Dodanie trzech kolejnych wierszy do tabeli "test1" i usunięcie dwóch wierszy z niej (pierwszego i środkowego), w obu przypadkach najpierw anulowanie operacji, a potem jej akceptacja.
8) Utworzenie tabeli "test2" z kolumnami "reserved" typu string oraz "kolor" typu liczba całkowita
9) Dodanie wiersza do tabeli "test2" z danymi (puste pole), "1337" - oczekiwane powodzenie.
10) Dodanie wiersza do tabeli "test2" z danymi "bla","1939b" - oczekiwane niepowodzenie (tekst w polu typu liczba całkowita).
11) Usunięcie tabeli "test2", najpierw anulowanie operacji, a potem jej akceptacja.
12) Próba utworzenia tabeli bez nazwy - oczekiwane niepowodzenie.
13) Próba utworzenia tabeli o nazwie " " (spacja) - oczekiwane niepowodzenie.
14) Próba utworzenia tabeli z kolumną bez nazwy - oczekiwane niepowodzenie.
15) Próba utworzenia tabeli z kolumną o nazwie "    " (cztery spacje) - oczekiwane niepowodzenie.
16) Wypełnienie tabeli "test1" danymi tekstowymi (kolejne wartości "ID","wzrost" między 1.0 i 2.0) oraz wyszukanie w niej wierszy dla których "wzrost" ma wartość podaną przez prowadzącego oraz "ID" jest liczbą parzystą lub nieparzystą. 
