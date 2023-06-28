# **Projekt 1 - Baza danych dań restauracji**

## **Opis projektu:**

Celem projektu było stworzenie bazy danych zawierającej informacje <br> 
o daniach restauracji  oraz zintegrowanie jej z aplikacją okienkową PyQt5. <br>
Baza ta miała umożliwić użytkownikom przeglądanie menu  restauracji <br> 
oraz dodawanie i edycję dań za pomocą intuicyjnego interfejsu graficznego. <br> <p> 
W projekcie skorzystałam z języka ***Python*** oraz biblioteki ***PyQt5*** <br> do stworzenia ***aplikacji okienkowej***. Stworzyłam formularze umożliwiające <br> dodawanie, usuwanie i edycję dań oraz przeglądanie menu restauracji.
</p>
<p> Projekt został spełniony zgodnie z założeniami. Aplikacja okienkowa umożliwia <br> użytkownikom intuicyjne i łatwe korzystanie z bazy danych dań restauracji.<br> Interfejs graficzny jest przejrzysty i czytelny, co umożliwia szybkie znajdywanie <br> potrzebnych informacji.
</p>
<p> Projekt ten był dla mnie ważnym doświadczeniem, które pozwoliło mi na <br> poznanie różnych funkcji i możliwości biblioteki PyQt5 oraz lepsze zrozumienie <br> procesu tworzenia aplikacji okienkowych w języku Python.</p>

<hr>

## **Podział projektu**

- Components
    - Dishes
- Data
- Static
    - Images
        - Icons

<hr>

## **Components**

W projekcie znajduje się wiele komponentów,takich jak : "_pycache_", *"Dishes"*,<br> "_init_.py", *"custom_components.py"*, *"dishes_utils.py"*,*"users_utils.py"*,<br> *"windows.py"*, z których każdy pełni określoną rolę w funkcjonowaniu aplikacji.<br> Dzięki tym komponentom możliwe jest tworzenie aplikacji okienkowej o <br> rozbudowanej funkcjonalności i łatwej w obsłudze interfejsie użytkownika.

- **\_\_init\_\_.py**

    Plik \_\_init\_\_.py to pusty plik który umożliwia interpretowanie folderu Components jako pakiet.<br>

- **custom_components.py**

    Ten plik zawiera definicje nistandardowych komponentów takich jak klasa *"CustomListItem"*, która reprezentuje <br> niestandardowy element listy w aplikacji PyQt5. Klasa ta zawiera etykiety <br> z nazwą i ceną dania oraz przyciski do edycji i usuwania. Funkcja <br> *"add_custom_widget_to_list"* tworzy element listy i dodaje go do listy głównej.

- **dishes_utils.py**

    Ten plik zawiera funkcje dodające dania do karty menu oraz funkcje <br> pobierające informacje o daniach z karty menu. Funkcje *"_add_starter"*,<br> *"_add_main"* i *"_add_dessert"* dodają nowe dania do karty menu dla <br> odpowiednich kategorii. Funkcje *"get_all_dishes"*, *"get_all_starters"*,<br> *"get_all_mains"* i *"get_all_desserts"* służą do pobierania informacji o <br> daniach z karty menu. Funkcja *"validate_dish_input"* sprawdza <br> poprawność danych dla wprowadzonych nowych dań. Plik wymaga <br> modułów json i os.

    **validate_dish_input**  

    > Ta funkcja przyjmuje słownik opisujący danie i zwraca wartość typu<br> bool, określającą, czy dane o danym daniu są poprawne.<br>

   > W pierwszej kolejności funkcja sprawdza, czy nazwa dania składa <br> się tylko z liter, czy jest ciągiem znaków i czy jej długość mieści <br> się w zakresie od 1 do 32. Następnie sprawdzane są ceny dania<br> - czy są liczbami zmiennoprzecinkowymi, większymi od 0 i<br> mniejszymi od 250.

   > Funkcja sprawdza też, czy opis dania składa się z tekstu, czy jego <br> długość mieści się w zakresie od 1 do 300 i czy nie zawiera cyfr.

   > Jeśli danie posiada składniki, funkcja sprawdza, czy każdy z nich <br> jest ciągiem znaków, nie zawiera cyfr i ma długość większą od 0.

   > Na końcu funkcja sprawdza, czy rodzaj diety i kuchnia dania <br> należą do odpowiednich zbiorów dopuszczalnych wartości.

   > Jeśli któryś z powyższych warunków nie jest spełniony,<br> funkcja zwraca False. W przeciwnym razie zwraca True.

