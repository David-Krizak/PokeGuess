# Pogodi Pokémona 🎮

Web-aplikacija „Pogodi Pokémona“ je jednostavna edukativna igra izrađena u Python Flask okviru, koja koristi vanjski REST API (PokeAPI) za dohvat podataka o Pokémonima.

Cilj igre je pogoditi ime nasumično odabranog Pokémona na temelju njegove siluete, uz ograničen broj pokušaja i mogućnost korištenja hintova.



## Funkcionalnosti

- Nasumični Pokémon (Generacija 1)
- Prikaz siluete Pokémona prije pogađanja
- Polje za unos odgovora
- Sustav od 3 života
- Sustav hintova (tip, visina, težina)
- Mogućnost odustajanja (Give up)
- Spremanje rezultata nakon završetka igre
- Multiplayer scoreboard (server-side, JSON)
- Overlay scoreboard preko igre
- Moderan i responzivan dizajn

---

## Korištene tehnologije

### Backend
- Python
- Flask
- REST API (PokeAPI)
- Session management (Flask session)
- JSON datoteka za pohranu rezultata

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript (Fetch API)
- CSS animacije i overlay komponente

## Način rada aplikacije

1. Aplikacija se automatski pokreće pri učitavanju stranice
2. Igrač vidi siluetu Pokémona
3. Igrač unosi naziv Pokémona
4. Sustav provjerava unos i smanjuje broj života ako je odgovor netočan
5. Nakon gubitka ili odustajanja prikazuje se modal za unos imena
6. Rezultat se sprema u scoreboard
7. Scoreboard se prikazuje kao overlay preko igre


## Instalacija i pokretanje

1. Klonirati repozitorij ili preuzeti projekt
2. Instalirati potrebne pakete:
   ```bash
   pip install -r requirements.txt
