# DataBase_Client

Opis programu:
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