- **users_utils.py**

     #### Ten plik zawiera trzy funkcje związane z zarządzaniem użytkownikami w <br> aplikacji: 
    - Pierwsza funkcja "register_new_user" dodaje nowego użytkownika <br> do bazy danych z jego nazwą użytkownika, hasłem i datą <br> utworzenia konta. 
    - Druga funkcja "remove_all_users" usuwa wszystkich użytkowników <br> z bazy danych. 
    - Trzecia funkcja "login_user" pozwala na logowanie użytkownika,<br> sprawdzając jego dane logowania w bazie danych. 
    - czwarta funkcja "validate_registration_input" służy do walidacji <br> danych rejestracyjnych użytkownika. 
    #### Plik korzysta z biblioteki JSON i modułu datetime w Pythonie.

- **windows.py**

    Opis users_utils.py (krótkie wprowadzenie do pliku, max 50 słów)<br>

### **Components/Dishes**

To kluczowy element każdej kuchni. Bez różnorodnych  składników i potraw <br> trudno wyobrazić sobie smaczne i zrównoważone posiłki. W tym pliku <br> znajdziesz wiele ciekawych inspiracji na składniki i przepisy, które pozwolą <br> Ci urozmaicić swoje codzienne menu oraz zaskoczyć bliskich i znajomych w <br> trakcie specjalnych okazji. Od prostych dań jednogarnkowych po wyszukane <br> komponenty do dań gourmet - z pewnością znajdziesz tutaj coś dla siebie.

