Projekt zaliczeniowy na przedmiot Systemy Rozproszone, prowadzący dr. Bartłomiej Kubica.

Temat: 
Gra sieciowa „Guess who?” wykonana w języku Python.
Zespół:
Andrzej Moczulak 191705
Daniel Kazarnowicz 196169
Opis:
Gra sieciowa oparta na zasadach popularnej gry planszowej „Guess
who?”, wykorzystująca komunikację za pomocą socketów.

Instrukcja uruchomienia:
Do poprawnego działania na początku należy zainstalować bibliotekę PIL używając komendy 'pip install pillow'.
Gdy biblioteka jest juz poprawnie zainstalowana potrzeba uruchomić serwer komendą 'python serwer.py', a następnie
dołączyć do serwera dwóch graczy odpowiednio komendami 'python Gracz1.py' oraz 'python Gracz2.py'.
UWAGA! Każdą komendę musimy wpisać używając osobnych terminali, znajdując się w folderze 'Projekt'.

Zasady gry:
Na początku gry każdy z dwóch graczy otrzymuje informację o postaci, która została dla niego wylosowana przez program.
W czasie trwania gry informacja ta jest niedostępna dla przeciwnika.
Zadaniem gracza jest odgadnięcie postaci przeciwnika.
Każdy z graczy początkowo posiada 8 punktów.
Podczas rozpoczęcia każdemu wyświetlają się dwa okna. Jedno okno to okno wszystkich postaci dostępnych w grze.
Podczas przebiegu gry można odhaczać charaktery, które odrzuciliśmy na podstawie zadanych pytań klikając na postać.
W drugim oknie znajdują się pytania możliwe do zadania, aby dowiedzieć się jak najwięcej o postaci przeciwnika.
Po zadaniu pytania liczba punktów zmniejsza się o 1.
Gra dzieję się w czasie rzeczywistym - podczas zadawania pytań trzeba poczekać na pytanie od strony przeciwnika.
Gra kończy się wyborem i zatwierdzeniem odgadniętej postaci przeciwnika.
Wygrywa osoba, której udało zachować się więcej punktów.
