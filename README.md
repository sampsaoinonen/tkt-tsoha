# NHL-jääkiekkoilijoiden arviointi- ja keskustelufoorumi

Sovelluksen avulla voidaan tarkastella erilaisia tilastoja NHL-jääkiekkoilijoista sekä arvostella pelikorttimaisesti pelaajien taitojen eri osa-alueita.

### Sovelluksen ominaisuuksia ovat:

* Käyttäjä voi luoda tunnuksen ja kirjautua sisään sekä ulos.
* käyttäjä voi hakea tilastoista haluamaansa tietoa eri attribuuteilla.
* Käyttäjä voi lisätä kommentteja pelaajien profiileihin.
* Käytttäjä voi arvioida numeerisesti pelaajien taitojen eri osa-aluieita pelaajien profiileihin.
* Ylläpitäjä voi kirjautua sisään sekä ulos. 
* Ylläpitäjä voi moderoida keskustelua.
* Sovellus hakee datan jääkiekkoilijoista sivustolta moneypuck.com CSV-muodossa



## Välipalautus 2

#### Toteutuneet toiminnot

* CSV-muodossa oleva data tallentuu players-tauluun
* Uudelleenkäynnistäessä olemassa oleva data ei tuplaannu
* Aloitussivu hakee datan sivulle
* Yksittäisiä pelaajia voi klilata, jolloin pääsee muuttuvalla id:llä tehtyyn pelaajan omaan sivuun
* Pelaajan sivulla näkyy pelajan data, kommentit pelaajasta ja kommenttikenttä alhaaalla
* Pelaaja sivun data tallentuu comments-tauluun, joka on liitetty players-tauluun id:llä

#### Vastaan tulleet hankaluudet

* Datan hakeminen suoraan nettiosoitteesta ei onnistunut monen yrityksen jälkeen.

#### TODO seuraavaksi

* Kirjautumistoiminnot
* Turvallisuus
* Statistiikan järjestely eri attribuuteilla
* Timestamp kommentteihin sekä kommentoijan nimi (kommentointi vain kirjautumalla?)
* Ohjelman jäsentely(tosin tässä vaiheessa koin helpommaksi kaiken olevan yhdessä tiedostossa)

#### Kehitysideoita

* Sovellus voisi ehkä olla universaali pallo- tai urheilulajeihin, jossa aloitussivulla käyttäjä voisi laittaa CSV-tiedoston tai linkin, jonka perusteella data haetaan.

## Välipalautus 3

#### Toteutuneet toiminnot
* Sovellus on jaoteltu selkeämmin useaan eri tiedostoon
* Statistiikkaa voi listata isommasta pienempään ja toisin päin
* Rekisteröinti ja kirjautuminen mahdollista
* Kommentointi mahdollista vain kirjautuneena
* Kommentti-kentän validointi
* Rekisteröitynyt voi uploadata csv-tiedoston
* Taulun sarakkeiden nimet haetaan suoraan csv-tiedostosta eli ohjelma tulee olemaan ns. universaali csv-tiedostojen lukemiseen(pääosin tosin urhailu/palloilupeleihin tilastointi näkökulman takia)

#### Kesken olevat toiminnot
* Tarkoitus on, että rekisteröitynyt käyttäjä voi ottaa käyttöön lataamansa csv-tiedoston nyt ohjelmassa olevan esimerkki tiedoston tilalle. Tämä on vielä jonkun verran kesken.
* Tauluja pitäisi keksiä lisää(jos kerran tavoite on 5-10 taulua). Pelaajien arviointi voisi olla ainakin yksi.

#### Vastaantulleet haasteet
* Ohjelman muuttaminen geneeriseksi eri csv-tiedostoille olikin monimutkaisempaa sekä työläämpää kuin oletin, mutta on nyt hyvällä mallilla.
* Kun kaikki luotavan taulun sarakkeet luodaan csv-tiedostosta ovat ne muotoa text. Tällöin on numeroiden ja nimien järjestykseen laittaminen haastavaa. Tähän toivoisin vinkkejä. Nyt numerot ovat järjestyksessä, mutta nimien aakkostaminen ei taas onnistu(varsinkaan kun koko nimi on samassa sarakkeessa). Myöskään jääkiekossa olevat +/- tilastot eivät järjesty oikein.

#### TODO

* Käyttäjän omasta csv-tiedosta taulujen luonti loppuun
* Simppeleitä lisätoimintoja joista pari taulua lisää

## Lopullinen palautus

#### Toteutuneet toiminnot

* Käyttäjä voi kirjautua sisään
* Käyttäjä voi pelaajia kommentoida vain kirjautuneena
* Käyttäjä voi kirjautuneena tykätä pelaajasta ja tykkäysten summa näytetään sivulla
* Käyttäjä voi ladata tiedoston vain kirjautuneena
* Halutessaan tiedoston voi klikata "hidden", jolloin se näkyy vain käyttäjälle itselleen
* Ohjelma muuttaa CSV-tiedoston tiedoksi sql-tauluihin
* Timestampit kommenteissa ja tiedoston latauksissa
* Käyttäjä voi järjestää eri tavoin tilastot pelaajista



#### Vastaantulleet haasteet

* Mietin monta tuntia miksi sovellus ei toiminut Herokussa - tmp-hakemistossa pitää olla yksi tiedosto pushatessa, että Heroku tunnistaa hakemiston(!!)
* Universaali CSV-tiedoston SQL-tauluihin muuttaja valmistui hyvin pitkälle, mutta SQL-haut olivat tässä tapauksessa rajoittuneita



## https://tsoha-csv-reader.herokuapp.com/