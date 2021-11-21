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

* Datan hakeminen suoraan nettiosoitteesta ei onnistunut monen yrityksen jälkeen. Tarvitsen tähän apua.

#### TODO seuraavaksi

* Kirjautumistoiminnot
* Turvallisuus
* Statistiikan järjestely eri attribuuteilla
* Timestamp kommentteihin sekä kommentoijan nimi (kommentointi vain kirjautumalla?)
* Ohjelman jäsentely(tosin tässä vaiheessa koin helpommaksi kaiken olevan yhdessä tiedostossa)

#### Kehitysideoita

* Sovellus voisi ehkä olla universaali pallo- tai urheilulajeihin, jossa aloitussivulla käyttäjä voisi laittaa CSV-tiedoston tai linkin, jonka perusteella data haetaan.