- **Dish.py**

    Klasa ***Dish*** to model dania, zawierający informacje o nazwie, cenie, opisie, <br> składnikach, typie diety oraz kuchni. Metoda ***serialize_price*** przelicza ceny <br> w różnych walutach na PLN, USD i EUR. Metody ***to_usd***, ***to_pln*** i ***to_eur*** <br> dokonują konwersji między walutami. Metoda ***get_dictionary_data*** zwraca <br> dane dania w formie słownika.

    **\_\_init\_\_** - Ten kod Pythona definiuje konstruktor klasy, która reprezentuje <br> danie. Konstruktor przyjmuje szereg argumentów, takich jak nazwa dania,<br> cena, opis, składniki, typ diety i kuchnia. Następnie przypisuje każdy z <br> argumentów do odpowiedniego atrybutu obiektu i stosuje pewne <br> transformacje, takie jak zamiana ceny na liczbę i rozdzielanie składników <br> na listę.
    ><pre>
    > <b>params</b>: name, price, description, ingredients, diet_type, cuisine<br>
    >         <i>name</i>: str - Nazwa dania<br>
    >         <i>price</i>: list[str] | str - Koszt dania<br>
    >         <i>description</i>: str - Opis dania<br>
    >         <i>ingredients</i>: list[str] - Lista składników dania<br>
    >         <i>diet_type</i>: str - Rodzaj dania (czy zawiera mięso, czy jest wegańskie, czy wegetariańskie)<br>
    >         <i>cuisine</i>: str - Naród z jakiego pochodzi danie<br><br>
    > <b>returns</b>: None
    ></pre>

    **serialize_price** - Ten kod Pythona definiuje funkcję, która zamienia cenę <br> zapisaną jako ciąg znaków na słownik zawierający ceny w trzech różnych <br> walutach (USD, PLN, EUR). Funkcja sprawdza, jaki symbol waluty znajduje <br> się w cenie (jeśli cena jest listą, przegląda każdą z nich), a następnie <br> przelicza ją na pozostałe waluty. Na końcu funkcja zaokrągla każdą cenę <br> do dwóch miejsc po przecinku i zwraca słownik z cenami. Ten kod jest <br> przydatny dla aplikacji, która musi wyświetlać ceny dania w różnych walutach. <br>
    ><pre>
    > <b>params</b>: price<br>
    >         <i>price</i>: list[str] | str - Koszt dania<br>
    > <b>returns</b>: dict - Słownik z cenami w różnych walutach
    ></pre>

    **to_usd** - Ten kod Pythona definiuje funkcję, która przelicza podaną cenę <br> na wartość w dolarach amerykańskich. Jeśli cena jest wyrażona w złotych,<br> to funkcja przelicza ją na dolary (przyjmując kurs 1 USD = 3.8 PLN). Jeśli <br> cena jest wyrażona w euro, to funkcja przelicza ją na dolary (przyjmując <br> kurs 1 USD = 1.18 EUR). Funkcja zwraca przeliczoną wartość ceny w USD. <br> Ten kod jest użyteczny w aplikacjach, które muszą przeliczać ceny z <br> różnych walut na USD.
    ><pre>
    > <b>params</b>: price<br>
    >           <i>price</i>: str - Cena w złotówkach albo euro.<br>
    > <b>returns</b>: str - Cena przekonwertowana do dolarów amerykańskich.
    ></pre>

    **to_pln** - Ten kod Pythona definiuje funkcję, która przelicza podaną cenę <br> na wartość w złotych polskich. Jeśli cena jest wyrażona w dolarach <br> amerykańskich, to funkcja przelicza ją na złotówki (przyjmując kurs <br> 1 USD = 3.8 PLN). Jeśli cena jest wyrażona w euro, to funkcja przelicza<br> ją na złotówki (przyjmując kurs 1 EUR = 4.5 PLN). Funkcja zwraca <br> przeliczoną wartość ceny w PLN. Ten kod jest użyteczny w aplikacjach,<br> które muszą przeliczać ceny z różnych walut na PLN.
    ><pre>
    > <b>params</b>: price<br>
    >           <i>price</i>: str - Cena w dolarach albo euro.<br>
    > <b>returns</b>: str - Cena przekonwertowana do złotówek.
    ></pre>

    **to_eur** - Ten kod Pythona definiuje funkcję, która przelicza podaną cenę <br> na wartość w euro. Jeśli cena jest wyrażona w dolarach amerykańskich,<br> to funkcja przelicza ją na euro (przyjmując kurs 1 EUR = 1.18 USD). Jeśli <br> cena jest wyrażona w złotych polskich, to funkcja przelicza ją na euro <br> (przyjmując kurs 1 EUR = 4.5 PLN). Funkcja zwraca przeliczoną wartość <br> ceny w EUR. Ten kod jest użyteczny w aplikacjach, które muszą przeliczać <br> ceny z różnych walut na EUR.<br>
    ><pre>
    > <b>params</b>: price<br>
    >           <i>price</i>: str - Cena w złotówkach albo dolarach.<br>
    > <b>returns</b>: str - Cena przekonwertowana do euro.
    ></pre>

    **get_dictionary_data** - Ten kod Pythona definiuje funkcję, która tworzy <br> i zwraca słownik zawierający dane o daniu. Słownik ten ma klucze <br> odpowiadające nazwie, cenie, opisowi, składnikom, typowi diety i kuchni.<br> Funkcja pobiera te dane z atrybutów obiektu, na którym jest wywoływana.<br> Ten kod jest przydatny w przypadku tworzenia aplikacji, które muszą <br> przechowywać i wyświetlać informacje o daniach.
    ><pre>
    > <b>params</b>: None<br>
    > <b>returns</b>: dict - Słownik zawierający wszystkie informacje o daniu.
    ></pre>

- **Dessert.py**

    Klasa ***Dessert*** dziedziczy po klasie Dish, która reprezentuje danie w menu.<br> Klasa ta definiuje w konstruktorze nazwę, cenę, opis, składniki, typ diety i <br> kuchnię. Dzięki dziedziczeniu klasa ***Dessert*** posiada te same cechy, ale <br> skupia się na deserach.<br>
    ><pre>
    > <b>params</b>: name, price, description, ingredients, diet_type, cuisine<br>
    >         <i>name</i>: str - Nazwa dania<br>
    >         <i>price</i>: list[str] | str - Koszt dania<br>
    >         <i>description</i>: str - Opis dania<br>
    >         <i>ingredients</i>: list[str] - Lista składników dania<br>
    >         <i>diet_type</i>: str - Rodzaj dania (czy zawiera mięso, czy jest wegańskie, czy wegetariańskie)<br>
    >         <i>cuisine</i>: str - Naród z jakiego pochodzi danie<br><br>
    > <b>returns</b>: None
    ></pre>


- **MainDish.py**

    Klasa ***MainDish.py*** dziedziczy po klasie Dish, która reprezentuje danie <br> główne. Konstruktor klasy przyjmuje argumenty takie jak nazwa, cena,<br> opis, składniki, typ diety oraz kuchnia, które są dziedziczone z klasy <br> nadrzędnej.<br>
    ><pre>
    > <b>params</b>: name, price, description, ingredients, diet_type, cuisine<br>
    >         <i>name</i>: str - Nazwa dania<br>
    >         <i>price</i>: list[str] | str - Koszt dania<br>
    >         <i>description</i>: str - Opis dania<br>
    >         <i>ingredients</i>: list[str] - Lista składników dania<br>
    >         <i>diet_type</i>: str - Rodzaj dania (czy zawiera mięso, czy jest wegańskie, czy wegetariańskie)<br>
    >         <i>cuisine</i>: str - Naród z jakiego pochodzi danie<br><br>
    > <b>returns</b>: None
    ></pre>


- **Starter.py**

    Klasa ***Starter*** dziedziczy po klasie "Dish". Klasa ta reprezentuje danie <br> przystawkowe, które może być tworzone z różnych składników i być <br> odpowiednie dla różnych typów diet oraz kuchni. Ta klasa posiada <br> konstruktor, który inicjuje pola takie jak nazwa, cena, opis, składniki, <br> typ dietetyczny oraz kuchnię, do której to danie należy.
    ><pre>
    > <b>params</b>: name, price, description, ingredients, diet_type, cuisine<br>
    >         <i>name</i>: str - Nazwa dania<br>
    >         <i>price</i>: list[str] | str - Koszt dania<br>
    >         <i>description</i>: str - Opis dania<br>
    >         <i>ingredients</i>: list[str] - Lista składników dania<br>
    >         <i>diet_type</i>: str - Rodzaj dania (czy zawiera mięso, czy jest wegańskie, czy wegetariańskie)<br>
    >         <i>cuisine</i>: str - Naród z jakiego pochodzi danie<br><br>
    > <b>returns</b>: None
    ></pre>


<hr>

## **Data**

***Data*** to folder zawierający pliki JSON z różnymi danymi potrzebnymi do działania systemu zarządzania restauracją. W pliku "menu_data.json" znajdują się informacje o potrawach, napojach i cenach oferowanych przez restaurację. W pliku "settings.json" przechowywane są ustawienia aplikacji, natomiast w "style_sheets.json" dane dotyczące stylizacji interfejsu graficznego. W "users_data.json" zapisane są informacje o użytkownikach systemu.

<hr>

## **Static**

*"Static"* to katalog, który zawiera pliki statyczne używane przez aplikację internetową lub mobilną.

### **Static/Images**

*"Static/Images"* to folder w którym przechowuje się statyczne pliki graficzne,<br> takie jak obrazki, które są ładowane na stronę internetową lub w aplikacji <br> mobilnej.

### **Static/Images/Icons**

*"Static/Images/Icons"* to podfolder w folderze *"Static/Images"*, który zawiera <br> ikony lub symbole, które są wykorzystywane na stronie internetowej lub w aplikacji mobilnej.

<hr>

# **Wymagane biblioteki**

- **PyQt5** - To biblioteka umożliwiająca tworzenie GUI (graficznych interfejsów użytkownika)
- **json** - JSON (JavaScript Object Notation) to format tekstowy, który <br>
             &emsp; &emsp; służy do przechowywania i wymiany danych między aplikacjami. 
- **os** - Biblioteka standardowa zawierająca wszystkie funkcje które pozwalają pracować na systemie operacyjnym.
- **datetime** - Biblioteka standardowa zawierająca funkcje które pozwalają pracować z datami i czasem.
- **sys** - Biblioteka standardowa zawierająca funkcje systemowe.

<hr>

# **Jak uruchomić projekt?**

1. Zainstalować Pythona https://www.python.org/doc/
2. Pobrać wszystkie biblioteki: <code>pip install -r requirements.txt</code>
3. Sprawdzić czy nie ma brakujących plików i następnie uruchomić plik <code>app.py</code>